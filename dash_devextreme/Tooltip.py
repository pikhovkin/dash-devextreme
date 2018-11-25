# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Tooltip(Component):
    """A Tooltip component.


Keyword arguments:
- id (string; optional): The ID used to identify this compnent in Dash callbacks
- animation (dict; optional)
- closeOnBackButton (boolean; optional)
- closeOnOutsideClick (boolean; optional)
- container (string; optional)
- deferRendering (boolean; optional)
- disabled (boolean; optional)
- elementAttr (dict; optional)
- height (number | string; optional)
- hideEvent (dict | string; optional)
- hint (string; optional)
- hoverStateEnabled (boolean; optional)
- maxHeight (number | string; optional)
- maxWidth (number | string; optional)
- minHeight (number | string; optional)
- minWidth (number | string; optional)
- position (a value equal to: 'bottom', 'left', 'right', 'top' | dict; optional)
- rtlEnabled (boolean; optional)
- shading (boolean; optional)
- shadingColor (string; optional)
- showEvent (dict | string; optional)
- target (string; optional)
- visible (boolean; optional)
- width (number | string; optional)

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, animation=Component.UNDEFINED, closeOnBackButton=Component.UNDEFINED, closeOnOutsideClick=Component.UNDEFINED, container=Component.UNDEFINED, deferRendering=Component.UNDEFINED, disabled=Component.UNDEFINED, elementAttr=Component.UNDEFINED, height=Component.UNDEFINED, hideEvent=Component.UNDEFINED, hint=Component.UNDEFINED, hoverStateEnabled=Component.UNDEFINED, maxHeight=Component.UNDEFINED, maxWidth=Component.UNDEFINED, minHeight=Component.UNDEFINED, minWidth=Component.UNDEFINED, onContentReady=Component.UNDEFINED, onDisposing=Component.UNDEFINED, onHidden=Component.UNDEFINED, onHiding=Component.UNDEFINED, onInitialized=Component.UNDEFINED, onOptionChanged=Component.UNDEFINED, onShowing=Component.UNDEFINED, onShown=Component.UNDEFINED, position=Component.UNDEFINED, rtlEnabled=Component.UNDEFINED, shading=Component.UNDEFINED, shadingColor=Component.UNDEFINED, showEvent=Component.UNDEFINED, target=Component.UNDEFINED, visible=Component.UNDEFINED, width=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animation', 'closeOnBackButton', 'closeOnOutsideClick', 'container', 'deferRendering', 'disabled', 'elementAttr', 'height', 'hideEvent', 'hint', 'hoverStateEnabled', 'maxHeight', 'maxWidth', 'minHeight', 'minWidth', 'position', 'rtlEnabled', 'shading', 'shadingColor', 'showEvent', 'target', 'visible', 'width']
        self._type = 'Tooltip'
        self._namespace = 'dash_devextreme'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'animation', 'closeOnBackButton', 'closeOnOutsideClick', 'container', 'deferRendering', 'disabled', 'elementAttr', 'height', 'hideEvent', 'hint', 'hoverStateEnabled', 'maxHeight', 'maxWidth', 'minHeight', 'minWidth', 'position', 'rtlEnabled', 'shading', 'shadingColor', 'showEvent', 'target', 'visible', 'width']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Tooltip, self).__init__(**args)

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
            return ('Tooltip(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Tooltip(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
