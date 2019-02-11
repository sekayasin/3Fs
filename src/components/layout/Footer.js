import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Footer extends Component {
  render() {
    return (
      <footer>
        <div className="row">
          <div className="clearfix">
            <div className="footer-nav">
              <ul className="footer-nav-links">
                <li>
                  <Link to="#about-footer">About</Link>
                </li>
                <li>
                  <Link to="#blog-footer">Blog</Link>
                </li>
                <li>
                  <Link to="#press-footer">Press</Link>
                </li>
              </ul>
            </div>

            <div className="social-link">
              <ul className="social-links">
                <li>
                  <Link to="https://www.facebook.com/">
                    <i className="ion-social-facebook-outline" />
                  </Link>
                </li>
                <li>
                  <Link to="https://twitter.com/">
                    <i className="ion-social-twitter-outline" />
                  </Link>
                </li>
                <li>
                  <Link to="https://plus.google.com/discover">
                    <i className="ion-social-googleplus-outline" />
                  </Link>
                </li>
                <li>
                  <Link to="https://www.instagram.com/">
                    <i className="ion-social-instagram-outline" />
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div className="row">
          <p>
            Copyright &copy; {new Date().getFullYear()} 3Fs Software, Inc.
            Fast-Food-Fast Company. <br />
            All rights reserved. &nbsp;{' '}
            <Link to="#privacy">Privacy Policy</Link> •{' '}
            <Link to="#terms">Terms of Use</Link>
          </p>
        </div>
      </footer>
    );
  }
}
export default Footer;
