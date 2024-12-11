import React, { useState } from 'react';
import { create, all } from 'mathjs';
import './calculator.css';

const CalculatorCode = () => {
    const [input, setInput] = useState('');
    const [result, setResult] = useState('');

    const handleButtonClick = (value) => {
        if (value === '=') {
            try {
                const evaluatedResult = evaluateExpression(input);
                setResult(evaluatedResult);
                checkForSecretCode(input);
            } catch (error) {
                setResult('Error');
            }
        } else if (value === ('C')) {
            setResult('');
        } else if (value === ('AC')) {
            setInput('');
            setResult('');
        } else {
            setInput(input + value);
        }
    };

    const math = create(all);

    const evaluateExpression = (expr) => {
        expr = expr.replace(/(\d+)%/g, '($1 * 0.01)');
        return math.evaluate(expr);
    };

    const checkForSecretCode = (input) => {
        if (input === '0.571046') {
            alert("You've unlocked a piece of my heart! Remember, even in the chaos of time, you have the power to create your own destiny. Keep shining bright! 🌟")
        }
    };

    return (
        <div className="calculator">
            <div className="display">
                <div className="input">{input}</div>
                <div className="result">{result}</div>
            </div>
            <div className="button-grid">

                <button className='top-row-button' onClick={() => handleButtonClick('AC')}>AC</button>
                <button className='top-row-button' onClick={() => handleButtonClick('-')}>±</button>
                <button className='top-row-button' onClick={() => handleButtonClick('%')}>%</button>
                <button className='operation-button' onClick={() => handleButtonClick('/')}>÷</button>

                <button className='number-button' onClick={() => handleButtonClick(7)}>7</button>
                <button className='number-button' onClick={() => handleButtonClick(8)}>8</button>
                <button className='number-button' onClick={() => handleButtonClick(9)}>9</button>
                <button className='operation-button' onClick={() => handleButtonClick('*')}>×</button>

                <button className='number-button' onClick={() => handleButtonClick(4)}>4</button>
                <button className='number-button' onClick={() => handleButtonClick(5)}>5</button>
                <button className='number-button' onClick={() => handleButtonClick(6)}>6</button>
                <button className='operation-button' onClick={() => handleButtonClick('-')}>-</button>

                <button className='number-button' onClick={() => handleButtonClick(1)}>1</button>
                <button className='number-button' onClick={() => handleButtonClick(2)}>2</button>
                <button className='number-button' onClick={() => handleButtonClick(3)}>3</button>
                <button className='operation-button' onClick={() => handleButtonClick('+')}>+</button>

                <button className='number-button' onClick={() => handleButtonClick('C')}>C</button>
                <button className='number-button' onClick={() => handleButtonClick(0)}>0</button>
                <button className='number-button' onClick={() => handleButtonClick('.')}>.</button>
                <button className='operation-button' onClick={() => handleButtonClick('=')}>=</button>
            </div>
        </div>
    );
};

export default CalculatorCode;