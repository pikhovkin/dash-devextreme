import React, {Component} from 'react';
import PropTypes from 'prop-types';

import {TextBox as DXTextBox} from 'devextreme-react';


export default class TextBox extends Component {
    render() {
        const {setProps} = this.props;

        return (
            <DXTextBox
                id={this.props.id}
                value={this.props.value}
                onValueChanged={e => {
                    /*
                     * Send the new value to the parent component.
                     * In a Dash app, this will send the data back to the
                     * Python Dash app server.
                     */
                     if (setProps) {
                         setProps({
                            value: e.value
                        });
                     }
                }}
                valueChangeEvent={this.props.valueChangeEvent}
            />
        );
    }
}

TextBox.propTypes = {
    /**
     * The ID used to identify this compnent in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * The value displayed in the input
     */
    value: PropTypes.string,

    valueChangeEvent: PropTypes.string,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func
};
