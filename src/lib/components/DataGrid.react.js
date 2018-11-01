import React, {Component} from 'react';
import PropTypes from 'prop-types';

import {DataGrid as DXDataGrid} from 'devextreme-react';


export default class DataGrid extends Component {
    constructor(props) {
        super(props);

        this.cellTemplate = this.cellTemplate.bind(this);
    }

    render() {
        const {id, dataSource, setProps, columns} = this.props;

        return (
            <DXDataGrid
                id={id}
                dataSource={dataSource}
                columns={columns}
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
                columnAutoWidth={this.props.columnAutoWidth}
                grouping={this.props.grouping}
            />
        );
    }
}

DataGrid.propTypes = {
    id: PropTypes.string,

    dataSource: PropTypes.object,
    columns: PropTypes.arrayOf(PropTypes.shape),
    columnAutoWidth: PropTypes.bool,
    grouping: PropTypes.object,

    // Dash supplied props
    setProps: PropTypes.func
};

DataGrid.defaultProps = {
    columnAutoWidth: true
};
