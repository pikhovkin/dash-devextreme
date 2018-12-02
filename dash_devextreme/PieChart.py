# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class PieChart(Component):
    """A PieChart component.


Keyword arguments:
- id (string; optional): The ID used to identify this compnent in Dash callbacks
- adaptiveLayout (dict; optional)
- animation (dict | boolean; optional)
- commonSeriesSettings (dict; optional)
- dataSource (list | dict | string; optional)
- diameter (number; optional)
- disabled (boolean; optional)
- elementAttr (dict; optional)
- export (dict; optional)
- innerRadius (number; optional)
- legend (dict; optional)
- loadingIndicator (dict; optional)
- margin (dict; optional)
- minDiameter (number; optional)
- onLegendClick (string; optional)
- onPointClick (string; optional)
- palette (list | a value equal to: 'Bright', 'Harmony Light', 'Ocean', 'Pastel', 'Soft', 'Soft Pastel', 'Vintage', 'Violet', 'Carmine', 'Dark Moon', 'Dark Violet', 'Green Mist', 'Soft Blue', 'Material', 'Office'; optional)
- paletteExtensionMode (a value equal to: 'alternate', 'blend', 'extrapolate'; optional)
- pathModified (boolean; optional)
- pointSelectionMode (a value equal to: 'multiple', 'single'; optional)
- redrawOnResize (boolean; optional)
- resolveLabelOverlapping (a value equal to: 'hide', 'none', 'shift'; optional)
- rtlEnabled (boolean; optional)
- segmentsDirection (a value equal to: 'anticlockwise', 'clockwise'; optional)
- series (dict | list; optional)
- seriesTemplate (dict; optional)
- size (dict; optional)
- sizeGroup (string; optional)
- startAngle (number; optional)
- theme (a value equal to: 'generic.dark', 'generic.light', 'generic.contrast', 'ios7.default', 'generic.carmine', 'generic.darkmoon', 'generic.darkviolet', 'generic.greenmist', 'generic.softblue', 'material.blue.light', 'material.lime.light', 'material.orange.light', 'material.purple.light', 'material.teal.light'; optional)
- title (dict | string; optional)
- tooltip (dict; optional)
- type (a value equal to: 'donut', 'doughnut', 'pie'; optional)

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, adaptiveLayout=Component.UNDEFINED, animation=Component.UNDEFINED, commonSeriesSettings=Component.UNDEFINED, customizeLabel=Component.UNDEFINED, customizePoint=Component.UNDEFINED, dataSource=Component.UNDEFINED, diameter=Component.UNDEFINED, disabled=Component.UNDEFINED, elementAttr=Component.UNDEFINED, export=Component.UNDEFINED, innerRadius=Component.UNDEFINED, legend=Component.UNDEFINED, loadingIndicator=Component.UNDEFINED, margin=Component.UNDEFINED, minDiameter=Component.UNDEFINED, onDisposing=Component.UNDEFINED, onDone=Component.UNDEFINED, onDrawn=Component.UNDEFINED, onExported=Component.UNDEFINED, onExporting=Component.UNDEFINED, onFileSaving=Component.UNDEFINED, onIncidentOccurred=Component.UNDEFINED, onInitialized=Component.UNDEFINED, onLegendClick=Component.UNDEFINED, onOptionChanged=Component.UNDEFINED, onPointClick=Component.UNDEFINED, onPointHoverChanged=Component.UNDEFINED, onPointSelectionChanged=Component.UNDEFINED, onTooltipHidden=Component.UNDEFINED, onTooltipShown=Component.UNDEFINED, palette=Component.UNDEFINED, paletteExtensionMode=Component.UNDEFINED, pathModified=Component.UNDEFINED, pointSelectionMode=Component.UNDEFINED, redrawOnResize=Component.UNDEFINED, resolveLabelOverlapping=Component.UNDEFINED, rtlEnabled=Component.UNDEFINED, segmentsDirection=Component.UNDEFINED, series=Component.UNDEFINED, seriesTemplate=Component.UNDEFINED, size=Component.UNDEFINED, sizeGroup=Component.UNDEFINED, startAngle=Component.UNDEFINED, theme=Component.UNDEFINED, title=Component.UNDEFINED, tooltip=Component.UNDEFINED, type=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'adaptiveLayout', 'animation', 'commonSeriesSettings', 'dataSource', 'diameter', 'disabled', 'elementAttr', 'export', 'innerRadius', 'legend', 'loadingIndicator', 'margin', 'minDiameter', 'onLegendClick', 'onPointClick', 'palette', 'paletteExtensionMode', 'pathModified', 'pointSelectionMode', 'redrawOnResize', 'resolveLabelOverlapping', 'rtlEnabled', 'segmentsDirection', 'series', 'seriesTemplate', 'size', 'sizeGroup', 'startAngle', 'theme', 'title', 'tooltip', 'type']
        self._type = 'PieChart'
        self._namespace = 'dash_devextreme'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'adaptiveLayout', 'animation', 'commonSeriesSettings', 'dataSource', 'diameter', 'disabled', 'elementAttr', 'export', 'innerRadius', 'legend', 'loadingIndicator', 'margin', 'minDiameter', 'onLegendClick', 'onPointClick', 'palette', 'paletteExtensionMode', 'pathModified', 'pointSelectionMode', 'redrawOnResize', 'resolveLabelOverlapping', 'rtlEnabled', 'segmentsDirection', 'series', 'seriesTemplate', 'size', 'sizeGroup', 'startAngle', 'theme', 'title', 'tooltip', 'type']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(PieChart, self).__init__(**args)

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
            return ('PieChart(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'PieChart(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
