# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class TextBox(Component):
    """A TextBox component.


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
- inputAttr (dict; optional)
- isValid (boolean; optional)
- mask (string; optional)
- maskChar (string; optional)
- maskInvalidMessage (string; optional)
- maskRules (dict; optional)
- maxLength (string | number; optional)
- mode (a value equal to: 'email', 'password', 'search', 'tel', 'text', 'url'; optional)
- name (string; optional)
- placeholder (string; optional)
- readOnly (boolean; optional)
- rtlEnabled (boolean; optional)
- showClearButton (boolean; optional)
- showMaskMode (a value equal to: 'always', 'onFocus'; optional)
- spellcheck (boolean; optional)
- stylingMode (a value equal to: 'outlined', 'underlined', 'filled'; optional)
- tabIndex (number; optional)
- useMaskedValue (boolean; optional)
- validationError (dict; optional)
- validationMessageMode (a value equal to: 'always', 'auto'; optional)
- value (string; optional)
- valueChangeEvent (string; optional)
- visible (boolean; optional)
- width (number | string; optional)

Available events: 'change'"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, accessKey=Component.UNDEFINED, activeStateEnabled=Component.UNDEFINED, disabled=Component.UNDEFINED, elementAttr=Component.UNDEFINED, focusStateEnabled=Component.UNDEFINED, height=Component.UNDEFINED, hint=Component.UNDEFINED, hoverStateEnabled=Component.UNDEFINED, inputAttr=Component.UNDEFINED, isValid=Component.UNDEFINED, mask=Component.UNDEFINED, maskChar=Component.UNDEFINED, maskInvalidMessage=Component.UNDEFINED, maskRules=Component.UNDEFINED, maxLength=Component.UNDEFINED, mode=Component.UNDEFINED, name=Component.UNDEFINED, onChange=Component.UNDEFINED, onContentReady=Component.UNDEFINED, onCopy=Component.UNDEFINED, onCut=Component.UNDEFINED, onDisposing=Component.UNDEFINED, onEnterKey=Component.UNDEFINED, onFocusIn=Component.UNDEFINED, onFocusOut=Component.UNDEFINED, onInitialized=Component.UNDEFINED, onInput=Component.UNDEFINED, onKeyDown=Component.UNDEFINED, onKeyPress=Component.UNDEFINED, onKeyUp=Component.UNDEFINED, onOptionChanged=Component.UNDEFINED, onPaste=Component.UNDEFINED, onValueChanged=Component.UNDEFINED, placeholder=Component.UNDEFINED, readOnly=Component.UNDEFINED, rtlEnabled=Component.UNDEFINED, showClearButton=Component.UNDEFINED, showMaskMode=Component.UNDEFINED, spellcheck=Component.UNDEFINED, stylingMode=Component.UNDEFINED, tabIndex=Component.UNDEFINED, useMaskedValue=Component.UNDEFINED, validationError=Component.UNDEFINED, validationMessageMode=Component.UNDEFINED, value=Component.UNDEFINED, valueChangeEvent=Component.UNDEFINED, visible=Component.UNDEFINED, width=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'accessKey', 'activeStateEnabled', 'disabled', 'elementAttr', 'focusStateEnabled', 'height', 'hint', 'hoverStateEnabled', 'inputAttr', 'isValid', 'mask', 'maskChar', 'maskInvalidMessage', 'maskRules', 'maxLength', 'mode', 'name', 'placeholder', 'readOnly', 'rtlEnabled', 'showClearButton', 'showMaskMode', 'spellcheck', 'stylingMode', 'tabIndex', 'useMaskedValue', 'validationError', 'validationMessageMode', 'value', 'valueChangeEvent', 'visible', 'width']
        self._type = 'TextBox'
        self._namespace = 'dash_devextreme'
        self._valid_wildcard_attributes =            []
        self.available_events = ['change']
        self.available_properties = ['id', 'accessKey', 'activeStateEnabled', 'disabled', 'elementAttr', 'focusStateEnabled', 'height', 'hint', 'hoverStateEnabled', 'inputAttr', 'isValid', 'mask', 'maskChar', 'maskInvalidMessage', 'maskRules', 'maxLength', 'mode', 'name', 'placeholder', 'readOnly', 'rtlEnabled', 'showClearButton', 'showMaskMode', 'spellcheck', 'stylingMode', 'tabIndex', 'useMaskedValue', 'validationError', 'validationMessageMode', 'value', 'valueChangeEvent', 'visible', 'width']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(TextBox, self).__init__(**args)

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
            return ('TextBox(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'TextBox(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
