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
            self.cursor = self.db_connection.cursor(cursor_factory=RealDictCursor)
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
    
    def check_user_pass(self, username):
        """
        This is an SQL Query get a user by username
        """
        sql = """ SELECT * from users WHERE username = '{}'""".format(username)
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            get_user_dict = self.cursor.fetchone()
            return get_user_dict

    



