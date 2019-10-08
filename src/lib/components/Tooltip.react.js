import React, {Component} from 'react';
import PropTypes from 'prop-types';

import {Tooltip as DXTooltip} from 'devextreme-react';


export default class Tooltip extends Component {
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
            <DXTooltip
                {...this.props}
                onInitialized={this.props.onInitialized || this.onInitialized}
                onShowing={this.props.onShowing || this.onShowing}
                onHiding={this.props.onHiding || this.onHiding}
                visible={this.state.visible}
                target={this.state.target}
            />
        )
    }
}

Tooltip.propTypes = {
    /**
     * The ID used to identify this compnent in Dash callbacks
     */
    id: PropTypes.string,

    animation: PropTypes.object,
    children: PropTypes.node,
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
    showEvent: PropTypes.oneOfType([PropTypes.object, PropTypes.string]),
    target: PropTypes.string,
    visible: PropTypes.bool,
    width: PropTypes.oneOfType([PropTypes.number, PropTypes.string, PropTypes.func]),

    setProps: PropTypes.func
};

Tooltip.defaultProps = {
    animation: {show: {type: 'fade', from: 0, to: 1}, hide: {type: 'fade', to: 0}},
    children: null,
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
    // showEvent: undefined,
    // target
    visible: false,
    width: 'auto'
};
