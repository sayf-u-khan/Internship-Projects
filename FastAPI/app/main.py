from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import matplotlib.pyplot as plt
import seaborn as sns
import io

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to my FastAPI app!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

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