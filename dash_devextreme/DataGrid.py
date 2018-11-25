# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DataGrid(Component):
    """A DataGrid component.


Keyword arguments:
- id (string; optional)
- accessKey (string; optional)
- activeStateEnabled (boolean; optional)
- allowColumnReordering (boolean; optional)
- allowColumnResizing (boolean; optional)
- cacheEnabled (boolean; optional)
- cellHintEnabled (boolean; optional)
- columnAutoWidth (boolean; optional)
- columnChooser (dict; optional)
- columnFixing (dict; optional)
- columnHidingEnabled (boolean; optional)
- columnMinWidth (number; optional)
- columnResizingMode (a value equal to: 'nextColumn', 'widget'; optional)
- columns (list; optional)
- columnWidth (number; optional)
- dataSource (dict | list; optional)
- dateSerializationFormat (string; optional)
- disabled (boolean; optional)
- editing (dict; optional)
- elementAttr (dict; optional)
- errorRowEnabled (boolean; optional)
- export (dict; optional)
- filterBuilder (dict; optional)
- filterBuilderPopup (dict; optional)
- filterPanel (dict; optional)
- filterRow (dict; optional)
- filterSyncEnabled (boolean; optional)
- filterValue (dict; optional)
- focusedColumnIndex (number; optional)
- focusedRowEnabled (boolean; optional)
- focusedRowIndex (number; optional)
- focusedRowKey (boolean | number | string | dict | list; optional)
- focusStateEnabled (boolean; optional)
- grouping (dict; optional)
- groupPanel (dict; optional)
- headerFilter (dict; optional)
- height (number | string; optional)
- highlightChanges (boolean; optional)
- hint (string; optional)
- hoverStateEnabled (boolean; optional)
- keyExpr (string | list; optional)
- loadPanel (dict; optional)
- masterDetail (dict; optional)
- noDataText (string; optional)
- onCellClick (string; optional)
- onRowClick (string; optional)
- pager (dict; optional)
- paging (dict; optional)
- remoteOperations (boolean | dict; optional)
- renderAsync (boolean; optional)
- repaintChangesOnly (boolean; optional)
- rowAlternationEnabled (boolean; optional)
- rowTemplate (string; optional)
- rtlEnabled (boolean; optional)
- scrolling (dict; optional)
- searchPanel (dict; optional)
- selectedRowKeys (list; optional)
- selection (dict; optional)
- selectionFilter (list; optional)
- showBorders (boolean; optional)
- showColumnHeaders (boolean; optional)
- showColumnLines (boolean; optional)
- showRowLines (boolean; optional)
- sortByGroupSummaryInfo (list; optional)
- sorting (dict; optional)
- stateStoring (dict; optional)
- summary (dict; optional)
- tabIndex (number; optional)
- twoWayBindingEnabled (boolean; optional)
- visible (boolean; optional)
- width (number | string; optional)
- wordWrapEnabled (boolean; optional)

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, accessKey=Component.UNDEFINED, activeStateEnabled=Component.UNDEFINED, allowColumnReordering=Component.UNDEFINED, allowColumnResizing=Component.UNDEFINED, cacheEnabled=Component.UNDEFINED, cellHintEnabled=Component.UNDEFINED, columnAutoWidth=Component.UNDEFINED, columnChooser=Component.UNDEFINED, columnFixing=Component.UNDEFINED, columnHidingEnabled=Component.UNDEFINED, columnMinWidth=Component.UNDEFINED, columnResizingMode=Component.UNDEFINED, columns=Component.UNDEFINED, columnWidth=Component.UNDEFINED, customizeColumns=Component.UNDEFINED, customizeExportData=Component.UNDEFINED, dataSource=Component.UNDEFINED, dateSerializationFormat=Component.UNDEFINED, disabled=Component.UNDEFINED, editing=Component.UNDEFINED, elementAttr=Component.UNDEFINED, errorRowEnabled=Component.UNDEFINED, export=Component.UNDEFINED, filterBuilder=Component.UNDEFINED, filterBuilderPopup=Component.UNDEFINED, filterPanel=Component.UNDEFINED, filterRow=Component.UNDEFINED, filterSyncEnabled=Component.UNDEFINED, filterValue=Component.UNDEFINED, focusedColumnIndex=Component.UNDEFINED, focusedRowEnabled=Component.UNDEFINED, focusedRowIndex=Component.UNDEFINED, focusedRowKey=Component.UNDEFINED, focusStateEnabled=Component.UNDEFINED, grouping=Component.UNDEFINED, groupPanel=Component.UNDEFINED, headerFilter=Component.UNDEFINED, height=Component.UNDEFINED, highlightChanges=Component.UNDEFINED, hint=Component.UNDEFINED, hoverStateEnabled=Component.UNDEFINED, keyExpr=Component.UNDEFINED, loadPanel=Component.UNDEFINED, masterDetail=Component.UNDEFINED, noDataText=Component.UNDEFINED, onAdaptiveDetailRowPreparing=Component.UNDEFINED, onCellClick=Component.UNDEFINED, onCellHoverChanged=Component.UNDEFINED, onCellPrepared=Component.UNDEFINED, onContentReady=Component.UNDEFINED, onContextMenuPreparing=Component.UNDEFINED, onDataErrorOccurred=Component.UNDEFINED, onDisposing=Component.UNDEFINED, onEditingStart=Component.UNDEFINED, onEditorPrepared=Component.UNDEFINED, onEditorPreparing=Component.UNDEFINED, onExported=Component.UNDEFINED, onExporting=Component.UNDEFINED, onFileSaving=Component.UNDEFINED, onFocusedCellChanged=Component.UNDEFINED, onFocusedCellChanging=Component.UNDEFINED, onFocusedRowChanged=Component.UNDEFINED, onFocusedRowChanging=Component.UNDEFINED, onInitialized=Component.UNDEFINED, onInitNewRow=Component.UNDEFINED, onKeyDown=Component.UNDEFINED, onOptionChanged=Component.UNDEFINED, onRowClick=Component.UNDEFINED, onRowCollapsed=Component.UNDEFINED, onRowCollapsing=Component.UNDEFINED, onRowExpanded=Component.UNDEFINED, onRowExpanding=Component.UNDEFINED, onRowInserted=Component.UNDEFINED, onRowInserting=Component.UNDEFINED, onRowPrepared=Component.UNDEFINED, onRowRemoved=Component.UNDEFINED, onRowRemoving=Component.UNDEFINED, onRowUpdated=Component.UNDEFINED, onRowUpdating=Component.UNDEFINED, onRowValidating=Component.UNDEFINED, onSelectionChanged=Component.UNDEFINED, onToolbarPreparing=Component.UNDEFINED, pager=Component.UNDEFINED, paging=Component.UNDEFINED, remoteOperations=Component.UNDEFINED, renderAsync=Component.UNDEFINED, repaintChangesOnly=Component.UNDEFINED, rowAlternationEnabled=Component.UNDEFINED, rowTemplate=Component.UNDEFINED, rtlEnabled=Component.UNDEFINED, scrolling=Component.UNDEFINED, searchPanel=Component.UNDEFINED, selectedRowKeys=Component.UNDEFINED, selection=Component.UNDEFINED, selectionFilter=Component.UNDEFINED, showBorders=Component.UNDEFINED, showColumnHeaders=Component.UNDEFINED, showColumnLines=Component.UNDEFINED, showRowLines=Component.UNDEFINED, sortByGroupSummaryInfo=Component.UNDEFINED, sorting=Component.UNDEFINED, stateStoring=Component.UNDEFINED, summary=Component.UNDEFINED, tabIndex=Component.UNDEFINED, twoWayBindingEnabled=Component.UNDEFINED, visible=Component.UNDEFINED, width=Component.UNDEFINED, wordWrapEnabled=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'accessKey', 'activeStateEnabled', 'allowColumnReordering', 'allowColumnResizing', 'cacheEnabled', 'cellHintEnabled', 'columnAutoWidth', 'columnChooser', 'columnFixing', 'columnHidingEnabled', 'columnMinWidth', 'columnResizingMode', 'columns', 'columnWidth', 'dataSource', 'dateSerializationFormat', 'disabled', 'editing', 'elementAttr', 'errorRowEnabled', 'export', 'filterBuilder', 'filterBuilderPopup', 'filterPanel', 'filterRow', 'filterSyncEnabled', 'filterValue', 'focusedColumnIndex', 'focusedRowEnabled', 'focusedRowIndex', 'focusedRowKey', 'focusStateEnabled', 'grouping', 'groupPanel', 'headerFilter', 'height', 'highlightChanges', 'hint', 'hoverStateEnabled', 'keyExpr', 'loadPanel', 'masterDetail', 'noDataText', 'onCellClick', 'onRowClick', 'pager', 'paging', 'remoteOperations', 'renderAsync', 'repaintChangesOnly', 'rowAlternationEnabled', 'rowTemplate', 'rtlEnabled', 'scrolling', 'searchPanel', 'selectedRowKeys', 'selection', 'selectionFilter', 'showBorders', 'showColumnHeaders', 'showColumnLines', 'showRowLines', 'sortByGroupSummaryInfo', 'sorting', 'stateStoring', 'summary', 'tabIndex', 'twoWayBindingEnabled', 'visible', 'width', 'wordWrapEnabled']
        self._type = 'DataGrid'
        self._namespace = 'dash_devextreme'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'accessKey', 'activeStateEnabled', 'allowColumnReordering', 'allowColumnResizing', 'cacheEnabled', 'cellHintEnabled', 'columnAutoWidth', 'columnChooser', 'columnFixing', 'columnHidingEnabled', 'columnMinWidth', 'columnResizingMode', 'columns', 'columnWidth', 'dataSource', 'dateSerializationFormat', 'disabled', 'editing', 'elementAttr', 'errorRowEnabled', 'export', 'filterBuilder', 'filterBuilderPopup', 'filterPanel', 'filterRow', 'filterSyncEnabled', 'filterValue', 'focusedColumnIndex', 'focusedRowEnabled', 'focusedRowIndex', 'focusedRowKey', 'focusStateEnabled', 'grouping', 'groupPanel', 'headerFilter', 'height', 'highlightChanges', 'hint', 'hoverStateEnabled', 'keyExpr', 'loadPanel', 'masterDetail', 'noDataText', 'onCellClick', 'onRowClick', 'pager', 'paging', 'remoteOperations', 'renderAsync', 'repaintChangesOnly', 'rowAlternationEnabled', 'rowTemplate', 'rtlEnabled', 'scrolling', 'searchPanel', 'selectedRowKeys', 'selection', 'selectionFilter', 'showBorders', 'showColumnHeaders', 'showColumnLines', 'showRowLines', 'sortByGroupSummaryInfo', 'sorting', 'stateStoring', 'summary', 'tabIndex', 'twoWayBindingEnabled', 'visible', 'width', 'wordWrapEnabled']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DataGrid, self).__init__(**args)

    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
           or any(getattr(self, c, None) is not None
                  for c in self.__dict__.keys()
                  if any(c.startswith(wc_attr)
                  for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                      for wc_attr in
                                      self._valid_wildcard_attributes])])
            return ('DataGrid(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'DataGrid(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
