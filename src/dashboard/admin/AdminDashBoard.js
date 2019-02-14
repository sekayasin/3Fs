import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class AdminDashBoard extends Component {
  render() {
    return (
      <div>
        <section className="userdashboard-header">
          <div className="row">
            <div className="clearfix">
              <div className="userdashboard-title">&nbsp;</div>
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
                      <span id="adminloggedin">Hello Rudy!</span>
                    </Link>
                  </li>
                  <li>
                    <Link to="#email">
                      <i className="ion-ios-email-outline" />
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
            <div className="col dashboard-stats">
              <div className="col-flex new-users">
                <p className="price">
                  <i className="ion-ios-people" />
                  <br />
                  3 659 <br />
                  <span>New Users</span>
                </p>
              </div>

              <div className="col-flex new-orders">
                <p className="price">
                  <i className="ion-ios-cart" />
                  <br />
                  19 364 <br />
                  <span>New Orders</span>
                </p>
              </div>

              <div className="col-flex total-sales">
                <p className="price">
                  <i className="ion-social-usd" />
                  <br />
                  165 984 <br />
                  <span>Sales</span>
                </p>
              </div>

              <div className="col-flex total-visits">
                <p className="price">
                  <i className="ion-eye" />
                  <br />
                  29 651 <br />
                  <span>Visits</span>
                </p>
              </div>
            </div>
          </div>

          <div className="row">
            <div className="dashboard-userinfo clearfix">
              <div className="admin-calendar-time clearfix">
                <div className="admin-calendar">
                  <div>
                    <i className="ion-ios-calendar" />
                  </div>
                  <div>
                    <p>
                      Friday <br />
                      28 September 2018
                    </p>
                  </div>
                </div>
                <div className="admin-time">
                  <div>
                    <i className="ion-ios-clock" />
                  </div>
                  <div>
                    <p>11:40:08</p>
                  </div>
                </div>
              </div>

              <div className="summary-stats">
                <div className="col">
                  <div className="col-flex">
                    <div className="sales-in-act-stats">
                      <i className="ion-social-usd" />
                    </div>
                    <p className="price stats-sales">
                      6,175<span> Sales</span>
                    </p>
                  </div>

                  <div className="col-flex">
                    <div className="visits-in-act-stats">
                      <i className="ion-eye" />
                    </div>
                    <p className="price stats-visits">
                      8,213<span> Visits</span>
                    </p>
                  </div>

                  <div className="col-flex">
                    <div className="users-in-act-stats">
                      <i className="ion-ios-person" />
                    </div>
                    <p className="price stats-users">
                      632<span> Users</span>
                    </p>
                  </div>
                </div>
                <div className="admin-actual-stats">
                  <p>
                    Actual Stats in the last <strong>4 months</strong>
                  </p>
                </div>
              </div>
            </div>
          </div>

          <div className="row">
            <div className="admin-dashboard-links">
              <ul className="admin-dashboard-links-header">
                <li>
                  <Link to="#notification">
                    <span>Notifications</span>
                  </Link>
                </li>
                <li>
                  <Link to="#view-orders">View Orders</Link>
                </li>
                <li>
                  <Link to="/adminadditems">
                    <i className="ion-ios-plus-empty" />
                    <span>ADD New Items</span>
                  </Link>
                </li>
              </ul>
            </div>

            <div className="col">
              <div className="col-flex">#Order ID</div>
              <div className="col-flex">Client Details</div>
              <div className="col-flex">Order Description</div>
              <div className="col-flex">Order Total fees</div>
              <div className="col-flex">Approval Status</div>
            </div>

            <div className="orders col">
              <div className="order-number col-flex">
                <Link to="#BD78463">
                  <strong>BD78463</strong>
                </Link>
              </div>
              <div className="order-img col-flex">
                Name: John Doe <br />
                Tel: +256 7239047 <br />
                Address: 12A Kevina Rd
              </div>
              <div className="order-name col-flex">
                <strong>Biri Supu n'eggi</strong>
                <br />
                OrderDate: 11/09/18 | 10:30 am <br />
                AssignedDriver: Ssalongo Boda
              </div>
              <div className="order-cost col-flex">25K UGX</div>
              <div className="order-remove col-flex">
                <Link to="#accept">
                  <i className="ion-ios-checkmark-empty" />
                  <span>Accept</span>
                </Link>
                <Link to="#decline">
                  <i className="ion-ios-close-empty" />
                  <span>Decline</span>
                </Link>
                <input type="checkbox" />
                Done
              </div>
            </div>

            <div className="orders col">
              <div className="order-number col-flex">
                <Link to="#bd78467">
                  <strong>BD78467</strong>
                </Link>
              </div>
              <div className="order-img col-flex">
                Name: John Doe <br />
                Tel: +256 7239047 <br />
                Address: 12A Kevina Rd
              </div>
              <div className="order-name col-flex">
                <strong>
                  Nyanya Mbisi, chapati Biri, maggi assatu, butungulu ne
                  ka'cabbage
                </strong>
                <br />
                OrderDate: 11/09/18 | 10:30 am <br />
                AssignedDriver: Owakabi Boltman Driver
              </div>
              <div className="order-cost col-flex">20K UGX</div>
              <div className="order-remove col-flex">
                <Link to="#accept">
                  <i className="ion-ios-checkmark-empty" />
                  <span>Accept</span>
                </Link>
                <Link to="#decline">
                  <i className="ion-ios-close-empty" />
                  <span>Decline</span>
                </Link>
                <input type="checkbox" />
                Done
              </div>
            </div>

            <div className="orders col">
              <div className="order-number col-flex">
                <Link to="#bd78480">
                  <strong>BD78480</strong>
                </Link>
              </div>
              <div className="order-img col-flex">
                Name: John Doe <br />
                Tel: +256 7239047 <br />
                Address: 12A Kevina Rd
              </div>
              <div className="order-name col-flex">
                <strong>Kapilawo ne supu w'enkoko</strong>
                <br />
                OrderDate: 11/09/18 | 10:30 am <br />
                AssignedDriver: Owakabi Boltman Driver
              </div>
              <div className="order-cost col-flex">30K UGX</div>
              <div className="order-remove col-flex">
                <Link to="#accept">
                  <i className="ion-ios-checkmark-empty" />
                  <span>Accept</span>
                </Link>
                <Link to="#decline">
                  <i className="ion-ios-close-empty" />
                  <span>Decline</span>
                </Link>
                <input type="checkbox" />
                Done
              </div>
            </div>
          </div>
        </section>
      </div>
    );
  }
}

export default AdminDashBoard;
