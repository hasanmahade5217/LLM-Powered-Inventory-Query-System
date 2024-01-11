from langchain.utilities import SQLDatabase



def get_db_object():
    
    db_user = "root"
    db_password = "root"
    db_host ="localhost"
    db_name = "atliq_tshirts"

    # Create a database object
    # this object will show 3 rows from each table of the database
    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", sample_rows_in_table_info=3)

    return db

