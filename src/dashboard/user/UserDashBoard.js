import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class UserDashBoard extends Component {
  render() {
    return (
      <div>
        <section className="userdashboard-header">
          <div className="row">
            <div className="clearfix">
              <Link to="/customer">
                <div className="userdashboard-title">
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
              <div className="userdashboard-notifications">
                <ul className="userdashboard-notf-icons">
                  <li>
                    <input type="text" placeholder="Search..." />
                  </li>
                  <li>
                    <Link to="#chat">
                      <i className="ion-ios-chatboxes-outline" />
                    </Link>
                  </li>
                  <li>
                    <Link to="#notification">
                      <i className="ion-android-notifications-none" />
                    </Link>
                  </li>
                  <li>
                    <Link to="#user">
                      <i className="ion-ios-person-outline" />
                      <span id="usernameloggedin">Welcome, John Doe</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="#cart">
                      <i className="ion-ios-cart-outline" />
                    </Link>
                  </li>
                  <li>
                    <Link to="/logout">
                      <i className="ion-log-out" />
                      <span>logout</span>
                    </Link>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </section>
        <section className="userdashboard-links">
          <div className="row">
            <ul className="dashboard-links">
              <li>
                <Link to="#dashboard">Dashboard</Link>
              </li>
              <li>
                <Link to="#place-order">Place order</Link>
              </li>
              <li>
                <Link to="orderhistory.html">Order history</Link>
              </li>
              <li>
                <Link to="#terms">Terms &amp; conditions</Link>
              </li>
              <li>
                <Link to="#add-funds">
                  <i className="ion-ios-plus-empty" />
                  ADD funds
                </Link>
              </li>
            </ul>
          </div>

          <div className="row">
            <div className="col dashboard-stats">
              <div className="col-flex fff-wallet">
                <p className="price">
                  50K UGX <br />
                  <span>Avaliable</span>
                </p>
              </div>

              <div className="col-flex total-receipts">
                <p className="price">
                  670K UGX <br />
                  <span>Total Receipts</span>
                </p>
              </div>

              <div className="col-flex locked">
                <p className="price">
                  0 UGX <br />
                  <span>Locked</span>
                </p>
              </div>
            </div>
          </div>

          <div className="row">
            <div className="dashboard-userinfo clearfix">
              <div className="userdetails clearfix">
                <div className="user-profile">
                  <ul className="userinfo">
                    <li>
                      <i className="ion-ios-person" />
                      <span>John Doe</span>
                    </li>
                    <li>
                      <i className="ion-ios-email" />
                      <span>john.doe@example.com</span>
                    </li>
                    <li>
                      <i className="ion-ios-telephone" />
                      <span>+256 772 062 954</span>
                    </li>
                    <li>
                      <i className="ion-ios-location" />
                      <span>
                        12A Kevina Rd, Kiganda Zone,
                        <br /> Katwe II Parish, Makindye Div
                        <br /> Kampala.
                      </span>
                    </li>
                  </ul>
                </div>
                <div className="user-queries">
                  <ul className="user-query">
                    <li>
                      <Link to="#submit-ticket">Submit Ticket</Link>
                    </li>
                    <li>
                      <Link to="#my-statement">My Statement</Link>
                    </li>
                    <li>
                      <Link to="#monthly-orders">View Monthly Orders</Link>
                    </li>
                    <li>
                      <Link to="#login-history">Login History</Link>
                    </li>
                  </ul>
                </div>
              </div>

              <div className="summary-stats">
                <div className="col">
                  <div className="past-orders col-flex">
                    <strong>44</strong> <br />
                    <span>Available</span>
                  </div>
                  <div className="pending-orders col-flex">
                    <strong>0</strong> <br />
                    <span>Pending</span>
                  </div>
                  <div className="rejected-orders col-flex">
                    <strong>15</strong> <br />
                    <span>Rejected</span>
                  </div>
                </div>
                <div className="order-summary-info">
                  <p>
                    Available, Pending and Rejected order out of Total{' '}
                    <strong>59</strong> Order
                  </p>
                </div>
              </div>
            </div>
          </div>

          <div className="row">
            <div className="order-table-header">
              <ul className="order-header">
                <li>
                  <Link to="#news">
                    <i className="ion-speakerphone" />
                    <span>Announcements</span>
                  </Link>
                </li>
                <li>
                  <Link to="#order">Place Order</Link>
                </li>
                <li>
                  <Link to="orderhistory.html">Last 20 Orders</Link>
                </li>
                <li>
                  <Link to="#pendinginvoices">Pending Invoices</Link>
                </li>
                <li>
                  <Link to="#menu">Top Menu Courses</Link>
                </li>
                <li>
                  <Link to="#appetizer">Top Appetizer</Link>
                </li>
                <li>
                  <Link to="#desserts">Top Desserts</Link>
                </li>
              </ul>
            </div>

            <div className="make-order">
              <select name="order-list" id="#" className="order-select-list">
                <option value="Add New Order">
                  - Select Your Favourite dish, meal course here -
                </option>
                <option value="Rolex">
                  Nyanya Mbisi, chapati ssatu, maggi assatu, butungulu ne
                  cabbage - 20K UGX
                </option>
                <option value="oysters Grill">
                  Cheese, Jalape, chilli, Onion - 20K UGX
                </option>
                <option value="Kikomando">Biri supu ne eggi - 25K UGX</option>
                <option value="oysters Grill">
                  pilawo ne supu w'enkoko - 30K UGX
                </option>
                <option value="oysters Grill">
                  Cheese, Jalape, chilli, Onion - 35k UGX
                </option>
                <option value="oysters Grill">
                  Cheese, Jalape, chilli, Onion - 20K UGX
                </option>
              </select>
              <Link to="#mk-order" className="add-order">
                <i className="ion-ios-plus-empty" />
                Add Item
              </Link>
            </div>

            <div className="orders col" id="mk-order">
              <div className="order-number col-flex">1</div>
              <div className="order-img col-flex">
                <i className="ion-android-restaurant" />
              </div>
              <div className="order-name col-flex">Biri Supu n'eggi</div>
              <div className="order-cost col-flex">25K UGX</div>
              <div className="order-remove col-flex">
                <Link to="#remove-item">
                  <i className="ion-ios-close-empty" />
                  <span>Remove Item</span>
                </Link>
              </div>
            </div>

            <div className="orders col">
              <div className="order-number col-flex">2</div>
              <div className="order-img col-flex">
                <i className="ion-android-restaurant" />
              </div>
              <div className="order-name col-flex">
                Nyanya Mbisi, chapati Biri, maggi assatu, butungulu ne
                ka'cabbage
              </div>
              <div className="order-cost col-flex">20K UGX</div>
              <div className="order-remove col-flex">
                <Link to="#remove-item">
                  <i className="ion-ios-close-empty" />
                  <span>Remove Item</span>
                </Link>
              </div>
            </div>

            <div className="orders col">
              <div className="order-number col-flex">3</div>
              <div className="order-img col-flex">
                <i className="ion-android-restaurant" />
              </div>
              <div className="order-name col-flex">
                Kapilawo ne supu w'enkoko
              </div>
              <div className="order-cost col-flex">30K UGX</div>
              <div className="order-remove col-flex">
                <Link to="#remove-item">
                  <i className="ion-ios-close-empty" />
                  <span>Remove Item</span>
                </Link>
              </div>
            </div>

            <div className="orders col">
              <div className="order-number col-flex">&nbsp;</div>
              <div className="order-img col-flex">&nbsp;</div>
              <div className="order-name col-flex">
                <strong>Total</strong>
              </div>
              <div className="order-cost col-flex">
                <strong>75K UGX</strong>
              </div>
              <div className="order-remove col-flex">&nbsp;</div>
            </div>

            <div className="proceed-to-checkout">
              <Link to="#checkout">Proceed to checkout</Link>
            </div>
          </div>
        </section>
      </div>
    );
  }
}

export default UserDashBoard;
