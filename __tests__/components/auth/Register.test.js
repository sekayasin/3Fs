import React from 'react';
import { shallow } from 'enzyme';
import {
  Register,
  mapStateToProps
} from '../../../src/components/auth/Register';

const registerUser = jest.fn();
const props = {
  onChange: jest.fn(),
  onSubmit: jest.fn(),
  registerUser
};
const state = {
  auth: '',
  errors: 'sekabira'
};

describe('test user registration', () => {
  let wrapper;
  beforeEach(() => {
    wrapper = shallow(<Register {...props} />);
  });
  it('matches snapshot', () => {
    expect(wrapper).toMatchSnapshot();
  });
  it('receives props', () => {
    wrapper.setProps({ errors: 'error' });
    expect(wrapper.state('errors')).toEqual('error');
  });
  it('test onChange', () => {
    wrapper
      .instance()
      .onChange({ target: { name: 'password', value: 'hajat❤️' } });
    expect(wrapper.state('password')).toEqual('hajat❤️');
  });
  it('test onSubmit', () => {
    wrapper.instance().onSubmit({ preventDefault: jest.fn() });
    expect(registerUser).toBeCalled();
  });
  it('test mapStateToProps', () => {
    expect(mapStateToProps(state).errors).toEqual('sekabira');
  });
});
