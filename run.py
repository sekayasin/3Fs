from api import fff, fastfoodfast_db

db = fastfoodfast_db.DatabaseConnection()

""" run the application """
if __name__=='__main__':
    db.create_all_db_schemas()
    fff.run(debug=True)