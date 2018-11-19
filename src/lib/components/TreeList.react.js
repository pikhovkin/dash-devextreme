import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import PropTypes from 'prop-types';

import {TreeList as DXTreeList} from 'devextreme-react';


export default class TreeList extends Component {
    constructor(props) {
        super(props);

        this.cellTemplate = this.cellTemplate.bind(this);
        this.headerCellTemplate = this.headerCellTemplate.bind(this);
        this._processCellTemplate = this._processCellTemplate.bind(this);
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
        const { columns } = this.props;

        this._processCellTemplate(columns);

        return <DXTreeList columns={columns} {...this.props}/>;
    }
}

TreeList.propTypes = {
    id: PropTypes.string,

    accessKey: PropTypes.string,
    activeStateEnabled: PropTypes.bool,
    allowColumnReordering: PropTypes.bool,
    allowColumnResizing: PropTypes.bool,
    autoExpandAll: PropTypes.bool,
    cacheEnabled: PropTypes.bool,
    cellHintEnabled: PropTypes.bool,
    columnAutoWidth: PropTypes.bool,
    columnChooser: PropTypes.object,
    columnFixing: PropTypes.object,
    columnHidingEnabled: PropTypes.bool,
    columnMinWidth: PropTypes.number,
    columnResizingMode: PropTypes.oneOf(['nextColumn', 'widget']),
    columns: PropTypes.arrayOf(PropTypes.shape),
    columnWidth: PropTypes.number,
    customizeColumns: PropTypes.func,
    dataSource: PropTypes.oneOfType([PropTypes.string, PropTypes.arrayOf(PropTypes.object)]),
    dataStructure: PropTypes.oneOf(['plain', 'tree']),
    dateSerializationFormat: PropTypes.string,
    disabled: PropTypes.bool,
    editing: PropTypes.object,
    elementAttr: PropTypes.object,
    errorRowEnabled: PropTypes.bool,
    expandedRowKeys: PropTypes.oneOfType([PropTypes.arrayOf(PropTypes.string), PropTypes.arrayOf(PropTypes.number)]),
    expandNodesOnFiltering: PropTypes.bool,
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
    hasItemsExpr: PropTypes.oneOfType([PropTypes.string, PropTypes.func]),
    headerFilter: PropTypes.object,
    height: PropTypes.oneOfType([PropTypes.string, PropTypes.number, PropTypes.func]),
    highlightChanges: PropTypes.bool,
    hint: PropTypes.string,
    hoverStateEnabled: PropTypes.bool,
    itemsExpr: PropTypes.oneOfType([PropTypes.string, PropTypes.func]),
    keyExpr: PropTypes.oneOfType([PropTypes.string, PropTypes.func]),
    loadPanel: PropTypes.object,
    noDataText: PropTypes.string,
    onAdaptiveDetailRowPreparing: PropTypes.func,
    onCellClick: PropTypes.oneOfType([PropTypes.string, PropTypes.func]),
    onCellHoverChanged: PropTypes.func,
    onCellPrepared: PropTypes.func,
    onContentReady: PropTypes.func,
    onContextMenuPreparing: PropTypes.func,
    onDataErrorOccurred: PropTypes.func,
    onDisposing: PropTypes.func,
    onEditingStart: PropTypes.func,
    onEditorPrepared: PropTypes.func,
    onEditorPreparing: PropTypes.func,
    onFocusedCellChanged: PropTypes.func,
    onFocusedCellChanging: PropTypes.func,
    onFocusedRowChanged: PropTypes.func,
    onFocusedRowChanging: PropTypes.func,
    onInitialized: PropTypes.func,
    onInitNewRow: PropTypes.func,
    onKeyDown: PropTypes.func,
    onNodesInitialized: PropTypes.func,
    onOptionChanged: PropTypes.func,
    onRowClick: PropTypes.oneOfType([PropTypes.string, PropTypes.func]),
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
    parentIdExpr: PropTypes.oneOfType([PropTypes.string, PropTypes.func]),
    remoteOperations: PropTypes.object,
    renderAsync: PropTypes.bool,
    repaintChangesOnly: PropTypes.bool,
    rootValue: PropTypes.object,
    rowAlternationEnabled: PropTypes.bool,
    rtlEnabled: PropTypes.bool,
    scrolling: PropTypes.object,
    searchPanel: PropTypes.object,
    selectedRowKeys: PropTypes.arrayOf(PropTypes.any),
    selection: PropTypes.object,
    showBorders: PropTypes.bool,
    showColumnHeaders: PropTypes.bool,
    showColumnLines: PropTypes.bool,
    showRowLines: PropTypes.bool,
    sorting: PropTypes.object,
    stateStoring: PropTypes.object,
    tabIndex: PropTypes.number,
    twoWayBindingEnabled: PropTypes.bool,
    visible: PropTypes.bool,
    width: PropTypes.oneOfType([PropTypes.string, PropTypes.number, PropTypes.func]),
    wordWrapEnabled: PropTypes.bool,

    // Dash supplied props
    setProps: PropTypes.func
};

TreeList.defaultProps = {
    accessKey: null,
    activeStateEnabled: false,
    allowColumnReordering: false,
    allowColumnResizing: false,
    autoExpandAll: false,
    cacheEnabled: true,
    cellHintEnabled: true,
    columnAutoWidth: false,
    // columnChooser
    // columnFixing
    columnHidingEnabled: false,
    columnMinWidth: undefined,
    columnResizingMode: 'nextColumn',
    columns: undefined,
    columnWidth: undefined,
    // customizeColumns
    dataSource: null,
    dataStructure: 'plain',
    // dateSerializationFormat
    disabled: false,
    // editing
    elementAttr: {},
    errorRowEnabled: true,
    expandedRowKeys: [],
    expandNodesOnFiltering: true,
    filterBuilder: {},
    filterBuilderPopup: {},
    filterPanel: {},
    // filterRow
    // filterSyncEnabled
    filterValue: null,
    focusedColumnIndex: -1,
    focusedRowEnabled: false,
    focusedRowIndex: -1,
    focusedRowKey: undefined,
    focusStateEnabled: false,
    // hasItemsExpr
    // headerFilter
    height: undefined,
    highlightChanges: false,
    hint: undefined,
    hoverStateEnabled: false,
    itemsExpr: 'items',
    keyExpr: 'id',
    // loadPanel
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
    onFocusedCellChanged: null,
    onFocusedCellChanging: null,
    onFocusedRowChanged: null,
    onFocusedRowChanging: null,
    onInitialized: null,
    onInitNewRow: null,
    onKeyDown: null,
    onNodesInitialized: null,
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
    parentIdExpr: 'parentId',
    // remoteOperations
    renderAsync: false,
    repaintChangesOnly: false,
    rootValue: 0,
    rowAlternationEnabled: false,
    rtlEnabled: false,
    // scrolling
    // searchPanel
    // selectedRowKeys
    // selection
    showBorders: false,
    showColumnHeaders: true,
    showColumnLines: true, // false (Material)
    showRowLines: false, // true (iOS, Material)
    // sorting
    // stateStoring
    tabIndex: 0,
    twoWayBindingEnabled: true,
    visible: true,
    width: undefined,
    wordWrapEnabled: false
};
