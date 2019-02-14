import React from 'react';
import { shallow } from 'enzyme';
import UserDashBoard from '../../src/dashboard/user/UserDashBoard';

describe('test user dashboard', () => {
  let wrapper;
  beforeEach(() => {
    wrapper = shallow(<UserDashBoard />);
  });
  it('matches snapshot', () => {
    expect(wrapper).toMatchSnapshot();
  });
});
