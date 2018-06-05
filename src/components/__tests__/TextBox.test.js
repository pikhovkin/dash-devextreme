import React from 'react';
import {shallow} from 'enzyme';
import TextBox from '../TextBox.react';

describe('TextBox', () => {

    it('renders', () => {
        const component = shallow(<TextBox valueChangeEvent='input' value=''/>);
        expect(component).to.be.ok;
    });
});
