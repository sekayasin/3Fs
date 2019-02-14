import React from 'react';
import { shallow } from 'enzyme';
import AdminDashBoard from '../../src/dashboard/admin/AdminDashBoard';

describe('test admin dashboard', () => {
  let wrapper;
  beforeEach(() => {
    wrapper = shallow(<AdminDashBoard />);
  });
  it('matches snapshot', () => {
    expect(wrapper).toMatchSnapshot();
  });
});
