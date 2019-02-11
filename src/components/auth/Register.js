import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import { registerUser } from '../../actions/authActions';

export class Register extends Component {
  constructor() {
    super();
    this.state = {
      first_name: '',
      last_name: '',
      username: '',
      password: '',
      email: '',
      address: '',
      tel: '',
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

    const newUser = {
      first_name: this.state.first_name,
      last_name: this.state.last_name,
      username: this.state.username,
      password: this.state.password,
      email: this.state.email,
      address: this.state.address,
      tel: this.state.tel
    };
    console.log(newUser);
    // this.props.registerUser(newUser);
    this.props.registerUser(newUser, this.props.history);
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
                    Already have an account? <Link to="/signin">Sign in</Link>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </section>
        <section className="signup-form-section">
          <div className="row">
            <div className="signup-intro">
              <h4>
                Feeling hungry! Sign up
                <br />
                Getting started is easy &amp; Free
              </h4>
              <p>Lucky you, you might win your self free Lunch within 48hrs</p>
            </div>
          </div>
          <div className="row">
            <form
              onSubmit={this.onSubmit}
              className="signup-form"
              id="mySignupForm"
            >
              <div className="form-elements">
                <label htmlFor="first_name">First Name</label>
                <input
                  type="text"
                  name="first_name"
                  value={this.state.first_name}
                  onChange={this.onChange}
                  placeholder="Enter your fist name"
                  required
                />
              </div>

              <div className="form-elements">
                <label htmlFor="last_name">Other name</label>
                <input
                  type="text"
                  name="last_name"
                  value={this.state.last_name}
                  onChange={this.onChange}
                  placeholder="Enter your other name"
                  required
                />
              </div>

              <div className="form-elements">
                <label htmlFor="username" id="usernametaken">
                  Username
                </label>
                <input
                  type="text"
                  name="username"
                  value={this.state.username}
                  onChange={this.onChange}
                  placeholder="Enter your preferred username"
                  required
                />
              </div>

              <div className="form-elements">
                <label htmlFor="password">Password</label>
                <input
                  type="password"
                  id="password"
                  name="password"
                  value={this.state.password}
                  onChange={this.onChange}
                  placeholder="••••••"
                  required
                />
              </div>

              <div className="form-elements">
                <label htmlFor="email" id="emailtaken">
                  Email
                </label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  value={this.state.email}
                  onChange={this.onChange}
                  placeholder="Enter your email address"
                  required
                />
              </div>

              <div className="form-elements">
                <label htmlFor="address">Address</label>
                <input
                  type="text"
                  name="address"
                  value={this.state.address}
                  onChange={this.onChange}
                  placeholder="Enter your residential address"
                  required
                />
              </div>

              <div className="form-elements">
                <label htmlFor="tel">Mobile contact</label>
                <input
                  type="tel"
                  name="tel"
                  value={this.state.tel}
                  onChange={this.onChange}
                  placeholder="Enter your mobile contact"
                  required
                />
              </div>

              <div className="form-elements signup-terms-agreemt">
                <input type="checkbox" name="check_terms" required />
                <label htmlFor="check_terms">
                  Yes, I have read and consent to the{' '}
                  <Link to="#terms">Terms of Use</Link>
                  and <Link to="#agreement">Fast-food-fast Agreement.</Link>
                </label>
              </div>

              <div className="form-elements signup-terms-agreemt">
                <input type="checkbox" name="user_data_pass" required />
                <label htmlFor="user_data_pass">
                  Yes, I have read and consent to the use of my data as
                  described in
                  <Link to="#privacy">fast-food-fast's Privacy Policy</Link>
                </label>
              </div>

              <div className="form-elements signup-terms-agreemt signup-last-para">
                <p>
                  We'd love to send you a few emails on making best use of
                  fast-food-fast, special meals updates, newsletters, or
                  surveys. You can always{' '}
                  <Link to="#unsubscribe">unsubscribe.</Link>
                </p>
                <input type="radio" name="updates" defaultChecked /> Yes,
                please, i'd like to stay in touch
                <br />
                <input type="radio" name="updates" /> No, I don't want to stay
                in touch
              </div>

              <div className="form-elements signup-btn">
                <input type="submit" value="sign Up" />
              </div>
            </form>
            <div className="signup-signin-after-form">
              <p>
                Already have an account? <Link to="/signin">Sign In</Link>
              </p>
            </div>
          </div>
        </section>
      </div>
    );
  }
}
Register.propTypes = {
  registerUser: PropTypes.func.isRequired,
  auth: PropTypes.shape({}),
  errors: PropTypes.shape({})
};

Register.defaultProps = {
  auth: {},
  errors: {}
};

export const mapStateToProps = state => ({
  auth: state.auth,
  errors: state.errors
});
export default connect(
  mapStateToProps,
  { registerUser }
)(withRouter(Register));
