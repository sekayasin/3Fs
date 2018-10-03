import psycopg2 as pg2
from psycopg2.extras import RealDictCursor
from datetime import datetime

class DatabaseConnection:
    """
    DatabaseConnection Class 
    - Handles the connection to a PostgreSQL database instance.
    """

    def __init__(self):
        try:
            self.db_connection = pg2.connect(
                "dbname='fastfoodfast_test_db' password='' host='localhost' port='5432' user='sekayasin'")            
            self.db_connection.autocommit = True
            self.cursor = self.db_connection.cursor()
            print("You are connected to fastfoodfast_db")
        except:
            print("Can not onnect to database")
    
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

        """ Close the db_connection """
        self.db_connection.close()


    def add_a_role(self, role_name):
        """
        This is an SQL Query to insert a new role
        :param str role_name: The role name of a user ( forexample is_admin, and is_user)
        """
        self.role_name = role_name

        sql = """ INSERT INTO roles(
            role_name)
            VALUES('{}')""".format(
                role_name 
            )
        
        self.cursor.execute(sql,(role_name,))
        print("role creation: Success")

        self.db_connection.close()
        

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
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.address = address
        self.tel = tel

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
                first_name,
                last_name,
                username,
                password,
                email,
                address,
                tel 
            )

        self.cursor.execute(sql,(first_name, last_name, username, password, email, address, tel))
        print("User creation: Success")

        self.db_connection.close()
    
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
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.address = address
        self.tel = tel

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
                first_name,
                last_name,
                username,
                password,
                email,
                address,
                tel
            )

        self.cursor.execute(sql,(first_name, last_name, username, password, email, address, tel))
        print("Staff creation: Success")

        self.db_connection.close()
    
    def add_menu(self, dish_name, dish_price, dish_toppings):
        """
        This is an SQL Query to add a menu option
        :param str dish_name: name of the dish
        :param int dish_price: cost of the dish
        :param str dish_toppings: Addons on the dish
        """
        self.dish_name = dish_name
        self.dish_price = dish_price
        self.dish_toppings = dish_toppings

        sql = """ INSERT INTO menu(
            dish_name,
            dish_price,
            dish_toppings)
            VALUES('{}', '{}', '{}')""".format(
                dish_name,
                dish_price,
                dish_toppings
            )

        self.cursor.execute(sql,(dish_name, dish_price, dish_toppings))
        print("dish creation: Success")

        self.db_connection.close()
    
    def place_order(self, order_quantity, total_order_cost):
        """
        This is an SQL Query to add a new order
        :param int user_id: ID of the user who has placed an order
        :param int dish_id: ID of the meal the customer has ordered 
        :param int order_quantity: the quantity of the order the customer wants
        :param int total_order_cost: total order cost = quantityXdish_price in menu table
        :param str order_status: the status of the order
        :param datetime: timestamp when the order was placed
        """
        self.user_id = 1
        self.dish_id = 2
        self.order_quantity = order_quantity
        self.total_order_cost = total_order_cost
        self.order_status = "NEW"
        self.order_timestamp = str(datetime.now())

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
        
        self.cursor.execute(sql, (order_quantity, total_order_cost))
        print("order creation: Success")

        self.db_connection.close()



# db = DatabaseConnection()
# db.create_all_db_schemas()
# db.add_a_role("is_admin")
# db.add_a_role("is_user")
# db.user_sign_up('Ibra', 'Kawesa', 'kawesa', 'ibra@bootcamp', 'ibra@me.com', '12A Kevina Rd', '+256772062954')
# db.user_sign_up('Umar', 'Bumalo', 'umsenge', 'umasenge123', 'umasenge@onetouch', '11A Kevina Rd', '+256704062954')
# db.staff_sign_up("Luqman", "Matovu", "matluq", "matluq123", "matluq@fastfoodfast", "1B Haji Sowedi Rd", "+25670030033")
# db.staff_sign_up("Mansour", "Kalasa", "kabiri", "kabiri123", "kalasamayanzi@fastfoodfast", "13 Kawempe Mbogo", "+25689822897")
# db.add_menu("Kikomando", 15, "Nanya mbisi neggi")
# db.add_menu("Chicken Submarine", 20, "Soda and chips")
# db.place_order(1,30)
    



