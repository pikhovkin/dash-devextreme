import React, {Component} from 'react';
import PropTypes from 'prop-types';

import {PieChart as DXPieChart} from 'devextreme-react/pie-chart';


export default class PieChart extends Component {
    constructor(props) {
        super(props);

        this.customizeText = this.customizeText.bind(this);
    }

    customizeText(template_id) {
        return window[template_id];
    }

    render() {
        const {series} = this.props;
        if (series && typeof series === 'object' && series.label && series.label.customizeText) {
            series.label.customizeText = this.customizeText(series.label.customizeText)
        }

        return (
            <DXPieChart
                id={this.props.id}
                type={this.props.type}
                title={this.props.title}
                palette={this.props.palette}
                dataSource={this.props.dataSource}
                series={series}
                legend={this.props.legend}
            />
        )
    }
}

PieChart.propTypes = {
    /**
     * The ID used to identify this compnent in Dash callbacks
     */
    id: PropTypes.string,

    adaptiveLayout: PropTypes.object,
    animation: PropTypes.oneOfType([PropTypes.object, PropTypes.bool]),
    commonSeriesSettings: PropTypes.object,
    customizeLabel: PropTypes.func,
    customizePoint: PropTypes.func,
    dataSource: PropTypes.oneOfType([PropTypes.arrayOf(PropTypes.any), PropTypes.object, PropTypes.string]),
    diameter: PropTypes.number,
    disabled: PropTypes.bool,
    elementAttr: PropTypes.object,
    export: PropTypes.object,
    innerRadius: PropTypes.number,
    legend: PropTypes.object,
    loadingIndicator: PropTypes.object,
    margin: PropTypes.object,
    minDiameter: PropTypes.number,
    onDisposing: PropTypes.func,
    onDone: PropTypes.func,
    onDrawn: PropTypes.func,
    onExported: PropTypes.func,
    onExporting: PropTypes.func,
    onFileSaving: PropTypes.func,
    onIncidentOccurred: PropTypes.func,
    onInitialized: PropTypes.func,
    onLegendClick: PropTypes.oneOfType([PropTypes.func, PropTypes.string]),
    onOptionChanged: PropTypes.func,
    onPointClick: PropTypes.oneOfType([PropTypes.func, PropTypes.string]),
    onPointHoverChanged: PropTypes.func,
    onPointSelectionChanged: PropTypes.func,
    onTooltipHidden: PropTypes.func,
    onTooltipShown: PropTypes.func,
    palette: PropTypes.oneOfType([PropTypes.arrayOf(PropTypes.string), PropTypes.oneOf(['Bright', 'Harmony Light', 'Ocean', 'Pastel', 'Soft', 'Soft Pastel', 'Vintage', 'Violet', 'Carmine', 'Dark Moon', 'Dark Violet', 'Green Mist', 'Soft Blue', 'Material', 'Office'])]),
    paletteExtensionMode: PropTypes.oneOf(['alternate', 'blend', 'extrapolate']),
    pathModified: PropTypes.bool,
    pointSelectionMode: PropTypes.oneOf(['multiple', 'single' ]),
    redrawOnResize: PropTypes.bool,
    resolveLabelOverlapping: PropTypes.oneOf(['hide', 'none', 'shift']),
    rtlEnabled: PropTypes.bool,
    segmentsDirection: PropTypes.oneOf(['anticlockwise', 'clockwise']),
    series: PropTypes.oneOfType([PropTypes.object, PropTypes.arrayOf(PropTypes.object)]),
    seriesTemplate: PropTypes.object,
    size: PropTypes.object,
    sizeGroup: PropTypes.string,
    startAngle: PropTypes.number,
    theme: PropTypes.oneOf(['generic.dark', 'generic.light', 'generic.contrast', 'ios7.default', 'generic.carmine', 'generic.darkmoon', 'generic.darkviolet', 'generic.greenmist', 'generic.softblue', 'material.blue.light', 'material.lime.light', 'material.orange.light', 'material.purple.light', 'material.teal.light']),
    title: PropTypes.oneOfType([PropTypes.object, PropTypes.string]),
    tooltip: PropTypes.object,
    type: PropTypes.oneOf(['donut', 'doughnut', 'pie']),

    setProps: PropTypes.func
};

PieChart.defaultProps = {
    adaptiveLayout: {},
    animation: {},
    commonSeriesSettings: {},
    customizeLabel: null,
    customizePoint: null,
    dataSource: null,
    // diameter: undefined,
    disabled: false,
    elementAttr: {},
    export: {},
    innerRadius: 0.5,
    legend: {},
    loadingIndicator:  {},
    margin: {},
    minDiameter: 0.5,
    onDisposing: null,
    onDone: null,
    onDrawn: null,
    onExported: null,
    onExporting: null,
    onFileSaving: null,
    onIncidentOccurred: null,
    onInitialized: null,
    onLegendClick: null,
    onOptionChanged: null,
    onPointClick: null,
    onPointHoverChanged: null,
    onPointSelectionChanged: null,
    onTooltipHidden: null,
    onTooltipShown: null,
    palette: 'Material',
    paletteExtensionMode: 'blend',
    pathModified: false,
    pointSelectionMode: 'single',
    redrawOnResize: true,
    resolveLabelOverlapping: 'none',
    rtlEnabled: false,
    segmentsDirection: 'clockwise',
    series: [],
    seriesTemplate: {},
    size: {},
    // sizeGroup: undefined,
    startAngle: 0,
    theme: 'generic.light',
    title: {},
    tooltip: {},
    type: 'pie'
};
