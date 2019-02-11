import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import { hot } from 'react-hot-loader';
import store from './store';
import './App.css';
import Landing from './components/layout/Landing';
import Footer from './components/layout/Footer';
import Login from './components/auth/Login';
import Register from './components/auth/Register';
import UserDashBoard from './dashboard/user/UserDashBoard';
import AdminDashBoard from './dashboard/admin/AdminDashBoard';

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <Router>
          <div className="App">
            <Route exact path="/" component={Landing} />
            <Route exact path="/signin" component={Login} />
            <Route exact path="/signup" component={Register} />
            <Route exact path="/user" component={UserDashBoard} />
            <Route exact path="/admin" component={AdminDashBoard} />
            <Footer />
          </div>
        </Router>
      </Provider>
    );
  }
}
export default hot(module)(App);
