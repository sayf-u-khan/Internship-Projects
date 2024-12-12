import base64
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import matplotlib.pyplot as plt
import seaborn as sns
import io
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Basic into code

@app.get("/")
async def read_root():
    return {"message": "Welcome to my FastAPI app!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

# Designs a plot that is streamed back to react

@app.get("/plot")
async def get_plot():

    data = sns.load_dataset("iris")

    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x="sepal_length", y="sepal_width", hue="species")
    plt.title("Iris Sepal Length vs Width")
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0) 
    plt.close()

    return StreamingResponse(buf, media_type="image/png")

# This is code that displays when a button is pressed in react

@app.get("/code")
async def exec_message():
    def message():
        return "Hello World!"

    result = message()
    return {"message": result}

# Input a string of numbers in react and get some data analysis back

@app.post("/analyse-data")
async def analyse_data(data: list[float]):

    data = sorted(data)

    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data)

    # Scatter plot

    x = np.arange(1, len(data) + 1)
    y = np.array(data)

    coefficients = np.polyfit(x, y, 1)  # Linear fit
    polynomial = np.poly1d(coefficients)
    y_fit = polynomial(x)

    plt.figure(figsize=(8, 4))
    plt.scatter(x, y, color='blue', label='Data Points')
    plt.plot(x, y_fit, color='red', label='Line of Best Fit')
    plt.axhline(y=mean, color='green', linestyle='--', label='Mean')
    plt.axhline(y=median, color='purple', linestyle='--', label='Median')
    plt.title('Scatter Plot with Line of Best Fit')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    plot_data = base64.b64encode(buf.read()).decode('utf-8')
    
    return {
        "mean": mean,
        "median": median,
        "std_dev": std_dev,
        "plot": f"data:image/png;base64,{plot_data}"
    }