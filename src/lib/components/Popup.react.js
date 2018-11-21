import React, {Component} from 'react';
import PropTypes from 'prop-types';

import {Popup as DXPopup} from 'devextreme-react';


export default class Popup extends Component {
    constructor(props) {
        super(props);

        this.state = {visible: this.props.visible};

        this.closeOnOutsideClick = this.closeOnOutsideClick.bind(this);
    }

    closeOnOutsideClick(e) {
        e;
        this.setState({visible: false});
        return true;
    }

    render() {
        return <DXPopup
            showTitle={this.props.showTitle}
            title={this.props.title}
            visible={this.state.visible}
            dragEnabled={this.props.dragEnabled}
            closeOnOutsideClick={this.closeOnOutsideClick}
            closeOnBackButton={this.props.closeOnBackButton}
        />
    }
}

Popup.propTypes = {
    /**
     * The ID used to identify this compnent in Dash callbacks
     */
    id: PropTypes.string,

    showTitle: PropTypes.bool,
    title: PropTypes.string,
    visible: PropTypes.bool,
    dragEnabled: PropTypes.bool,
    closeOnOutsideClick: PropTypes.bool,
    closeOnBackButton: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func
};
