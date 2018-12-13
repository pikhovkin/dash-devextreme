import React, {Component} from 'react';
import PropTypes from 'prop-types';

import {TextBox as DXTextBox} from 'devextreme-react';


export default class TextBox extends Component {
    constructor(props) {
        super(props);

        this.onValueChanged = this.onValueChanged.bind(this);
    }

    onValueChanged(e) {
        const {setProps} = this.props;

        if (setProps) setProps({value: e.value});
    }

    render() {
        return (
            <DXTextBox {...this.props}
                onValueChanged={this.props.onValueChanged || this.onValueChanged}
            />
        );
    }
}

TextBox.propTypes = {
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
    inputAttr: PropTypes.object,
    isValid: PropTypes.bool,
    mask: PropTypes.string,
    maskChar: PropTypes.string,
    maskInvalidMessage: PropTypes.string,
    maskRules: PropTypes.object,
    maxLength: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    mode: PropTypes.oneOf(['email', 'password', 'search', 'tel', 'text', 'url']),
    name: PropTypes.string,
    onChange: PropTypes.func,
    onContentReady: PropTypes.func,
    onCopy: PropTypes.func,
    onCut: PropTypes.func,
    onDisposing: PropTypes.func,
    onEnterKey: PropTypes.func,
    onFocusIn: PropTypes.func,
    onFocusOut: PropTypes.func,
    onInitialized: PropTypes.func,
    onInput: PropTypes.func,
    onKeyDown: PropTypes.func,
    onKeyPress: PropTypes.func,
    onKeyUp: PropTypes.func,
    onOptionChanged: PropTypes.func,
    onPaste: PropTypes.func,
    onValueChanged: PropTypes.func,
    placeholder: PropTypes.string,
    readOnly: PropTypes.bool,
    rtlEnabled: PropTypes.bool,
    showClearButton: PropTypes.bool,
    showMaskMode: PropTypes.oneOf(['always', 'onFocus']),
    spellcheck: PropTypes.bool,
    stylingMode: PropTypes.oneOf(['outlined', 'underlined', 'filled']),
    tabIndex: PropTypes.number,
    useMaskedValue: PropTypes.bool,
    validationError: PropTypes.object,
    validationMessageMode: PropTypes.oneOf(['always', 'auto']),
    value: PropTypes.string,
    valueChangeEvent: PropTypes.string,
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

TextBox.defaultProps = {
    accessKey: null,
    activeStateEnabled: false,
    disabled: false,
    elementAttr: {},
    focusStateEnabled: true,
    height: undefined,
    hint: undefined,
    hoverStateEnabled: true,
    inputAttr: {},
    isValid: true,
    mask: '',
    maskChar: '_',
    maskInvalidMessage: 'Value is invalid',
    maskRules: {},
    maxLength: null,
    mode: 'text',
    name: '',
    onChange: null,
    onContentReady: null,
    onCopy: null,
    onCut: null,
    onDisposing: null,
    onEnterKey: null,
    onFocusIn: null,
    onFocusOut: null,
    onInitialized: null,
    onInput: null,
    onKeyDown: null,
    onKeyPress: null,
    onKeyUp: null,
    onOptionChanged: null,
    onPaste: null,
    onValueChanged: null,
    placeholder: '',
    readOnly: false,
    rtlEnabled: false,
    showClearButton: false,
    showMaskMode: 'always',
    spellcheck: false,
    stylingMode: 'outlined',
    tabIndex: 0,
    useMaskedValue: false,
    validationError: undefined,
    validationMessageMode: 'auto',
    value: '',
    valueChangeEvent: 'change',
    visible: true,
    width: undefined
};
