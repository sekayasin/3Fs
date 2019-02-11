import notify from 'msg-notify';
import GET_ERRORS from './types';
import 'msg-notify/dist/notify.css';

// Register User

export const registerUser = (userData, history) => dispatch => {
  const urlSignup = 'https://sekayasin-3fs-apiv2.herokuapp.com/auth/signup';
  return fetch(urlSignup, {
    method: 'post',
    headers: { 'Content-type': 'application/json; charset-utf-8' },
    CORS: 'no-cors',
    body: JSON.stringify(userData)
  })
    .then(response => response.json())
    .then(jsonData => {
      if (jsonData.message === 'Username Available, Try Again') {
        notify('Username Available, Try Again', 'error');
      }
      if (jsonData.message === 'Email Available, Try Again') {
        notify('Email Available, Try Again', 'error');
      }
      if (jsonData.message === 'Success') {
        notify('Account created successful', 'success');
        history.push('/signin');
      }
    })
    .catch(error => {
      dispatch({
        type: GET_ERRORS,
        payload: error
      });
    });
};

// Login user

export const loginUser = (userData, history) => dispatch => {
  const urlSignin = 'https://sekayasin-3fs-apiv2.herokuapp.com/auth/login';
  return fetch(urlSignin, {
    method: 'post',
    headers: { 'Content-type': 'application/json; charset-utf-8' },
    CORS: 'no-cors',
    body: JSON.stringify(userData)
  })
    .then(response => response.json())
    .then(jsonData => {
      //   console.log(jsonData);
      if (jsonData.msg === 'Invalid Username') {
        notify('username not found', 'error');
      }
      if (jsonData.msg === 'Invalid Password') {
        notify('invalid password', 'error');
      }
      if (jsonData.access_token) {
        if (jsonData.role_id === 2) {
          notify('welcome', 'success');
          history.push('/user');
        }
        if (jsonData.role_id === 1) {
          notify('welcome', 'success');
          history.push('/admin');
        }
      }
    })
    .catch(error => {
      dispatch({
        type: GET_ERRORS,
        playload: error
      });
    });
};
