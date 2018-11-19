# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class TreeList(Component):
    """A TreeList component.


Keyword arguments:
- id (string; optional)
- accessKey (string; optional)
- activeStateEnabled (boolean; optional)
- allowColumnReordering (boolean; optional)
- allowColumnResizing (boolean; optional)
- autoExpandAll (boolean; optional)
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
- dataSource (string | list; optional)
- dataStructure (a value equal to: 'plain', 'tree'; optional)
- dateSerializationFormat (string; optional)
- disabled (boolean; optional)
- editing (dict; optional)
- elementAttr (dict; optional)
- errorRowEnabled (boolean; optional)
- expandedRowKeys (list | list; optional)
- expandNodesOnFiltering (boolean; optional)
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
- hasItemsExpr (string; optional)
- headerFilter (dict; optional)
- height (string | number; optional)
- highlightChanges (boolean; optional)
- hint (string; optional)
- hoverStateEnabled (boolean; optional)
- itemsExpr (string; optional)
- keyExpr (string; optional)
- loadPanel (dict; optional)
- noDataText (string; optional)
- onCellClick (string; optional)
- onRowClick (string; optional)
- pager (dict; optional)
- paging (dict; optional)
- parentIdExpr (string; optional)
- remoteOperations (dict; optional)
- renderAsync (boolean; optional)
- repaintChangesOnly (boolean; optional)
- rootValue (dict; optional)
- rowAlternationEnabled (boolean; optional)
- rtlEnabled (boolean; optional)
- scrolling (dict; optional)
- searchPanel (dict; optional)
- selectedRowKeys (list; optional)
- selection (dict; optional)
- showBorders (boolean; optional)
- showColumnHeaders (boolean; optional)
- showColumnLines (boolean; optional)
- showRowLines (boolean; optional)
- sorting (dict; optional)
- stateStoring (dict; optional)
- tabIndex (number; optional)
- twoWayBindingEnabled (boolean; optional)
- visible (boolean; optional)
- width (string | number; optional)
- wordWrapEnabled (boolean; optional)

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, accessKey=Component.UNDEFINED, activeStateEnabled=Component.UNDEFINED, allowColumnReordering=Component.UNDEFINED, allowColumnResizing=Component.UNDEFINED, autoExpandAll=Component.UNDEFINED, cacheEnabled=Component.UNDEFINED, cellHintEnabled=Component.UNDEFINED, columnAutoWidth=Component.UNDEFINED, columnChooser=Component.UNDEFINED, columnFixing=Component.UNDEFINED, columnHidingEnabled=Component.UNDEFINED, columnMinWidth=Component.UNDEFINED, columnResizingMode=Component.UNDEFINED, columns=Component.UNDEFINED, columnWidth=Component.UNDEFINED, customizeColumns=Component.UNDEFINED, dataSource=Component.UNDEFINED, dataStructure=Component.UNDEFINED, dateSerializationFormat=Component.UNDEFINED, disabled=Component.UNDEFINED, editing=Component.UNDEFINED, elementAttr=Component.UNDEFINED, errorRowEnabled=Component.UNDEFINED, expandedRowKeys=Component.UNDEFINED, expandNodesOnFiltering=Component.UNDEFINED, filterBuilder=Component.UNDEFINED, filterBuilderPopup=Component.UNDEFINED, filterPanel=Component.UNDEFINED, filterRow=Component.UNDEFINED, filterSyncEnabled=Component.UNDEFINED, filterValue=Component.UNDEFINED, focusedColumnIndex=Component.UNDEFINED, focusedRowEnabled=Component.UNDEFINED, focusedRowIndex=Component.UNDEFINED, focusedRowKey=Component.UNDEFINED, focusStateEnabled=Component.UNDEFINED, hasItemsExpr=Component.UNDEFINED, headerFilter=Component.UNDEFINED, height=Component.UNDEFINED, highlightChanges=Component.UNDEFINED, hint=Component.UNDEFINED, hoverStateEnabled=Component.UNDEFINED, itemsExpr=Component.UNDEFINED, keyExpr=Component.UNDEFINED, loadPanel=Component.UNDEFINED, noDataText=Component.UNDEFINED, onAdaptiveDetailRowPreparing=Component.UNDEFINED, onCellClick=Component.UNDEFINED, onCellHoverChanged=Component.UNDEFINED, onCellPrepared=Component.UNDEFINED, onContentReady=Component.UNDEFINED, onContextMenuPreparing=Component.UNDEFINED, onDataErrorOccurred=Component.UNDEFINED, onDisposing=Component.UNDEFINED, onEditingStart=Component.UNDEFINED, onEditorPrepared=Component.UNDEFINED, onEditorPreparing=Component.UNDEFINED, onFocusedCellChanged=Component.UNDEFINED, onFocusedCellChanging=Component.UNDEFINED, onFocusedRowChanged=Component.UNDEFINED, onFocusedRowChanging=Component.UNDEFINED, onInitialized=Component.UNDEFINED, onInitNewRow=Component.UNDEFINED, onKeyDown=Component.UNDEFINED, onNodesInitialized=Component.UNDEFINED, onOptionChanged=Component.UNDEFINED, onRowClick=Component.UNDEFINED, onRowCollapsed=Component.UNDEFINED, onRowCollapsing=Component.UNDEFINED, onRowExpanded=Component.UNDEFINED, onRowExpanding=Component.UNDEFINED, onRowInserted=Component.UNDEFINED, onRowInserting=Component.UNDEFINED, onRowPrepared=Component.UNDEFINED, onRowRemoved=Component.UNDEFINED, onRowRemoving=Component.UNDEFINED, onRowUpdated=Component.UNDEFINED, onRowUpdating=Component.UNDEFINED, onRowValidating=Component.UNDEFINED, onSelectionChanged=Component.UNDEFINED, onToolbarPreparing=Component.UNDEFINED, pager=Component.UNDEFINED, paging=Component.UNDEFINED, parentIdExpr=Component.UNDEFINED, remoteOperations=Component.UNDEFINED, renderAsync=Component.UNDEFINED, repaintChangesOnly=Component.UNDEFINED, rootValue=Component.UNDEFINED, rowAlternationEnabled=Component.UNDEFINED, rtlEnabled=Component.UNDEFINED, scrolling=Component.UNDEFINED, searchPanel=Component.UNDEFINED, selectedRowKeys=Component.UNDEFINED, selection=Component.UNDEFINED, showBorders=Component.UNDEFINED, showColumnHeaders=Component.UNDEFINED, showColumnLines=Component.UNDEFINED, showRowLines=Component.UNDEFINED, sorting=Component.UNDEFINED, stateStoring=Component.UNDEFINED, tabIndex=Component.UNDEFINED, twoWayBindingEnabled=Component.UNDEFINED, visible=Component.UNDEFINED, width=Component.UNDEFINED, wordWrapEnabled=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'accessKey', 'activeStateEnabled', 'allowColumnReordering', 'allowColumnResizing', 'autoExpandAll', 'cacheEnabled', 'cellHintEnabled', 'columnAutoWidth', 'columnChooser', 'columnFixing', 'columnHidingEnabled', 'columnMinWidth', 'columnResizingMode', 'columns', 'columnWidth', 'dataSource', 'dataStructure', 'dateSerializationFormat', 'disabled', 'editing', 'elementAttr', 'errorRowEnabled', 'expandedRowKeys', 'expandNodesOnFiltering', 'filterBuilder', 'filterBuilderPopup', 'filterPanel', 'filterRow', 'filterSyncEnabled', 'filterValue', 'focusedColumnIndex', 'focusedRowEnabled', 'focusedRowIndex', 'focusedRowKey', 'focusStateEnabled', 'hasItemsExpr', 'headerFilter', 'height', 'highlightChanges', 'hint', 'hoverStateEnabled', 'itemsExpr', 'keyExpr', 'loadPanel', 'noDataText', 'onCellClick', 'onRowClick', 'pager', 'paging', 'parentIdExpr', 'remoteOperations', 'renderAsync', 'repaintChangesOnly', 'rootValue', 'rowAlternationEnabled', 'rtlEnabled', 'scrolling', 'searchPanel', 'selectedRowKeys', 'selection', 'showBorders', 'showColumnHeaders', 'showColumnLines', 'showRowLines', 'sorting', 'stateStoring', 'tabIndex', 'twoWayBindingEnabled', 'visible', 'width', 'wordWrapEnabled']
        self._type = 'TreeList'
        self._namespace = 'dash_devextreme'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'accessKey', 'activeStateEnabled', 'allowColumnReordering', 'allowColumnResizing', 'autoExpandAll', 'cacheEnabled', 'cellHintEnabled', 'columnAutoWidth', 'columnChooser', 'columnFixing', 'columnHidingEnabled', 'columnMinWidth', 'columnResizingMode', 'columns', 'columnWidth', 'dataSource', 'dataStructure', 'dateSerializationFormat', 'disabled', 'editing', 'elementAttr', 'errorRowEnabled', 'expandedRowKeys', 'expandNodesOnFiltering', 'filterBuilder', 'filterBuilderPopup', 'filterPanel', 'filterRow', 'filterSyncEnabled', 'filterValue', 'focusedColumnIndex', 'focusedRowEnabled', 'focusedRowIndex', 'focusedRowKey', 'focusStateEnabled', 'hasItemsExpr', 'headerFilter', 'height', 'highlightChanges', 'hint', 'hoverStateEnabled', 'itemsExpr', 'keyExpr', 'loadPanel', 'noDataText', 'onCellClick', 'onRowClick', 'pager', 'paging', 'parentIdExpr', 'remoteOperations', 'renderAsync', 'repaintChangesOnly', 'rootValue', 'rowAlternationEnabled', 'rtlEnabled', 'scrolling', 'searchPanel', 'selectedRowKeys', 'selection', 'showBorders', 'showColumnHeaders', 'showColumnLines', 'showRowLines', 'sorting', 'stateStoring', 'tabIndex', 'twoWayBindingEnabled', 'visible', 'width', 'wordWrapEnabled']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(TreeList, self).__init__(**args)

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
            return ('TreeList(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'TreeList(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
