import React, {Component} from 'react';
import PropTypes from 'prop-types';

import {PivotGrid as DXPivotGrid} from 'devextreme-react';


export default class PivotGrid extends Component {
    render() {
        const {setProps} = this.props;

        return (
            <DXPivotGrid
                id={this.props.id}
                dataSource={this.props.dataSource}
                onCellClick={e => {
                    if (setProps) {
                        setProps({
                            cell: {
                                area: e.area,
                                cell: {
                                    columnPath: e.cell.columnPath,
                                    dataIndex: e.cell.dataIndex,
                                    expanded: e.cell.expanded,
                                    path: e.cell.path,
                                    rowPath: e.cell.rowPath,
                                    text: e.cell.text,
                                    value: e.cell.value
                                },
                                rowIndex: e.rowIndex,
                                columnIndex: e.columnIndex,
                                columnFields: e.columnFields,
                                rowFields: e.rowFields,
                                dataFields: e.dataFields
                            }
                        });
                    }
                }}
            />
        );
    }
}

PivotGrid.propTypes = {
    // These props are "custom" - defined by me.
    id: PropTypes.string,

    dataSource: PropTypes.object,

    // Dash supplied props
    setProps: PropTypes.func
};
