import React, {Component} from 'react';
import PropTypes from 'prop-types';
import R from 'ramda';

import {SelectBox as DXSelectBox} from 'devextreme-react';


export default class SelectBox extends Component {
    constructor(props) {
        super(props);

        this.state = {
            value: props.value
        };

        this.onValueChanged = this.onValueChanged.bind(this);
    }

    onValueChanged(e) {
        const {setProps, fireEvent} = this.props;
        if (setProps) {
            setProps({
                value_changed: {value: e.value, previousValue: e.previousValue}
            });
        }
        this.setState({value: e.value});
        if (fireEvent) fireEvent('change');
    }

    render() {
        const {id, dataSource} = this.props;

        return (
            <DXSelectBox
                id={id}
                dataSource={dataSource}
                value={this.state.value}
                onValueChanged={this.onValueChanged}
              {...R.omit(['value', 'setProps', 'fireEvent'], this.props)}
            />
        );
    }
}

SelectBox.propTypes = {
    id: PropTypes.string,
    dataSource: PropTypes.object,
    value: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),

    // Dash supplied props
    setProps: PropTypes.func,

    dashEvents: PropTypes.oneOf(['change'])
};
