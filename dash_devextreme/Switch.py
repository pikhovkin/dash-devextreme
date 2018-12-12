# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Switch(Component):
    """A Switch component.


Keyword arguments:
- id (string; optional): The ID used to identify this compnent in Dash callbacks
- accessKey (string; optional)
- activeStateEnabled (boolean; optional)
- disabled (boolean; optional)
- elementAttr (dict; optional)
- focusStateEnabled (boolean; optional)
- height (number | string; optional)
- hint (string; optional)
- hoverStateEnabled (boolean; optional)
- isValid (boolean; optional)
- name (string; optional)
- readOnly (boolean; optional)
- rtlEnabled (boolean; optional)
- switchedOffText (string; optional)
- switchedOnText (string; optional)
- tabIndex (number; optional)
- validationError (dict; optional)
- validationMessageMode (a value equal to: 'always', 'auto'; optional)
- value (boolean; optional)
- visible (boolean; optional)
- width (number | string; optional)

Available events: 'change'"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, accessKey=Component.UNDEFINED, activeStateEnabled=Component.UNDEFINED, disabled=Component.UNDEFINED, elementAttr=Component.UNDEFINED, focusStateEnabled=Component.UNDEFINED, height=Component.UNDEFINED, hint=Component.UNDEFINED, hoverStateEnabled=Component.UNDEFINED, isValid=Component.UNDEFINED, name=Component.UNDEFINED, onContentReady=Component.UNDEFINED, onDisposing=Component.UNDEFINED, onInitialized=Component.UNDEFINED, onOptionChanged=Component.UNDEFINED, onValueChanged=Component.UNDEFINED, readOnly=Component.UNDEFINED, rtlEnabled=Component.UNDEFINED, switchedOffText=Component.UNDEFINED, switchedOnText=Component.UNDEFINED, tabIndex=Component.UNDEFINED, validationError=Component.UNDEFINED, validationMessageMode=Component.UNDEFINED, value=Component.UNDEFINED, visible=Component.UNDEFINED, width=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'accessKey', 'activeStateEnabled', 'disabled', 'elementAttr', 'focusStateEnabled', 'height', 'hint', 'hoverStateEnabled', 'isValid', 'name', 'readOnly', 'rtlEnabled', 'switchedOffText', 'switchedOnText', 'tabIndex', 'validationError', 'validationMessageMode', 'value', 'visible', 'width']
        self._type = 'Switch'
        self._namespace = 'dash_devextreme'
        self._valid_wildcard_attributes =            []
        self.available_events = ['change']
        self.available_properties = ['id', 'accessKey', 'activeStateEnabled', 'disabled', 'elementAttr', 'focusStateEnabled', 'height', 'hint', 'hoverStateEnabled', 'isValid', 'name', 'readOnly', 'rtlEnabled', 'switchedOffText', 'switchedOnText', 'tabIndex', 'validationError', 'validationMessageMode', 'value', 'visible', 'width']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Switch, self).__init__(**args)

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
            return ('Switch(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Switch(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
