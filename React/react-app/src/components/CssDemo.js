import React from 'react';
import './CssDemo.css';

const CssDemo = () => {
    return (
        <div>
            <h1>CSS Positioning</h1>

            <div className="static">Static Position</div>

            <div className="relative">Relative Position</div>

            <div style={{ position: 'relative', height: '200px', border: '1px solid #ccc' }}>
                <div className="absolute">Absolute Position (relative to the parent)</div>
            </div>

            <div className="fixed">Fixed Position (remains fixed when scrolling)</div>

            <div style={{ height: '400px', border: '1px solid #ccc' }}>
                <div className="sticky">Sticky Position (sticks to the top when scrolling)</div>
                <p>Scroll down to see the sticky effect.</p>
                <p style={{ height: '800px' }}>More content here to enable scrolling.</p>
            </div>

            <div className="z-index-example">Z-Index Example 1 (lower z-index)</div>
            <div className="z-index-example2">Z-Index Example 2 (higher z-index)</div>
        </div>
    );
};

export default CssDemo;