import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';
import fetchMock from 'fetch-mock';
import actionTypes from '../../src/actions/types';
import { registerUser, loginUser } from '../../src/actions/authActions';

const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);
const userToSignin = {
  username: 'sekayasin',
  password: 'sekayasin'
};
const userToRegister = {
  username: 'sekayasin',
  password: 'sekayasin',
  tel: 'sekayasin',
  address: 'sekayasin',
  last_name: 'sekayasin',
  first_name: 'sekayasin',
  email: 'sekayasin'
};

describe('unit tests authActions', () => {
  afterEach(() => {
    fetchMock.restore();
  });
  it('should mock auth actions', () => {
    const store = mockStore();
    fetchMock.postOnce('https://sekayasin-3fs-apiv2.herokuapp.com/auth/login', {
      headers: {
        'content-type': 'application/json'
      },
      body: userToSignin
    });
    store.dispatch(loginUser(userToSignin));
    expect(store.getActions()).toEqual([]);
  });

  it('should mock auth actions', () => {
    const store = mockStore();
    fetchMock.postOnce(
      'https://sekayasin-3fs-apiv2.herokuapp.com/auth/signup',
      {
        headers: {
          'content-type': 'application/json'
        },
        body: userToRegister
      }
    );
    store.dispatch(registerUser(userToRegister));
    expect(store.getActions()).toEqual([]);
  });
});
