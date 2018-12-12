import React, {Component} from 'react';
import PropTypes from 'prop-types';

import {CheckBox as DXCheckBox} from 'devextreme-react';


export default class CheckBox extends Component {
    constructor(props) {
        super(props);

        this.state = {
            value: props.value,
            visible: props.visible,
            isValid: props.isValid,
            disabled: props.disabled,
        };

        this.onValueChanged = this.onValueChanged.bind(this);
    }

    onValueChanged(e) {
        const {setProps, fireEvent} = this.props;

        this.setState({value: e.value});
        if (setProps) setProps({value: e.value});
        if (fireEvent) fireEvent('change');
    }

    render() {
        return (
            <DXCheckBox {...this.props}
                value={this.state.value}
                visible={this.state.visible}
                isValid={this.state.isValid}
                disabled={this.state.disabled}
                onValueChanged={this.onValueChanged}
            />
        )
    }
}

CheckBox.propTypes = {
    /**
     * The ID used to identify this compnent in Dash callbacks
     */
    id: PropTypes.string,

    accessKey: PropTypes.string,
    activeStateEnabled: PropTypes.bool,
    disabled: PropTypes.bool,
    elementAttr: PropTypes.object,
    focusStateEnabled: PropTypes.bool,
    height: PropTypes.oneOfType([PropTypes.number, PropTypes.string, PropTypes.func]),
    hint: PropTypes.string,
    hoverStateEnabled: PropTypes.bool,
    isValid: PropTypes.bool,
    name: PropTypes.string,
    onContentReady: PropTypes.func,
    onDisposing: PropTypes.func,
    onInitialized: PropTypes.func,
    onOptionChanged: PropTypes.func,
    onValueChanged: PropTypes.func,
    readOnly: PropTypes.bool,
    rtlEnabled: PropTypes.bool,
    tabIndex: PropTypes.number,
    text: PropTypes.string,
    validationError: PropTypes.object,
    validationMessageMode: PropTypes.oneOf(['always', 'auto']),
    value: PropTypes.bool,
    visible: PropTypes.bool,
    width: PropTypes.oneOfType([PropTypes.number, PropTypes.string, PropTypes.func]),

    /**
     * Dash-assigned callback that gets fired when the checkbox item gets selected.
     */
    fireEvent: PropTypes.func,

    /**
     * Dash-assigned callback that gets fired when the value changes.
     */
    setProps: PropTypes.func,

    dashEvents: PropTypes.oneOf(['change']),
};

CheckBox.defaultProps = {
    accessKey: null,
    activeStateEnabled: true,
    disabled: false,
    elementAttr: {},
    focusStateEnabled: true,
    // height: undefined,
    // hint: undefined,
    hoverStateEnabled: true,
    isValid: true,
    name: '',
    onContentReady: null,
    onDisposing: null,
    onInitialized: null,
    onOptionChanged: null,
    onValueChanged: null,
    readOnly: false,
    rtlEnabled: false,
    tabIndex: 0,
    text: '',
    // validationError: undefined,
    validationMessageMode: 'auto',
    value: null,
    visible: true,
    width: ''
};
