# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class TabPanel(Component):
    """A TabPanel component.


Keyword arguments:
- id (string; optional): The ID used to identify this compnent in Dash callbacks
- accessKey (string; optional)
- activeStateEnabled (boolean; optional)
- animationEnabled (boolean; optional)
- dataSource (string | list | list | dict; optional)
- deferRendering (boolean; optional)
- disabled (boolean; optional)
- elementAttr (dict; optional)
- focusStateEnabled (boolean; optional)
- height (number | string; optional)
- hint (string; optional)
- hoverStateEnabled (boolean; optional)
- itemHoldTimeout (number; optional)
- items (list | list; optional)
- itemTemplate (string | dict; optional)
- itemTitleTemplate (string | dict; optional)
- loop (boolean; optional)
- noDataText (string; optional)
- onItemClick (string; optional)
- onTitleClick (string; optional)
- repaintChangesOnly (boolean; optional)
- rtlEnabled (boolean; optional)
- scrollByContent (boolean; optional)
- scrollingEnabled (boolean; optional)
- selectedIndex (number; optional)
- selectedItem (dict; optional)
- showNavButtons (boolean; optional)
- swipeEnabled (boolean; optional)
- tabIndex (number; optional)
- visible (boolean; optional)
- width (number | string; optional)

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, accessKey=Component.UNDEFINED, activeStateEnabled=Component.UNDEFINED, animationEnabled=Component.UNDEFINED, dataSource=Component.UNDEFINED, deferRendering=Component.UNDEFINED, disabled=Component.UNDEFINED, elementAttr=Component.UNDEFINED, focusStateEnabled=Component.UNDEFINED, height=Component.UNDEFINED, hint=Component.UNDEFINED, hoverStateEnabled=Component.UNDEFINED, itemHoldTimeout=Component.UNDEFINED, items=Component.UNDEFINED, itemComponent=Component.UNDEFINED, itemTemplate=Component.UNDEFINED, itemTitleRender=Component.UNDEFINED, itemTitleTemplate=Component.UNDEFINED, loop=Component.UNDEFINED, noDataText=Component.UNDEFINED, onContentReady=Component.UNDEFINED, onDisposing=Component.UNDEFINED, onInitialized=Component.UNDEFINED, onItemClick=Component.UNDEFINED, onItemContextMenu=Component.UNDEFINED, onItemHold=Component.UNDEFINED, onItemRendered=Component.UNDEFINED, onOptionChanged=Component.UNDEFINED, onSelectionChanged=Component.UNDEFINED, onTitleClick=Component.UNDEFINED, onTitleHold=Component.UNDEFINED, onTitleRendered=Component.UNDEFINED, repaintChangesOnly=Component.UNDEFINED, rtlEnabled=Component.UNDEFINED, scrollByContent=Component.UNDEFINED, scrollingEnabled=Component.UNDEFINED, selectedIndex=Component.UNDEFINED, selectedItem=Component.UNDEFINED, showNavButtons=Component.UNDEFINED, swipeEnabled=Component.UNDEFINED, tabIndex=Component.UNDEFINED, visible=Component.UNDEFINED, width=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'accessKey', 'activeStateEnabled', 'animationEnabled', 'dataSource', 'deferRendering', 'disabled', 'elementAttr', 'focusStateEnabled', 'height', 'hint', 'hoverStateEnabled', 'itemHoldTimeout', 'items', 'itemTemplate', 'itemTitleTemplate', 'loop', 'noDataText', 'onItemClick', 'onTitleClick', 'repaintChangesOnly', 'rtlEnabled', 'scrollByContent', 'scrollingEnabled', 'selectedIndex', 'selectedItem', 'showNavButtons', 'swipeEnabled', 'tabIndex', 'visible', 'width']
        self._type = 'TabPanel'
        self._namespace = 'dash_devextreme'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'accessKey', 'activeStateEnabled', 'animationEnabled', 'dataSource', 'deferRendering', 'disabled', 'elementAttr', 'focusStateEnabled', 'height', 'hint', 'hoverStateEnabled', 'itemHoldTimeout', 'items', 'itemTemplate', 'itemTitleTemplate', 'loop', 'noDataText', 'onItemClick', 'onTitleClick', 'repaintChangesOnly', 'rtlEnabled', 'scrollByContent', 'scrollingEnabled', 'selectedIndex', 'selectedItem', 'showNavButtons', 'swipeEnabled', 'tabIndex', 'visible', 'width']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(TabPanel, self).__init__(**args)

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
            return ('TabPanel(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'TabPanel(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
