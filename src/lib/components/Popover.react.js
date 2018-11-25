import React, {Component} from 'react';
import PropTypes from 'prop-types';

import {Popover as DXPopover} from 'devextreme-react';


export default class Popover extends Component {
    constructor(props) {
        super(props);

        this.state = {visible: this.props.visible, target: this.props.target};

        this.onInitialized = this.onInitialized.bind(this);
        this.onShowing = this.onShowing.bind(this);
        this.onHiding = this.onHiding.bind(this);
    }

    onInitialized(e) {
        this.setState({target: document.getElementById(this.props.target)});
    }

    onShowing(e) {
        this.setState({visible: true});
    }

    onHiding(e) {
        this.setState({visible: false});
    }

    render() {
        return (
            <DXPopover {...this.props}
                onInitialized={this.props.onInitialized || this.onInitialized}
                onShowing={this.props.onShowing || this.onShowing}
                onHiding={this.props.onHiding || this.onHiding}
                visible={this.state.visible}
                target={this.state.target}
            />
        )
    }
}

Popover.propTypes = {
    /**
     * The ID used to identify this compnent in Dash callbacks
     */
    id: PropTypes.string,

    animation: PropTypes.object,
    closeOnBackButton: PropTypes.bool,
    closeOnOutsideClick: PropTypes.oneOfType([PropTypes.bool, PropTypes.func]),
    container: PropTypes.string,
    // contentTemplate: PropTypes.string,
    deferRendering: PropTypes.bool,
    disabled: PropTypes.bool,
    elementAttr: PropTypes.object,
    height: PropTypes.oneOfType([PropTypes.number, PropTypes.string, PropTypes.func]),
    hideEvent: PropTypes.oneOfType([PropTypes.object, PropTypes.string]),
    hint: PropTypes.string,
    hoverStateEnabled: PropTypes.bool,
    maxHeight: PropTypes.oneOfType([PropTypes.number, PropTypes.string, PropTypes.func]),
    maxWidth: PropTypes.oneOfType([PropTypes.number, PropTypes.string, PropTypes.func]),
    minHeight: PropTypes.oneOfType([PropTypes.number, PropTypes.string, PropTypes.func]),
    minWidth: PropTypes.oneOfType([PropTypes.number, PropTypes.string, PropTypes.func]),
    onContentReady: PropTypes.func,
    onDisposing: PropTypes.func,
    onHidden: PropTypes.func,
    onHiding: PropTypes.func,
    onInitialized: PropTypes.func,
    onOptionChanged: PropTypes.func,
    onShowing: PropTypes.func,
    onShown: PropTypes.func,
    position: PropTypes.oneOfType([PropTypes.oneOf(['bottom', 'left', 'right', 'top']), PropTypes.object]),
    rtlEnabled: PropTypes.bool,
    shading: PropTypes.bool,
    shadingColor: PropTypes.string,
    showCloseButton: PropTypes.bool,
    showEvent: PropTypes.oneOfType([PropTypes.object, PropTypes.string]),
    showTitle: PropTypes.bool,
    target: PropTypes.string,
    title: PropTypes.string,
    titleTemplate: PropTypes.string,
    toolbarItems: PropTypes.arrayOf(PropTypes.object),
    visible: PropTypes.bool,
    width: PropTypes.oneOfType([PropTypes.number, PropTypes.string, PropTypes.func]),

    setProps: PropTypes.func
};

Popover.defaultProps = {
    animation: {show: {type: 'fade', from: 0, to: 1}, hide: {type: 'fade', to: 0}},
    closeOnBackButton: true,
    closeOnOutsideClick: true,
    // container: undefined,
    // contentTemplate: 'content',
    deferRendering: true,
    disabled: false,
    elementAttr: {},
    height: 'auto',
    // hideEvent: undefined,
    // hint: undefined,
    hoverStateEnabled: false,
    maxHeight: null,
    maxWidth: null,
    minHeight: null,
    minWidth: null,
    onContentReady: null,
    onDisposing: null,
    onHidden: null,
    onHiding: null,
    onInitialized: null,
    onOptionChanged: null,
    onShowing: null,
    onShown: null,
    position: 'bottom',
    rtlEnabled: false,
    shading: false,
    shadingColor: '',
    showCloseButton: false, // true (desktop)
    // showEvent: undefined,
    showTitle: false,
    // target
    title: '',
    titleTemplate: 'title',
    // toolbarItems
    visible: false,
    width: 'auto'
};
