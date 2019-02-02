import React, {Component} from 'react';
import PropTypes from 'prop-types';
import * as R from 'ramda';

import {SelectBox as DXSelectBox} from 'devextreme-react';


export default class SelectBox extends Component {
    constructor(props) {
        super(props);

        this.state = {
            value: props.value,
            opened: props.opened
        };

        this.onValueChanged = this.onValueChanged.bind(this);
        this.onOpened = this.onOpened.bind(this);
        this.onFocusOut = this.onFocusOut.bind(this);
    }

    onValueChanged(e) {
        const {setProps, fireEvent} = this.props;
        if (setProps) {
            setProps({
                value: {value: e.value, previousValue: e.previousValue}
            });
        }
        this.setState({value: e.value, opened: false});
        if (fireEvent) fireEvent({event: 'change'});
    }

    onOpened(e) {
        this.setState({opened: true});
    }

    onFocusOut(e) {
        this.setState({opened: false});
    }

    render() {
        return (
            <DXSelectBox
                items={this.props.dxItems}
                value={this.state.value}
                opened={this.state.opened}
                onValueChanged={this.props.onValueChanged || this.onValueChanged}
                onOpened={this.props.onOpened || this.onOpened}
                onFocusOut={this.props.onFocusOut || this.onFocusOut}
                {...R.omit(['opened', 'value', 'setProps', 'fireEvent', 'onOpened', 'onFocusOut', 'onValueChanged', 'dxItems'], this.props)}
            />
        );
    }
}

SelectBox.propTypes = {
    id: PropTypes.string,

    acceptCustomValue: PropTypes.bool,
    accessKey: PropTypes.string,
    activeStateEnabled: PropTypes.bool,
    dataSource: PropTypes.oneOfType([PropTypes.string, PropTypes.arrayOf(PropTypes.any)]),
    deferRendering: PropTypes.bool,
    disabled: PropTypes.bool,
    displayExpr: PropTypes.oneOfType([PropTypes.string, PropTypes.func]),
    dropDownButtonTemplate: PropTypes.string,
    elementAttr: PropTypes.object,
    fieldTemplate: PropTypes.string,
    focusStateEnabled: PropTypes.bool,
    grouped: PropTypes.bool,
    groupTemplate: PropTypes.string,
    height: PropTypes.oneOfType([PropTypes.number, PropTypes.string, PropTypes.func]),
    hint: PropTypes.string,
    hoverStateEnabled: PropTypes.bool,
    inputAttr: PropTypes.object,
    isValid: PropTypes.bool,
    dxItems: PropTypes.arrayOf(PropTypes.any),
    itemTemplate: PropTypes.string,
    maxLength: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    minSearchLength: PropTypes.number,
    name: PropTypes.string,
    noDataText: PropTypes.string,
    onChange: PropTypes.func,
    onClosed: PropTypes.func,
    onContentReady: PropTypes.func,
    onCopy: PropTypes.func,
    onCustomItemCreating: PropTypes.func,
    onCut: PropTypes.func,
    onDisposing: PropTypes.func,
    onEnterKey: PropTypes.func,
    onFocusIn: PropTypes.func,
    onFocusOut: PropTypes.func,
    onInitialized: PropTypes.func,
    onInput: PropTypes.func,
    onItemClick: PropTypes.func,
    onKeyDown: PropTypes.func,
    onKeyPress: PropTypes.func,
    onKeyUp: PropTypes.func,
    onOpened: PropTypes.func,
    onOptionChanged: PropTypes.func,
    onPaste: PropTypes.func,
    onSelectionChanged: PropTypes.func,
    onValueChanged: PropTypes.func,
    opened: PropTypes.bool,
    openOnFieldClick: PropTypes.bool,
    placeholder: PropTypes.string,
    readOnly: PropTypes.bool,
    rtlEnabled: PropTypes.bool,
    searchEnabled: PropTypes.bool,
    searchExpr: PropTypes.oneOfType([PropTypes.string, PropTypes.arrayOf(PropTypes.string)]),
    searchMode: PropTypes.oneOf(['contains', 'startswith']),
    searchTimeout: PropTypes.number,
    showClearButton: PropTypes.bool,
    showDataBeforeSearch: PropTypes.bool,
    showDropDownButton: PropTypes.bool,
    showSelectionControls: PropTypes.bool,
    spellcheck: PropTypes.bool,
    stylingMode: PropTypes.oneOf(['outlined', 'underlined', 'filled']),
    tabIndex: PropTypes.number,
    validationError: PropTypes.object,
    validationMessageMode: PropTypes.oneOf(['always', 'auto']),
    value: PropTypes.any,
    valueChangeEvent: PropTypes.string,
    valueExpr: PropTypes.oneOfType([PropTypes.string, PropTypes.func]),
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

SelectBox.defaultProps = {
    acceptCustomValue: false,
    accessKey: null,
    activeStateEnabled: true,
    dataSource: null,
    deferRendering: true,
    disabled: false,
    // displayExpr: undefined,
    dropDownButtonTemplate: 'dropDownButton',
    elementAttr: {},
    fieldTemplate: null,
    focusStateEnabled: true,
    grouped: false,
    groupTemplate: 'group',
    // height: undefined,
    // hint: undefined,
    hoverStateEnabled: true,
    inputAttr: {},
    isValid: true,
    dxItems: null,
    itemTemplate: 'item',
    maxLength: null,
    minSearchLength: 0,
    name: '',
    noDataText: 'No data to display',
    onChange: null,
    onClosed: null,
    onContentReady: null,
    onCopy: null,
    // onCustomItemCreating: function(e) { if(!e.customItem) { e.customItem = e.text; } },
    onCut: null,
    onDisposing: null,
    onEnterKey: null,
    onFocusIn: null,
    onFocusOut: null,
    onInitialized: null,
    onInput: null,
    onItemClick: null,
    onKeyDown: null,
    onKeyPress: null,
    onKeyUp: null,
    onOpened: null,
    onOptionChanged: null,
    onPaste: null,
    onSelectionChanged: null,
    onValueChanged: null,
    opened: false,
    openOnFieldClick: true,
    placeholder: 'Select',
    readOnly: false,
    rtlEnabled: false,
    searchEnabled: false,
    searchExpr: null,
    searchMode: 'contains',
    searchTimeout: 500,
    showClearButton: false,
    showDataBeforeSearch: false,
    showDropDownButton: true,
    showSelectionControls: false,
    spellcheck: false,
    stylingMode: 'outlined',
    tabIndex: 0,
    // validationError: undefined,
    validationMessageMode: 'auto',
    value: null,
    valueChangeEvent: 'change',
    valueExpr: 'this',
    visible: true,
    // width: undefined
};
