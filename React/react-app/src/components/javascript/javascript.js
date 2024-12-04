import React from 'react';
import {Garage} from './functions';
import Test1 from './test';
import CarAvailability from './conditional';
import CarCategoriser from './categoriser';

const JavaScript = () => {
      return (
        <div>
            <h2>JavaScript For Loop</h2>
            <p id="demo">Car list:</p>
            <ul>
              <Garage />
            </ul>
          <div>
            <Test1 />
          </div>
          <div>
            <p>This is showcasing the use of conditional statements in JavaScript</p>
            <CarAvailability />
          </div>
          <div>
            <p>This is showcasing the use of categoriser in JavaScript</p>
            <CarCategoriser />
          </div>
        </div>
    );
};

export default JavaScript;