import React, {Component} from 'react';
import {TextBox} from '../src';

class Demo extends Component {
    constructor() {
        super();
        this.state = {
            value: ''
        }
    }

    render() {
        return (
            <div>
                <h1>dash-devextreme Demo</h1>

                <hr/>
                <h2>TextBox</h2>
                <TextBox
                    valueChangeEvent='input'
                    value={this.state.value}
                    setProps={newProps => this.setState({value: newProps.value})}
                />
                <hr/>
            </div>
        );
    }
}

export default Demo;
