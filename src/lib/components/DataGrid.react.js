import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import PropTypes from 'prop-types';

import {DataGrid as DXDataGrid} from 'devextreme-react';


export default class DataGrid extends Component {
    constructor(props) {
        super(props);

        this.rowTemplate = this.rowTemplate.bind(this);
        this.cellTemplate = this.cellTemplate.bind(this);
        this.headerCellTemplate = this.headerCellTemplate.bind(this);
        this._processCellTemplate = this._processCellTemplate.bind(this);
    }

    rowTemplate(template_id) {
        var tmpl = window[template_id];
        return function(container, options) {
            const d = window.document.createElement('div');
            ReactDOM.render(tmpl(options), d);
            container.append(d.firstChild);
        }
    }

    cellTemplate(template_id) {
        var tmpl = window[template_id];
        return function(container, options) {
            ReactDOM.render(tmpl(options), container);
        }
    }

    headerCellTemplate(template_id) {
        var tmpl = window[template_id];
        return function(container, options) {
            ReactDOM.render(tmpl(options), container);
        }
    }

    _processCellTemplate(columns) {
        for(const c in columns){
            if (columns[c].cellTemplate && typeof columns[c].cellTemplate === 'string') {
                columns[c].cellTemplate = this.cellTemplate(columns[c].cellTemplate);
            }
            if (columns[c].headerCellTemplate && typeof columns[c].headerCellTemplate === 'string') {
                columns[c].headerCellTemplate = this.headerCellTemplate(columns[c].headerCellTemplate);
            }
            if (columns[c].columns && typeof columns[c].columns === 'object') {
                this._processCellTemplate(columns[c].columns);
            }
        }
    }

    render() {
        const {id, dataSource, setProps, columns} = this.props;
        let {rowTemplate} = this.props;

        this._processCellTemplate(columns);

        if (rowTemplate && typeof rowTemplate === 'string'){
            rowTemplate = this.rowTemplate(rowTemplate);
        }

        return (
            <DXDataGrid
                id={id}
                dataSource={dataSource}
                columns={columns}
                rowTemplate={rowTemplate}
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

    rowTemplate: PropTypes.string,

    // Dash supplied props
    setProps: PropTypes.func
};

DataGrid.defaultProps = {
    columnAutoWidth: true
};
