import React from 'react';
import './CssVanity.css';

const CssVanity = () => {
    return (
        <div>
            <h1 class="h1c">This is the Title</h1>
            <p class="padded-text box">This text is in a box</p>
            <p class="padded-text highlight">This text is highlighted</p>
            <p class="padded-text block">Block with padding</p>
            <p class="padded-text inline">Inline text</p>
            <p class='padded-text section1'>Highlight gradient</p>
            <p class='padded-text animate'>Animate gradient</p>
            <p class='padded-text hover-effect'>Drop shadow hover</p>
        </div>
    );
};

export default CssVanity;