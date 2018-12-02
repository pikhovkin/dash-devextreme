import React, {Component} from 'react';
import ReactDOM from "react-dom";
import PropTypes from 'prop-types';

import {Tabs as DXTabs} from 'devextreme-react';


export default class Tabs extends Component {
    constructor(props) {
        super(props);

        this.state = {selectedIndex: this.props.selectedIndex};

        this.itemTemplate = this.itemTemplate.bind(this);
        this.onOptionChanged = this.onOptionChanged.bind(this);
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
        let {itemTemplate} = this.props;

        if (itemTemplate && typeof itemTemplate === 'string'){
            itemTemplate = this.itemTemplate(itemTemplate);
        }

        return (
            <DXTabs {...this.props}
                itemTemplate={itemTemplate}
                selectedIndex={this.state.selectedIndex}
                onOptionChanged ={this.onOptionChanged}
            />
        )
    }
}

Tabs.propTypes = {
    /**
     * The ID used to identify this compnent in Dash callbacks
     */
    id: PropTypes.string,

    accessKey: PropTypes.string,
    dataSource: PropTypes.oneOfType([PropTypes.string, PropTypes.arrayOf(PropTypes.string), PropTypes.arrayOf(PropTypes.object), PropTypes.object]),
    disabled: PropTypes.bool,
    elementAttr: PropTypes.object,
    focusStateEnabled: PropTypes.bool,
    height: PropTypes.oneOfType([PropTypes.number, PropTypes.string, PropTypes.func]),
    hint: PropTypes.string,
    hoverStateEnabled: PropTypes.bool,
    itemHoldTimeout: PropTypes.number,
    items: PropTypes.oneOfType([PropTypes.arrayOf(PropTypes.string), PropTypes.arrayOf(PropTypes.object)]),
    itemTemplate: PropTypes.oneOfType([PropTypes.string, PropTypes.func, PropTypes.object]),
    keyExpr: PropTypes.oneOfType([PropTypes.string, PropTypes.func]),
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
    repaintChangesOnly: PropTypes.bool,
    rtlEnabled: PropTypes.bool,
    scrollByContent: PropTypes.bool,
    scrollingEnabled: PropTypes.bool,
    selectedIndex: PropTypes.number,
    selectedItem: PropTypes.object,
    selectedItemKeys: PropTypes.number,
    selectedItems: PropTypes.arrayOf(PropTypes.any),
    selectionMode: PropTypes.oneOf(['multiple', 'single']),
    showNavButtons: PropTypes.bool,
    tabIndex: PropTypes.number,
    visible: PropTypes.bool,
    width: PropTypes.oneOfType([PropTypes.number, PropTypes.string, PropTypes.func]),

    setProps: PropTypes.func
};

Tabs.defaultProps = {
    accessKey: null,
    dataSource: null,
    disabled: false,
    elementAttr: {},
    focusStateEnabled: true,
    height: 'auto',
    // hint: undefined,
    hoverStateEnabled: true,
    itemHoldTimeout: 750,
    items: null,
    itemTemplate: 'item',
    keyExpr: null,
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
    repaintChangesOnly: false,
    rtlEnabled: false,
    scrollByContent: false,
    scrollingEnabled: true,
    selectedIndex: -1,
    selectedItem: null,
    selectedItemKeys: null,
    selectedItems: null,
    selectionMode: 'single',
    showNavButtons: true,
    tabIndex: 0,
    visible: true,
    width: 'auto'
};
