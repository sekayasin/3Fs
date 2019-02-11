import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Landing extends Component {
  render() {
    return (
      <div>
        <header>
          <nav>
            <div className="row">
              <div className="clearfix">
                <img
                  src={require('../../img/3FsLogo_White.png')}
                  alt="fast-food-fast logo"
                  className="logo"
                />
                <ul className="main-nav">
                  <li>
                    <Link to="#aboutus" id="about">
                      About us
                    </Link>
                  </li>
                  <li>
                    <Link to="#delivery" id="deliver">
                      Food Delivery
                    </Link>
                  </li>
                  <li>
                    <Link to="#ourcities">Our cities</Link>
                  </li>
                  <li>
                    <Link to="#testimonials">Testimonials</Link>
                  </li>
                  <li>
                    <Link to="#blog">Blog</Link>
                  </li>
                  <li>
                    <Link to="/signup">Sign up</Link>
                  </li>
                </ul>
              </div>
            </div>
          </nav>
          <div className="hero-text">
            <h1>
              We cook just like yo mother!
              <span>
                <br />
                super healthy &amp; delicious food
                <br />
                delivered right to yo door 24/7 365!
              </span>
            </h1>
            <Link to="#hungry-signup" className="btn btn-full" id="hungry">
              I'm hungry
            </Link>
            <Link to="#meals" className="btn btn-light" id="show-me">
              show me more..
            </Link>
          </div>

          <div className="signin">
            <p>
              Already have an account? <Link to="/signin">Sign in</Link>
            </p>
          </div>
        </header>
        <section className="section-features-about-us" id="aboutus">
          <div className="row">
            <h2>Good Food &mdash; Good Mood</h2>
            <p className="hero-intro">
              Hello, We're Fast-Food-Fast{' '}
              <strike>
                <em>!Not Fast Food aka junk!</em>
              </strike>
              call us 3Fs, yo new premium door to door food delivery service.{' '}
              <br />
              No time for cooking! No worries, let us take care of that, we're
              really good at it! we promise!
            </p>
          </div>

          <div className="row">
            <div className="col">
              <div className="col-flex col-box">
                <i className="ion-ios-loop-strong i-center" />
                <h3>24/7 365 days committed</h3>
                <p>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Eum
                  dolore nulla tempora praesentium fugit impedit expedita soluta
                  possimus culpa sint.
                </p>
              </div>

              <div className="col-flex col-box">
                <i className="ion-ios-stopwatch-outline i-center" />
                <h3>Ready in 30 Mintues</h3>
                <p>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Eum
                  dolore nulla tempora praesentium fugit impedit expedita soluta
                  possimus culpa sint.
                </p>
              </div>

              <div className="col-flex col-box">
                <i className="ion-ios-nutrition-outline i-center" />
                <h3>Super healthy meals</h3>
                <p>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Eum
                  dolore nulla tempora praesentium fugit impedit expedita soluta
                  possimus culpa sint.
                </p>
              </div>
            </div>
          </div>
        </section>
        <div className="section-meals" id="meals">
          <ul className="meals-showcase clearfix">
            <li>
              <figure className="meal-sample">
                <img
                  src="https://source.unsplash.com/QcUJLRMDryQ/800x600"
                  alt="two sliced breads with avocado on top"
                />
              </figure>
            </li>
            <li>
              <figure className="meal-sample">
                <img
                  src="https://source.unsplash.com/lqyJE0XnGf4/800x600"
                  alt="flatlay of slice citrus on table"
                />
              </figure>
            </li>
            <li>
              <figure className="meal-sample">
                <img
                  src="https://source.unsplash.com/qDQljlZCxz0/800x600"
                  alt="glass pitcher filled kiwi juice"
                />
              </figure>
            </li>
            <li>
              <figure className="meal-sample">
                <img
                  src="https://source.unsplash.com/HYqMhq4gz8c/800x600"
                  alt="bowl of salad with slide of cooked egg with grapes on the side"
                />
              </figure>
            </li>
          </ul>

          <ul className="meals-showcase clearfix">
            <li>
              <figure className="meal-sample">
                <img
                  src="https://source.unsplash.com/-YHSwy6uqvk/800x600"
                  alt="cooked dish on gray bowl"
                />
              </figure>
            </li>
            <li>
              <figure className="meal-sample">
                <img
                  src="https://source.unsplash.com/5X8oLkzZ1fI/800x600"
                  alt="bowl of cereal with sliced fruits and spoon"
                />
              </figure>
            </li>
            <li>
              <figure className="meal-sample">
                <img
                  src="https://source.unsplash.com/6G98hiCJETA/800x600"
                  alt="pancake with chocolate syrup on ceramic plate"
                />
              </figure>
            </li>
            <li>
              <figure className="meal-sample">
                <img
                  src="https://source.unsplash.com/L1ZhjK-R6uc/800x600"
                  alt="brown chopsticks on white bowl"
                />
              </figure>
            </li>
          </ul>
        </div>
        <div className="section-door-to-door-delivery" id="delivery">
          <div className="row">
            <h2>
              Door-to-door food delivery - just a few clicks or taps away on yo
              phone or web
            </h2>
          </div>

          <div className="row">
            <div className="col">
              <div className="col-flex order-steps">
                <img
                  src={require('../../img/3fs-app.png')}
                  alt="3fs mobile app"
                  className="app-tap-order"
                />
              </div>
              <div className="col-flex order-steps">
                <div className="order-step">
                  <div className="number">1</div>
                  <p>
                    Signup today and choose a subscription plan which fits your
                    needs
                  </p>
                </div>
                <div className="order-step">
                  <div className="number">2</div>
                  <p>
                    Order your best delicious meal using our mobile app or
                    website. Or you can even call us!
                  </p>
                </div>
                <div className="order-step">
                  <div className="number">3</div>
                  <p>
                    3Fs Boltman Driver will deliver your meal after less than 30
                    minutes right next to your door
                  </p>
                </div>

                <Link to="#googleplaystore" className="btn-app">
                  <img
                    src={require('../../img/mobile-googleplay.png')}
                    alt="play store button"
                  />
                </Link>
                <Link to="#applestore" className="btn-app">
                  <img
                    src={require('../../img/mobile-applestore.png')}
                    alt="App store button"
                  />
                </Link>
              </div>
            </div>
          </div>
        </div>
        <div className="section-subscription-plans" id="hungry-signup">
          <div className="row">
            <h2>Start eating healthy &amp; fresh today</h2>
          </div>

          <div className="row">
            <div className="col plans">
              <div className="col-flex sub-plan">
                <div className="premium">
                  <h3>Premium</h3>
                  <p className="price">
                    599.9K UGX <span>/ month</span>
                  </p>
                  <p className="price-meal">Only 19.9K per meal</p>
                </div>
                <div className="meal-toppings">
                  <ul>
                    <li>
                      <i className="ion-ios-checkmark-outline i-checkmark" />1
                      meal every day
                    </li>
                    <li>
                      <i className="ion-ios-checkmark-outline i-checkmark" />
                      Order 24/7
                    </li>
                    <li>
                      <i className="ion-ios-checkmark-outline i-checkmark" />
                      Access to newest meal offers
                    </li>
                    <li>
                      <i className="ion-ios-checkmark-outline i-checkmark" />
                      Free delivery
                    </li>
                  </ul>
                </div>
                <div className="signup-now">
                  <Link to="/signup" className="btn btn-light">
                    Sign up now
                  </Link>
                </div>
              </div>

              <div className="col-flex sub-plan">
                <div className="pro">
                  <h3>Pro</h3>
                  <p className="price">
                    239.9K UGX <span>/ month</span>
                  </p>
                  <p className="price-meal">Only 23.9K per meal</p>
                </div>
                <div className="meal-toppings">
                  <ul>
                    <li>
                      <i className="ion-ios-checkmark-outline i-checkmark" />1
                      meal 10 days/month
                    </li>
                    <li>
                      <i className="ion-ios-checkmark-outline i-checkmark" />
                      Order 24/7
                    </li>
                    <li>
                      <i className="ion-ios-checkmark-outline i-checkmark" />
                      Access to newest meal offers
                    </li>
                    <li>
                      <i className="ion-ios-checkmark-outline i-checkmark" />
                      Free delivery
                    </li>
                  </ul>
                </div>
                <div className="signup-now">
                  <Link to="/signup" className="btn btn-light">
                    Sign up now
                  </Link>
                </div>
              </div>

              <div className="col-flex sub-plan">
                <div className="starter">
                  <h3>Starter</h3>
                  <p className="price">
                    29.9K UGX <span>/ meal</span>
                  </p>
                  <p className="price-meal">&nbsp;</p>
                </div>
                <div className="meal-toppings">
                  <ul>
                    <li>
                      <i className="ion-ios-checkmark-outline i-checkmark" />1
                      meal
                    </li>
                    <li>
                      <i className="ion-ios-checkmark-outline i-checkmark" />
                      Order from 8 am to 12 pm
                    </li>
                    <li>
                      <i className="ion-ios-close-outline i-checkmark" />
                    </li>
                    <li>
                      <i className="ion-ios-checkmark-outline i-checkmark" />
                      Free delivery
                    </li>
                  </ul>
                </div>
                <div className="signup-now">
                  <Link to="/signup" className="btn btn-light">
                    Sign up now
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </div>
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
      </div>
    );
  }
}
export default Landing;
