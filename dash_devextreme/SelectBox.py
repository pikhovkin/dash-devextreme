# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class SelectBox(Component):
    """A SelectBox component.


Keyword arguments:
- id (string; optional)
- acceptCustomValue (boolean; optional)
- accessKey (string; optional)
- activeStateEnabled (boolean; optional)
- dataSource (string | list; optional)
- deferRendering (boolean; optional)
- disabled (boolean; optional)
- displayExpr (string; optional)
- dropDownButtonTemplate (string; optional)
- elementAttr (dict; optional)
- fieldTemplate (string; optional)
- focusStateEnabled (boolean; optional)
- grouped (boolean; optional)
- groupTemplate (string; optional)
- height (number | string; optional)
- hint (string; optional)
- hoverStateEnabled (boolean; optional)
- inputAttr (dict; optional)
- isValid (boolean; optional)
- dxItems (list; optional)
- itemTemplate (string; optional)
- maxLength (string | number; optional)
- minSearchLength (number; optional)
- name (string; optional)
- noDataText (string; optional)
- opened (boolean; optional)
- openOnFieldClick (boolean; optional)
- placeholder (string; optional)
- readOnly (boolean; optional)
- rtlEnabled (boolean; optional)
- searchEnabled (boolean; optional)
- searchExpr (string | list; optional)
- searchMode (a value equal to: 'contains', 'startswith'; optional)
- searchTimeout (number; optional)
- showClearButton (boolean; optional)
- showDataBeforeSearch (boolean; optional)
- showDropDownButton (boolean; optional)
- showSelectionControls (boolean; optional)
- spellcheck (boolean; optional)
- stylingMode (a value equal to: 'outlined', 'underlined', 'filled'; optional)
- tabIndex (number; optional)
- validationError (dict; optional)
- validationMessageMode (a value equal to: 'always', 'auto'; optional)
- value (boolean | number | string | dict | list; optional)
- valueChangeEvent (string; optional)
- valueExpr (string; optional)
- visible (boolean; optional)
- width (number | string; optional)

Available events: 'change'"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, acceptCustomValue=Component.UNDEFINED, accessKey=Component.UNDEFINED, activeStateEnabled=Component.UNDEFINED, dataSource=Component.UNDEFINED, deferRendering=Component.UNDEFINED, disabled=Component.UNDEFINED, displayExpr=Component.UNDEFINED, dropDownButtonTemplate=Component.UNDEFINED, elementAttr=Component.UNDEFINED, fieldTemplate=Component.UNDEFINED, focusStateEnabled=Component.UNDEFINED, grouped=Component.UNDEFINED, groupTemplate=Component.UNDEFINED, height=Component.UNDEFINED, hint=Component.UNDEFINED, hoverStateEnabled=Component.UNDEFINED, inputAttr=Component.UNDEFINED, isValid=Component.UNDEFINED, dxItems=Component.UNDEFINED, itemTemplate=Component.UNDEFINED, maxLength=Component.UNDEFINED, minSearchLength=Component.UNDEFINED, name=Component.UNDEFINED, noDataText=Component.UNDEFINED, onChange=Component.UNDEFINED, onClosed=Component.UNDEFINED, onContentReady=Component.UNDEFINED, onCopy=Component.UNDEFINED, onCustomItemCreating=Component.UNDEFINED, onCut=Component.UNDEFINED, onDisposing=Component.UNDEFINED, onEnterKey=Component.UNDEFINED, onFocusIn=Component.UNDEFINED, onFocusOut=Component.UNDEFINED, onInitialized=Component.UNDEFINED, onInput=Component.UNDEFINED, onItemClick=Component.UNDEFINED, onKeyDown=Component.UNDEFINED, onKeyPress=Component.UNDEFINED, onKeyUp=Component.UNDEFINED, onOpened=Component.UNDEFINED, onOptionChanged=Component.UNDEFINED, onPaste=Component.UNDEFINED, onSelectionChanged=Component.UNDEFINED, onValueChanged=Component.UNDEFINED, opened=Component.UNDEFINED, openOnFieldClick=Component.UNDEFINED, placeholder=Component.UNDEFINED, readOnly=Component.UNDEFINED, rtlEnabled=Component.UNDEFINED, searchEnabled=Component.UNDEFINED, searchExpr=Component.UNDEFINED, searchMode=Component.UNDEFINED, searchTimeout=Component.UNDEFINED, showClearButton=Component.UNDEFINED, showDataBeforeSearch=Component.UNDEFINED, showDropDownButton=Component.UNDEFINED, showSelectionControls=Component.UNDEFINED, spellcheck=Component.UNDEFINED, stylingMode=Component.UNDEFINED, tabIndex=Component.UNDEFINED, validationError=Component.UNDEFINED, validationMessageMode=Component.UNDEFINED, value=Component.UNDEFINED, valueChangeEvent=Component.UNDEFINED, valueExpr=Component.UNDEFINED, visible=Component.UNDEFINED, width=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'acceptCustomValue', 'accessKey', 'activeStateEnabled', 'dataSource', 'deferRendering', 'disabled', 'displayExpr', 'dropDownButtonTemplate', 'elementAttr', 'fieldTemplate', 'focusStateEnabled', 'grouped', 'groupTemplate', 'height', 'hint', 'hoverStateEnabled', 'inputAttr', 'isValid', 'dxItems', 'itemTemplate', 'maxLength', 'minSearchLength', 'name', 'noDataText', 'opened', 'openOnFieldClick', 'placeholder', 'readOnly', 'rtlEnabled', 'searchEnabled', 'searchExpr', 'searchMode', 'searchTimeout', 'showClearButton', 'showDataBeforeSearch', 'showDropDownButton', 'showSelectionControls', 'spellcheck', 'stylingMode', 'tabIndex', 'validationError', 'validationMessageMode', 'value', 'valueChangeEvent', 'valueExpr', 'visible', 'width']
        self._type = 'SelectBox'
        self._namespace = 'dash_devextreme'
        self._valid_wildcard_attributes =            []
        self.available_events = ['change']
        self.available_properties = ['id', 'acceptCustomValue', 'accessKey', 'activeStateEnabled', 'dataSource', 'deferRendering', 'disabled', 'displayExpr', 'dropDownButtonTemplate', 'elementAttr', 'fieldTemplate', 'focusStateEnabled', 'grouped', 'groupTemplate', 'height', 'hint', 'hoverStateEnabled', 'inputAttr', 'isValid', 'dxItems', 'itemTemplate', 'maxLength', 'minSearchLength', 'name', 'noDataText', 'opened', 'openOnFieldClick', 'placeholder', 'readOnly', 'rtlEnabled', 'searchEnabled', 'searchExpr', 'searchMode', 'searchTimeout', 'showClearButton', 'showDataBeforeSearch', 'showDropDownButton', 'showSelectionControls', 'spellcheck', 'stylingMode', 'tabIndex', 'validationError', 'validationMessageMode', 'value', 'valueChangeEvent', 'valueExpr', 'visible', 'width']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(SelectBox, self).__init__(**args)

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
            return ('SelectBox(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'SelectBox(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
