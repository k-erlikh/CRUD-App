import psycopg

#Database connection based off the four information requirments. If necessary, this can be changed to suit the database and host information
def connectDatabase():
    try:
        connection = psycopg.connect("host=localhost dbname=students user=postgres password=postgres")
        return connection
    except Exception as e:
        print("ERROR: Cannot connect to database.", e)

