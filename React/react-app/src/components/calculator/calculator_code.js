import React, { useState } from 'react';
import { create, all } from 'mathjs';
import './calculator.css';

const CalculatorCode = () => {
    const [input, setInput] = useState('');
    const [result, setResult] = useState('');

    const handleButtonClick = (value) => {
        if (value === '=') {
            try {
                // Evaluate the expression safely
                const evaluatedResult = evaluateExpression(input);
                setResult(evaluatedResult);
            } catch (error) {
                setResult('Error');
            }
            setInput('');
        } else if (value === 'C') {
            setInput('');
            setResult('');
        } else {
            setInput(input + value);
        }
    };

    const math = create(all);

    const evaluateExpression = (expr) => {
    // Replace modulus operator with JavaScript's % operator
    expr = expr.replace(/%/g, '/100*');
    return math.evaluate(expr);
    };

    return (
        <div className="calculator">
            <div className="display">
                <div className="input">{input}</div>
                <div className="result">{result}</div>
            </div>
            <div className="cbuttons">
                {['7', '8', '9', '/'].map((item) => (
                    <button class='cbutton' key={item} onClick={() => handleButtonClick(item)}>
                        {item}
                    </button>
                ))}
                {['4', '5', '6', '*'].map((item) => (
                    <button class='cbutton' key={item} onClick={() => handleButtonClick(item)}>
                        {item}
                    </button>
                ))}
                {['1', '2', '3', '-'].map((item) => (
                    <button class='cbutton' key={item} onClick={() => handleButtonClick(item)}>
                        {item}
                    </button>
                ))}
                {['0', '%', '=', '+'].map((item) => (
                    <button class='cbutton' key={item} onClick={() => handleButtonClick(item)}>
                        {item}
                    </button>
                ))}
                <button className="clear" onClick={() => handleButtonClick('C')}>
                    C
                </button>
            </div>
        </div>
    );
};

export default CalculatorCode;