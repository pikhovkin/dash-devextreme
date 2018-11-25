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
        const {columns, setProps} = this.props;
        let {rowTemplate} = this.props;

        this._processCellTemplate(columns);

        if (rowTemplate && typeof rowTemplate === 'string'){
            rowTemplate = this.rowTemplate(rowTemplate);
        }

        return (
            <DXDataGrid {...this.props}
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
            />
        );
    }
}

DataGrid.propTypes = {
    id: PropTypes.string,

    accessKey: PropTypes.string,
    activeStateEnabled: PropTypes.bool,
    allowColumnReordering: PropTypes.bool,
    allowColumnResizing: PropTypes.bool,
    cacheEnabled: PropTypes.bool,
    cellHintEnabled: PropTypes.bool,
    columnAutoWidth: PropTypes.bool,
    columnChooser: PropTypes.object,
    columnFixing: PropTypes.object,
    columnHidingEnabled: PropTypes.bool,
    columnMinWidth: PropTypes.number,
    columnResizingMode: PropTypes.oneOf(['nextColumn', 'widget']),
    columns: PropTypes.arrayOf(PropTypes.object),
    columnWidth: PropTypes.number,
    customizeColumns: PropTypes.func,
    customizeExportData: PropTypes.func,
    dataSource: PropTypes.oneOfType([PropTypes.object, PropTypes.arrayOf(PropTypes.object)]),
    dateSerializationFormat: PropTypes.string,
    disabled: PropTypes.bool,
    editing: PropTypes.object,
    elementAttr: PropTypes.object,
    errorRowEnabled: PropTypes.bool,
    export: PropTypes.object,
    filterBuilder: PropTypes.object,
    filterBuilderPopup: PropTypes.object,
    filterPanel: PropTypes.object,
    filterRow: PropTypes.object,
    filterSyncEnabled: PropTypes.bool,
    filterValue: PropTypes.object,
    focusedColumnIndex: PropTypes.number,
    focusedRowEnabled: PropTypes.bool,
    focusedRowIndex: PropTypes.number,
    focusedRowKey: PropTypes.any,
    focusStateEnabled: PropTypes.bool,
    grouping: PropTypes.object,
    groupPanel: PropTypes.object,
    headerFilter: PropTypes.object,
    height: PropTypes.oneOfType([PropTypes.number, PropTypes.string, PropTypes.func]),
    highlightChanges: PropTypes.bool,
    hint: PropTypes.string,
    hoverStateEnabled: PropTypes.bool,
    keyExpr: PropTypes.oneOfType([PropTypes.string, PropTypes.arrayOf(PropTypes.string)]),
    loadPanel: PropTypes.object,
    masterDetail: PropTypes.object,
    noDataText: PropTypes.string,
    onAdaptiveDetailRowPreparing: PropTypes.func,
    onCellClick: PropTypes.oneOfType([PropTypes.func, PropTypes.string]),
    onCellHoverChanged: PropTypes.func,
    onCellPrepared: PropTypes.func,
    onContentReady: PropTypes.func,
    onContextMenuPreparing: PropTypes.func,
    onDataErrorOccurred: PropTypes.func,
    onDisposing: PropTypes.func,
    onEditingStart: PropTypes.func,
    onEditorPrepared: PropTypes.func,
    onEditorPreparing: PropTypes.func,
    onExported: PropTypes.func,
    onExporting: PropTypes.func,
    onFileSaving: PropTypes.func,
    onFocusedCellChanged: PropTypes.func,
    onFocusedCellChanging: PropTypes.func,
    onFocusedRowChanged: PropTypes.func,
    onFocusedRowChanging: PropTypes.func,
    onInitialized: PropTypes.func,
    onInitNewRow: PropTypes.func,
    onKeyDown: PropTypes.func,
    onOptionChanged: PropTypes.func,
    onRowClick: PropTypes.oneOfType([PropTypes.func, PropTypes.string]),
    onRowCollapsed: PropTypes.func,
    onRowCollapsing: PropTypes.func,
    onRowExpanded: PropTypes.func,
    onRowExpanding: PropTypes.func,
    onRowInserted: PropTypes.func,
    onRowInserting: PropTypes.func,
    onRowPrepared: PropTypes.func,
    onRowRemoved: PropTypes.func,
    onRowRemoving: PropTypes.func,
    onRowUpdated: PropTypes.func,
    onRowUpdating: PropTypes.func,
    onRowValidating: PropTypes.func,
    onSelectionChanged: PropTypes.func,
    onToolbarPreparing: PropTypes.func,
    pager: PropTypes.object,
    paging: PropTypes.object,
    remoteOperations: PropTypes.oneOfType([PropTypes.bool, PropTypes.object]),
    renderAsync: PropTypes.bool,
    repaintChangesOnly: PropTypes.bool,
    rowAlternationEnabled: PropTypes.bool,
    rowTemplate: PropTypes.string,
    rtlEnabled: PropTypes.bool,
    scrolling: PropTypes.object,
    searchPanel: PropTypes.object,
    selectedRowKeys: PropTypes.arrayOf(PropTypes.any),
    selection: PropTypes.object,
    selectionFilter: PropTypes.arrayOf(PropTypes.shape),
    showBorders: PropTypes.bool,
    showColumnHeaders: PropTypes.bool,
    showColumnLines: PropTypes.bool,
    showRowLines: PropTypes.bool,
    sortByGroupSummaryInfo: PropTypes.arrayOf(PropTypes.object),
    sorting: PropTypes.object,
    stateStoring: PropTypes.object,
    summary: PropTypes.object,
    tabIndex: PropTypes.number,
    twoWayBindingEnabled: PropTypes.bool,
    visible: PropTypes.bool,
    width: PropTypes.oneOfType([PropTypes.number, PropTypes.string, PropTypes.func]),
    wordWrapEnabled: PropTypes.bool,

    // Dash supplied props
    setProps: PropTypes.func
};

DataGrid.defaultProps = {
    accessKey: null,
    activeStateEnabled: false,
    allowColumnReordering: false,
    allowColumnResizing: false,
    cacheEnabled: true,
    cellHintEnabled: true,
    columnAutoWidth: false,
    // columnChooser
    // columnFixing
    columnHidingEnabled: false,
    // columnMinWidth
    columnResizingMode: 'nextColumn',
    // columns
    // columnWidth
    // customizeColumns
    // customizeExportData
    dataSource: null,
    // dateSerializationFormat
    disabled: false,
    // editing
    elementAttr: {},
    errorRowEnabled: true,
    // export
    filterBuilder: {},
    filterBuilderPopup: {},
    filterPanel: {},
    // filterRow
    // filterSyncEnabled
    filterValue: null,
    focusedColumnIndex: -1,
    focusedRowEnabled: false,
    focusedRowIndex: -1,
    // focusedRowKey
    focusStateEnabled: false,
    // grouping
    // groupPanel
    // headerFilter
    // height
    highlightChanges: false,
    // hint
    hoverStateEnabled: false,
    // keyExpr
    // loadPanel
    // masterDetail
    noDataText: 'No data',
    onAdaptiveDetailRowPreparing: null,
    onCellClick: null,
    onCellHoverChanged: null,
    onCellPrepared: null,
    onContentReady: null,
    onContextMenuPreparing: null,
    onDataErrorOccurred: null,
    onDisposing: null,
    onEditingStart: null,
    onEditorPrepared: null,
    onEditorPreparing: null,
    onExported: null,
    onExporting: null,
    onFileSaving: null,
    onFocusedCellChanged: null,
    onFocusedCellChanging: null,
    onFocusedRowChanged: null,
    onFocusedRowChanging: null,
    onInitialized: null,
    onInitNewRow: null,
    onKeyDown: null,
    onOptionChanged: null,
    onRowClick: null,
    onRowCollapsed: null,
    onRowCollapsing: null,
    onRowExpanded: null,
    onRowExpanding: null,
    onRowInserted: null,
    onRowInserting: null,
    onRowPrepared: null,
    onRowRemoved: null,
    onRowRemoving: null,
    onRowUpdated: null,
    onRowUpdating: null,
    onRowValidating: null,
    onSelectionChanged: null,
    onToolbarPreparing: null,
    // pager
    // paging
    // remoteOperations
    renderAsync: false,
    repaintChangesOnly: false,
    rowAlternationEnabled: false,
    // rowTemplate
    rtlEnabled: false,
    // scrolling
    // searchPanel
    // selectedRowKeys
    // selection
    selectionFilter: [],
    showBorders: false,
    showColumnHeaders: true,
    showColumnLines: true, // false (Material)
    showRowLines: false, // true (iOS, Material)
    // sortByGroupSummaryInfo
    // sorting
    // stateStoring
    // summary
    tabIndex: 0,
    twoWayBindingEnabled: true,
    visible: true,
    // width
    wordWrapEnabled: false,
};
