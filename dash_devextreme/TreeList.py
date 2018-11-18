# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class TreeList(Component):
    """A TreeList component.


Keyword arguments:
- id (string; optional)
- dataSource (dict; optional)
- columns (list; optional)
- keyExpr (string; optional)
- parentIdExpr (string; optional)
- showColumnHeaders (boolean; optional)
- showColumnLines (boolean; optional)
- showRowLines (boolean; optional)
- showBorders (boolean; optional)
- columnWidth (number; optional)
- columnMinWidth (number; optional)
- columnAutoWidth (boolean; optional)
- allowColumnResizing (boolean; optional)
- disabled (boolean; optional)
- columnResizingMode (a value equal to: 'nextColumn', 'widget'; optional)
- dataStructure (a value equal to: 'plain', 'tree'; optional)
- scrolling (dict; optional)
- paging (dict; optional)
- pager (dict; optional)
- sorting (dict; optional)
- height (string | number; optional)
- width (string | number; optional)
- visible (boolean; optional)
- wordWrapEnabled (boolean; optional)

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, dataSource=Component.UNDEFINED, columns=Component.UNDEFINED, keyExpr=Component.UNDEFINED, parentIdExpr=Component.UNDEFINED, showColumnHeaders=Component.UNDEFINED, showColumnLines=Component.UNDEFINED, showRowLines=Component.UNDEFINED, showBorders=Component.UNDEFINED, columnWidth=Component.UNDEFINED, columnMinWidth=Component.UNDEFINED, columnAutoWidth=Component.UNDEFINED, allowColumnResizing=Component.UNDEFINED, disabled=Component.UNDEFINED, columnResizingMode=Component.UNDEFINED, dataStructure=Component.UNDEFINED, scrolling=Component.UNDEFINED, paging=Component.UNDEFINED, pager=Component.UNDEFINED, sorting=Component.UNDEFINED, height=Component.UNDEFINED, width=Component.UNDEFINED, visible=Component.UNDEFINED, wordWrapEnabled=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'dataSource', 'columns', 'keyExpr', 'parentIdExpr', 'showColumnHeaders', 'showColumnLines', 'showRowLines', 'showBorders', 'columnWidth', 'columnMinWidth', 'columnAutoWidth', 'allowColumnResizing', 'disabled', 'columnResizingMode', 'dataStructure', 'scrolling', 'paging', 'pager', 'sorting', 'height', 'width', 'visible', 'wordWrapEnabled']
        self._type = 'TreeList'
        self._namespace = 'dash_devextreme'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'dataSource', 'columns', 'keyExpr', 'parentIdExpr', 'showColumnHeaders', 'showColumnLines', 'showRowLines', 'showBorders', 'columnWidth', 'columnMinWidth', 'columnAutoWidth', 'allowColumnResizing', 'disabled', 'columnResizingMode', 'dataStructure', 'scrolling', 'paging', 'pager', 'sorting', 'height', 'width', 'visible', 'wordWrapEnabled']
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
