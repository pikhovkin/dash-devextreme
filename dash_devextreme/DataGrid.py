# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DataGrid(Component):
    """A DataGrid component.


Keyword arguments:
- id (string; optional)
- dataSource (dict; optional)
- columns (list; optional)
- columnAutoWidth (boolean; optional)
- grouping (dict; optional)

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, dataSource=Component.UNDEFINED, columns=Component.UNDEFINED, columnAutoWidth=Component.UNDEFINED, grouping=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'dataSource', 'columns', 'columnAutoWidth', 'grouping']
        self._type = 'DataGrid'
        self._namespace = 'dash_devextreme'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'dataSource', 'columns', 'columnAutoWidth', 'grouping']
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
