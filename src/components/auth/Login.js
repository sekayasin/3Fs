import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import classnames from 'classnames';
import { loginUser } from '../../actions/authActions';

export class Login extends Component {
  constructor() {
    super();
    this.state = {
      username: '',
      password: '',
      errors: {}
    };

    this.onChange = this.onChange.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
  }

  componentWillReceiveProps(nextProps) {
    if (nextProps.errors) {
      this.setState({ errors: nextProps.errors });
    }
  }

  onChange(e) {
    this.setState({ [e.target.name]: e.target.value });
  }

  onSubmit(e) {
    e.preventDefault();

    const user = {
      username: this.state.username,
      password: this.state.password
    };

    this.props.loginUser(user, this.props.history);
  }

  render() {
    const { errors } = this.state;

    return (
      <div>
        <section className="signin-header">
          <div className="row">
            <div className="clearfix">
              <Link to="/">
                <div className="signin-title">
                  <div className="imagebox">
                    <div className="imgShow">
                      <img
                        src={require('../../img/3FsLogo_black.png')}
                        alt="fast-food-fast logo dark"
                      />
                    </div>
                    <div className="imgHover">
                      <img
                        src={require('../../img/3FsLogo_color.png')}
                        alt="fast-food-fast logo color"
                      />
                    </div>
                  </div>
                </div>
              </Link>
              <div className="signin-signup">
                <ul className="top-navbar">
                  <li>
                    <Link to="#about-us">About us</Link>
                  </li>
                  <li>
                    <Link to="#food-delivery">Food Delivery</Link>
                  </li>
                  <li>
                    <Link to="#our-cities">Our cities</Link>
                  </li>
                  <li>
                    <Link to="#testimonials">Testimonials</Link>
                  </li>
                  <li>
                    <Link to="#blog">Blog</Link>
                  </li>
                  <li>
                    Don't have an account? <Link to="/signup">Sign up</Link>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </section>
        <section className="signin-form-section">
          <div className="row">
            <form
              onSubmit={this.onSubmit}
              className="signin-form"
              id="mySiginForm"
            >
              <div className="signin-form-title">
                <p>Sign In</p>
              </div>

              <div className="signin-form-subtitle">
                <p>Sign in to continue to Fast-Food-Fast</p>
              </div>

              <div className="form-elements">
                <label htmlFor="username" id="usernameerror">
                  Sign in as{' '}
                </label>
                <input
                  type="text"
                  name="username"
                  value={this.state.username}
                  onChange={this.onChange}
                  id="username"
                  placeholder="Enter your Username"
                  className={classnames({
                    'is-invalid': errors.msg
                  })}
                />
                {}
                {errors.msg && (
                  <div className="invalid-feedback">{errors.msg}</div>
                )}
              </div>

              <div className="form-elements">
                <label htmlFor="password" id="userpasserror">
                  Password{' '}
                </label>
                <input
                  type="password"
                  name="password"
                  value={this.state.password}
                  onChange={this.onChange}
                />
              </div>

              <div className="form-elements">
                <input type="submit" value="sign in" />
              </div>

              <div className="forgot-pass">
                <p>
                  <Link to="#forgot-password">Forgot password?</Link>
                </p>
              </div>
            </form>
            <div className="signin-signup-after-form">
              <p>
                Feeling hungry! Don't have an account yet?{' '}
                <Link to="/signup">Sign up here</Link>
              </p>
            </div>
          </div>
        </section>
        <section className="download-3fs-phone-app">
          <div className="row">
            <div className="fff-phone-app">
              <h4>
                Never feel hungry again! <br /> take Fast-food-fast with you!
              </h4>
              <p>Stay up-to-date on your iPhone, iPad, and Android devices.</p>
            </div>
          </div>

          <div className="row">
            <div className="fff-phone-app pos-badges">
              <div className="phone-app">
                <img
                  src={require('../../img/3fs-app-half.png')}
                  alt="3fs phone app"
                />
              </div>
              <div className="get-app-badges">
                <Link to="#download-playstore">
                  <img
                    src={require('../../img/mobile-googleplay.png')}
                    alt="download android app"
                  />
                </Link>
                <Link to="#download-applestore">
                  <img
                    src={require('../../img/mobile-applestore.png')}
                    alt="download iphone app"
                  />
                </Link>
              </div>
            </div>
          </div>
        </section>
      </div>
    );
  }
}
Login.propTypes = {
  loginUser: PropTypes.func.isRequired,
  auth: PropTypes.shape({}),
  errors: PropTypes.shape({})
};

Login.defaultProps = {
  auth: {},
  errors: {}
};

export const mapStateToProps = state => {
  return {
    auth: state.auth,
    errors: state.errors
  };
};
export default connect(
  mapStateToProps,
  { loginUser }
)(withRouter(Login));
