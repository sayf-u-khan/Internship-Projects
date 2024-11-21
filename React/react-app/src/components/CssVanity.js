import React from 'react';
import './CssVanity.css';

const CssVanity = () => {
    return (
        <div>
            <h1 class="h1c">This is the Title</h1>
            <p class="box">This text is in a box</p>
            <p class="highlight">This text is highlighted</p>
            <p class="block">Block with padding</p>
            <p class="inline">Inline text</p>
        </div>
    );
};

export default CssVanity;