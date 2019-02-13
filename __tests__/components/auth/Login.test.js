import React from 'react';
import { shallow } from 'enzyme';
import { Login, mapStateToProps } from '../../../src/components/auth/Login';

const loginUser = jest.fn();
const props = {
  onChange: jest.fn(),
  onSubmit: jest.fn(),
  loginUser
};

const state = {
  auth: '',
  errors: 'invalid'
};

describe('test login', () => {
  let wrapper;
  beforeEach(() => {
    wrapper = shallow(<Login {...props} />);
  });
  it('matches snapshot', () => {
    expect(wrapper).toMatchSnapshot();
  });
  it('will receive props', () => {
    wrapper.setProps({ errors: 'invalid username' });
    expect(wrapper.state('errors')).toEqual('invalid username');
  });
  it('test onChange', () => {
    wrapper
      .instance()
      .onChange({ target: { name: 'username', value: 'hajat' } });
    expect(wrapper.state('username')).toEqual('hajat');
  });
  it('test onSubmit', () => {
    wrapper.instance().onSubmit({ preventDefault: jest.fn() });
    expect(loginUser).toBeCalled();
  });
  it('maps state to props', () => {
    expect(mapStateToProps(state).errors).toEqual('invalid');
  });
});
