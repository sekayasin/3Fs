import psycopg2 as pg2
from psycopg2.extras import RealDictCursor
from datetime import datetime

class DatabaseConnection:
    """
    DatabaseConnection Class 
    - Handles the connection to a PostgreSQL database instance.
    Local connection
    "dbname='fastfoodfast_test_db' 
    password='' 
    host='localhost' 
    port='5432' 
    user='sekayasin'
    sslmode='require'

    Heroku rotates credentials periodically and 
    updates applications where this database is attached.

    Host ec2-54-225-68-133.compute-1.amazonaws.com
    Database d3h5fquda8ms9u
    User gjgjeoxmwaoipq
    Port 5432
    Password 403fa6bb565ae3bc600488f58fd1e5d4acaef14d92bc7749065ed1fc2f89aca6
    URI postgres://gjgjeoxmwaoipq:403fa6bb565ae3bc600488f58fd1e5d4acaef14d92bc7749065ed1fc2f89aca6@ec2-54-225-68-133.compute-1.amazonaws.com:5432/d3h5fquda8ms9u
    """

    # DATABASE_URL = os.environ['postgres://gjgjeoxmwaoipq:403fa6bb565ae3bc600488f58fd1e5d4acaef14d92bc7749065ed1fc2f89aca6@ec2-54-225-68-133.compute-1.amazonaws.com:5432/d3h5fquda8ms9u']

    def __init__(self):
        try:
            self.db_connection = pg2.connect(
                "dbname='d3h5fquda8ms9u' \
                password='403fa6bb565ae3bc600488f58fd1e5d4acaef14d92bc7749065ed1fc2f89aca6' \
                host='ec2-54-225-68-133.compute-1.amazonaws.com' \
                port='5432' \
                user='gjgjeoxmwaoipq'\
                ")            
            self.db_connection.autocommit = True
            self.cursor = self.db_connection.cursor(cursor_factory=RealDictCursor)
            print("Database Connection: Success")
        except pg2.DatabaseError as e:
            print("Cannot connect to any database. {}".format(e))
    
    """
    Setting tables for our fastfoodfast_db
    - roles_table
    - customer_table
    - menu_table
    - orders_table

    Setting tables for tests
    - roles_test_table
    - customer_test_table
    - menu_test_table
    - orders_test_table
    """
    def create_all_db_schemas(self):
        
        create_roles_table = "\
        CREATE TABLE IF NOT EXISTS roles (\
        role_id serial PRIMARY KEY,\
        role_name VARCHAR(50) NOT NULL UNIQUE)"
        self.cursor.execute(create_roles_table)

        roles_test_table = "CREATE TABLE IF NOT EXISTS roles_test (LIKE roles)"
        self.cursor.execute(roles_test_table)

        create_users_table = "\
        CREATE TABLE IF NOT EXISTS users (\
        user_id serial PRIMARY KEY,\
        role_id integer NOT NULL,\
        first_name VARCHAR(50) NOT NULL,\
        last_name VARCHAR(50) NOT NULL,\
        username VARCHAR(50) NOT NULL UNIQUE,\
        password VARCHAR(50) NOT NULL,\
        email VARCHAR(255) NOT NULL UNIQUE,\
        address VARCHAR(255) NOT NULL,\
        tel VARCHAR(50) NOT NULL,\
        FOREIGN KEY(role_id) REFERENCES roles(role_id) ON UPDATE CASCADE ON DELETE CASCADE)"
        self.cursor.execute(create_users_table)

        users_test_table = "CREATE TABLE IF NOT EXISTS users_test (LIKE users)"
        self.cursor.execute(users_test_table)

        create_menu_table = "\
        CREATE TABLE IF NOT EXISTS menu (\
        dish_id serial PRIMARY KEY,\
        dish_name VARCHAR(50) UNIQUE NOT NULL,\
        dish_price integer NOT NULL,\
        dish_toppings VARCHAR(50) NOT NULL)"
        self.cursor.execute(create_menu_table)

        menu_test_table = "CREATE TABLE IF NOT EXISTS menu_test (LIKE menu)"
        self.cursor.execute(menu_test_table)

        create_orders_table = "\
        CREATE TABLE IF NOT EXISTS orders (\
        order_id serial PRIMARY KEY,\
        user_id integer NOT NULL,\
        dish_id integer NOT NULL,\
        order_quantity integer NOT NULL,\
        total_order_cost integer NOT NULL,\
        order_status VARCHAR(50) NOT NULL,\
        order_timestamp TIMESTAMP NOT NULL,\
        FOREIGN KEY(user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE CASCADE,\
        FOREIGN KEY(dish_id) REFERENCES menu(dish_id) ON UPDATE CASCADE ON DELETE CASCADE)"
        
        self.cursor.execute(create_orders_table)

        orders_test_table = "CREATE TABLE IF NOT EXISTS orders_test (LIKE orders)"
        self.cursor.execute(orders_test_table)

        print("Schema creation: Success")


    def add_a_role(self, role_name):
        """
        This is an SQL Query to insert a new role
        :param str role_name: The role name of a user ( forexample is_admin, and is_user)
        """
        self.role_name = role_name

        sql = """ INSERT INTO roles(
            role_name)
            VALUES('{}')""".format(
                self.role_name 
            )
        
        self.cursor.execute(sql,(role_name,))
        print("role creation: Success")
        

    def user_sign_up(self, first_name, last_name, username, password, email, address, tel):
        """
        This is an SQL Query to insert a new user
        :param int role_id: This references the roles table, and a user has a role_id of 2
        :param str first_name: first name of the customer
        :param str last_name: last name of the customer
        :param str username: a unique username of the customer
        :param str password: password of the customer
        :param str email: a unique email of the customer
        :param str address: the address of the customer
        :param str tel: the mobile contact of the customer
        """
        self.role_id = 2
        self.first_name = " ".join(first_name.split()).lower()
        self.last_name = " ".join(last_name.split()).lower()
        self.username = " ".join(username.split()).lower()
        self.password = " ".join(password.split()).lower()
        self.email = " ".join(email.split()).lower()
        self.address = " ".join(address.split()).lower()
        self.tel = "-".join(tel.split())

        checkusername_sql = """ SELECT * from users WHERE username = '{}'""".format(self.username)
        self.cursor.execute(checkusername_sql)
        if self.cursor.rowcount > 0:
            return "Username Available, Try Again"

        checkemail_sql = """ SELECT * from users WHERE email = '{}'""".format(self.email)
        self.cursor.execute(checkemail_sql)
        if self.cursor.rowcount > 0:
            return "Email Available, Try Again"

        sql = """ INSERT INTO users(
            role_id,
            first_name,
            last_name,
            username,
            password,
            email,
            address,
            tel)
            VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
                self.role_id,
                self.first_name,
                self.last_name,
                self.username,
                self.password,
                self.email,
                self.address,
                self.tel 
            )

        self.cursor.execute(sql,(self.first_name, self.last_name, self.username, self.password, self.email, self.address, self.tel))
        return "Success"
    
    def staff_sign_up(self, first_name, last_name, username, password, email, address, tel):
        """
        This is an SQL Query to insert a new staff
        :param int role_id: This references the roles table, and a staff has a role_id of 1
        :param str first_name: first name of the staff
        :param str last_name: last name of the staff
        :param str username: a unique username of the staff
        :param str password: password of the staff
        :param str email: a unique email of the staff
        :param str address: the address of the staff
        :param str tel: the mobile contact of the staff
        """
        self.role_id = 1
        self.first_name = " ".join(first_name.split()).lower()
        self.last_name = " ".join(last_name.split()).lower()
        self.username = " ".join(username.split()).lower()
        self.password = " ".join(password.split()).lower()
        self.email = " ".join(email.split()).lower()
        self.address = " ".join(address.split()).lower()
        self.tel = "-".join(tel.split())

        checkusername_sql = """ SELECT * from users WHERE username = '{}'""".format(self.username)
        self.cursor.execute(checkusername_sql)
        if self.cursor.rowcount > 0:
            return "Username Available, Try Again"

        checkemail_sql = """ SELECT * from users WHERE email = '{}'""".format(self.email)
        self.cursor.execute(checkemail_sql)
        if self.cursor.rowcount > 0:
            return "Email Available, Try Again"

        sql = """ INSERT INTO users(
            role_id,
            first_name,
            last_name,
            username,
            password,
            email,
            address,
            tel)
            VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
                self.role_id,
                self.first_name,
                self.last_name,
                self.username,
                self.password,
                self.email,
                self.address,
                self.tel
            )

        self.cursor.execute(sql,(self.first_name, self.last_name, self.username, self.password, self.email, self.address, self.tel))
        return "Admin Success"
    
    def check_user_pass(self, username):
        """
        This is an SQL Query get a user by username
        """
        sql = """ SELECT * from users WHERE username = '{}'""".format(username)
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            get_user_dict = self.cursor.fetchone()
            return get_user_dict
        return None
    
    def add_menu(self, dish_name, dish_price, dish_toppings):
        """
        This is an SQL Query to add a menu option
        :param str dish_name: name of the dish
        :param int dish_price: cost of the dish
        :param str dish_toppings: Addons on the dish
        """
        self.dish_name = " ".join(dish_name.split()).lower()
        self.dish_price = dish_price
        self.dish_toppings = " ".join(dish_toppings.split()).lower()

        check_dish_name_sql = """ SELECT * from menu WHERE dish_name = '{}'""".format(self.dish_name)
        self.cursor.execute(check_dish_name_sql)
        if self.cursor.rowcount > 0: 
            return "Dish name {} is already on the menu".format(self.dish_name)
        
        if not isinstance(self.dish_price, int):
            return "Dish price must be a real price in a number-integer value"

        sql = """ INSERT INTO menu(
            dish_name,
            dish_price,
            dish_toppings)
            VALUES('{}', '{}', '{}')""".format(
                self.dish_name,
                self.dish_price,
                self.dish_toppings
            )

        self.cursor.execute(sql,(self.dish_name, self.dish_price, self.dish_toppings))
        return '{} has been added on the menu'.format(self.dish_name)
    
    def get_menu(self):
        """
        This is an SQL Query to get the menu items
        """
        sql = """ SELECT * from menu"""
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            menu_dict = self.cursor.fetchall()
            available_menu = [{k: v for k,v in menu_item.items() if k != "dish_id"} for menu_item in menu_dict]
            return available_menu
    
    def place_order(self, username, meal, order_quantity, total_order_cost):
        """
        This is an SQL Query to add a new order
        :param int user_id: ID of the user who has placed an order
        :param int dish_id: ID of the meal the customer has ordered 
        :param int order_quantity: the quantity of the order the customer wants
        :param int total_order_cost: total order cost = quantityXdish_price in menu table
        :param str order_status: the status of the order
        :param datetime: timestamp when the order was placed
        """

        userquery = """ SELECT * from users WHERE username = '{}'""".format(username)
        self.cursor.execute(userquery)
        if self.cursor.rowcount > 0:
            get_user_dict = self.cursor.fetchone()
        else:
            return "Invalid username"
        
        mealquery = """ SELECT * from menu WHERE dish_name = '{}'""".format(meal)
        self.cursor.execute(mealquery)
        if self.cursor.rowcount > 0:
            get_meal_dict = self.cursor.fetchone()
        else:
            return "Sorry, That Meal type of meal is not available, check again todays menu"
        
        self.user_id = get_user_dict['user_id']
        self.dish_id = get_meal_dict['dish_id']
        self.order_quantity = order_quantity
        self.total_order_cost = total_order_cost
        self.order_status = "NEW"
        self.order_timestamp = str(datetime.now())

        if not isinstance(self.order_quantity, int):
            return "Order quantity must be in a number-integer value"
        
        if not isinstance(self.total_order_cost, int):
            return "Order quantity must be in a real price number-integer value"
        
        sql = """ INSERT INTO orders(
            user_id,
            dish_id,
            order_quantity,
            total_order_cost,
            order_status,
            order_timestamp)
            VALUES('{}', '{}', '{}', '{}', '{}','{}')""".format(
                self.user_id, 
                self.dish_id,
                self.order_quantity,
                self.total_order_cost,
                self.order_status,
                self.order_timestamp)
        
        self.cursor.execute(sql, (self.order_quantity, self.total_order_cost))
        return "You\'ve successfully placed an order, Your Request is forwarded to our master chef"

    def get_all_orders(self):
        """ This is an SQL Query to get all the  orders """
        get_all_orders_query = """ SELECT order_id, username, email, address,
        dish_name, order_quantity, total_order_cost, order_status, order_timestamp FROM users 
        INNER JOIN orders ON orders.user_id = users.user_id 
        INNER JOIN menu on orders.dish_id = menu.dish_id """

        self.cursor.execute(get_all_orders_query)
        if self.cursor.rowcount > 0:
            all_orders = self.cursor.fetchall()
            return all_orders
    
    def get_order_by_id(self, order_id):
        """ This is an SQL Query to get a specific order """
        
        self.order_id = order_id

        get_order = """ SELECT order_id, username, email, address,
        dish_name, order_quantity, total_order_cost, order_status, order_timestamp FROM users 
        INNER JOIN orders ON orders.user_id = users.user_id 
        INNER JOIN menu on orders.dish_id = menu.dish_id WHERE order_id = '{}'""".format(self.order_id)

        self.cursor.execute(get_order)
        if self.cursor.rowcount > 0:
            order = self.cursor.fetchone()
            return order
        return "Invalid order ID"
    
    def get_user_specific_orders_by_username(self, username):
        """ This is an SQL Query to get a user specific order """

        self.username = username

        get_user_specific_orders = """ SELECT order_id, username, email, address,
        dish_name, order_quantity, total_order_cost, order_status, order_timestamp FROM users 
        INNER JOIN orders ON orders.user_id = users.user_id 
        INNER JOIN menu on orders.dish_id = menu.dish_id WHERE username = '{}'""".format(self.username)

        self.cursor.execute(get_user_specific_orders)
        if self.cursor.rowcount > 0:
            user_orders = self.cursor.fetchall()
            return user_orders 


    def update_order_status(self, order_id, order_status):
        """ This is an SQL Query to update the  status """
        
        self.order_id = order_id
        self.order_status = order_status

        query_order = """ SELECT * FROM orders WHERE order_id = '{}'""".format(self.order_id)
        self.cursor.execute(query_order)

        if self.cursor.rowcount > 0:
            update_order = """ UPDATE orders SET order_status = '{}' WHERE order_id = '{}'""".format(self.order_status, self.order_id)
            self.cursor.execute(update_order)
            return "Order Status has been changed to {}".format(self.order_status)
        return "OrderID {} Unknown,  Kindly confirm the order ID you wish to update".format(self.order_id)

    
    def remove_completed_order(self, order_id):
        """ This is an SQL Query to delete an order marked complete """

        self.order_id = order_id

        query_order = """ SELECT * FROM orders WHERE order_id = '{}'""".format(self.order_id)
        self.cursor.execute(query_order)

        if self.cursor.rowcount > 0:
            delete_order = """ DELETE FROM orders WHERE order_id = '{}'""".format(self.order_id)
            self.cursor.execute(delete_order)
            return "Order {} has been Marked Complete, Done, Removed, and cannot be traced back".format(self.order_id)
        return "OrderID {} Unknown, Kindly confirm the order ID you wish to Mark Complete and Remove".format(self.order_id)  






