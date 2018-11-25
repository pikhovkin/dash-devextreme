# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Popup(Component):
    """A Popup component.


Keyword arguments:
- id (string; optional): The ID used to identify this compnent in Dash callbacks
- showTitle (boolean; optional)
- title (string; optional)
- visible (boolean; optional)
- dragEnabled (boolean; optional)
- closeOnOutsideClick (boolean; optional)
- closeOnBackButton (boolean; optional)

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, showTitle=Component.UNDEFINED, title=Component.UNDEFINED, visible=Component.UNDEFINED, dragEnabled=Component.UNDEFINED, closeOnOutsideClick=Component.UNDEFINED, closeOnBackButton=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'showTitle', 'title', 'visible', 'dragEnabled', 'closeOnOutsideClick', 'closeOnBackButton']
        self._type = 'Popup'
        self._namespace = 'dash_devextreme'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'showTitle', 'title', 'visible', 'dragEnabled', 'closeOnOutsideClick', 'closeOnBackButton']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Popup, self).__init__(**args)

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
            return ('Popup(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Popup(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
