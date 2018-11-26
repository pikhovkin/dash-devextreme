import React, {Component} from 'react';
import ReactDOM from "react-dom";
import PropTypes from 'prop-types';

import {TabPanel as DXTabPanel} from 'devextreme-react';


export default class TabPanel extends Component {
    constructor(props) {
        super(props);

        this.state = {selectedIndex: this.props.selectedIndex};

        this.itemTitleTemplate = this.itemTitleTemplate.bind(this);
        this.itemTemplate = this.itemTemplate.bind(this);
        this.onOptionChanged = this.onOptionChanged.bind(this);
    }

    itemTitleTemplate(template_id) {
        var tmpl = window[template_id];
        return function(itemData, itemIndex, element) {
            const d = window.document.createElement('div');
            ReactDOM.render(tmpl(itemData), d);
            element.append(d.firstChild);
        }
    }

    itemTemplate(template_id) {
        var tmpl = window[template_id];
        return function(itemData, itemIndex, element) {
            const d = window.document.createElement('div');
            ReactDOM.render(tmpl(itemData), d);
            element.append(d.firstChild);
        }
    }

    onOptionChanged(e) {
        if(e.name === 'selectedIndex') {
            this.setState({selectedIndex: e.value});
        }
    }

    render() {
        let {itemTitleTemplate, itemTemplate} = this.props;

        if (itemTitleTemplate && typeof itemTitleTemplate === 'string'){
            itemTitleTemplate = this.itemTitleTemplate(itemTitleTemplate);
        }

        if (itemTemplate && typeof itemTemplate === 'string'){
            itemTemplate = this.itemTemplate(itemTemplate);
        }

        return (
            <DXTabPanel {...this.props}
                itemTitleTemplate={itemTitleTemplate}
                itemTemplate={itemTemplate}
                selectedIndex={this.state.selectedIndex}
                onOptionChanged ={this.onOptionChanged}
            />
        )
    }
}

TabPanel.propTypes = {
    /**
     * The ID used to identify this compnent in Dash callbacks
     */
    id: PropTypes.string,

    accessKey: PropTypes.string,
    activeStateEnabled: PropTypes.bool,
    animationEnabled: PropTypes.bool,
    dataSource: PropTypes.oneOfType([PropTypes.string, PropTypes.arrayOf(PropTypes.string), PropTypes.arrayOf(PropTypes.object), PropTypes.object]),
    deferRendering: PropTypes.bool,
    disabled: PropTypes.bool,
    elementAttr: PropTypes.object,
    focusStateEnabled: PropTypes.bool,
    height: PropTypes.oneOfType([PropTypes.number, PropTypes.string, PropTypes.func]),
    hint: PropTypes.string,
    hoverStateEnabled: PropTypes.bool,
    itemHoldTimeout: PropTypes.number,
    items: PropTypes.oneOfType([PropTypes.arrayOf(PropTypes.string), PropTypes.arrayOf(PropTypes.object)]),
    itemComponent: PropTypes.func,
    itemTemplate: PropTypes.oneOfType([PropTypes.string, PropTypes.func, PropTypes.object]),
    itemTitleRender: PropTypes.func,
    itemTitleTemplate: PropTypes.oneOfType([PropTypes.string, PropTypes.func, PropTypes.object]),
    loop: PropTypes.bool,
    noDataText: PropTypes.string,
    onContentReady: PropTypes.func,
    onDisposing: PropTypes.func,
    onInitialized: PropTypes.func,
    onItemClick: PropTypes.oneOfType([PropTypes.func, PropTypes.string]),
    onItemContextMenu: PropTypes.func,
    onItemHold: PropTypes.func,
    onItemRendered: PropTypes.func,
    onOptionChanged: PropTypes.func,
    onSelectionChanged: PropTypes.func,
    onTitleClick: PropTypes.oneOfType([PropTypes.func, PropTypes.string]),
    onTitleHold: PropTypes.func,
    onTitleRendered: PropTypes.func,
    repaintChangesOnly: PropTypes.bool,
    rtlEnabled: PropTypes.bool,
    scrollByContent: PropTypes.bool,
    scrollingEnabled: PropTypes.bool,
    selectedIndex: PropTypes.number,
    selectedItem: PropTypes.object,
    showNavButtons: PropTypes.bool,
    swipeEnabled: PropTypes.bool,
    tabIndex: PropTypes.number,
    visible: PropTypes.bool,
    width: PropTypes.oneOfType([PropTypes.number, PropTypes.string, PropTypes.func]),

    setProps: PropTypes.func
};

TabPanel.defaultProps = {
    accessKey: null,
    activeStateEnabled: false,
    animationEnabled: true,
    dataSource: null,
    deferRendering: true,
    disabled: false,
    elementAttr: {},
    focusStateEnabled: false,
    height: 'auto',
    // hint: undefined,
    hoverStateEnabled: true,
    itemHoldTimeout: 750,
    items: undefined,
    itemComponent: null,
    itemTemplate: 'item',
    itemTitleRender: null,
    itemTitleTemplate: 'title',
    loop: false,
    noDataText: 'No data to display',
    onContentReady: null,
    onDisposing: null,
    onInitialized: null,
    onItemClick: null,
    onItemContextMenu: null,
    onItemHold: null,
    onItemRendered: null,
    onOptionChanged: null,
    onSelectionChanged: null,
    onTitleClick: null,
    onTitleHold: null,
    onTitleRendered: null,
    repaintChangesOnly: false,
    rtlEnabled: false,
    scrollByContent: true,
    scrollingEnabled: true,
    selectedIndex: 0,
    selectedItem: null,
    showNavButtons: false,
    swipeEnabled: true,
    tabIndex: 0,
    visible: true,
    width: 'auto'
};
