import psycopg

# Checks if the table "students" exists in the data base. If it doesnt, it will create the table and populate the columns
def tableExist(connection: psycopg.Connection):
    with connection.cursor() as cur:
        cur.execute("SELECT EXISTS(SELECT FROM information_schema.tables WHERE table_schema=%s AND table_name=%s);", ("students", "students"))
        if not cur.fetchone()[0]:
            print("Table students doesnt exist, creating table...")
            cur.execute("CREATE TABLE IF NOT EXISTS students (student_id SERIAL PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, enrollment_date DATE);")
            connection.commit()
        else:
            print("Table students exists")

# Checks if data exists in the students table. If there is no data, it will popualte the table with the data
def dataExist(connection: psycopg.Connection):
    with connection.cursor() as cur:
        cur.execute("SELECT * FROM students;")
        if cur.rowcount== 0:
            print("Students table empty. Popualting with data...")
            cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('John', 'Doe', 'john.doe@example.com', '2023-09-01'), ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'), ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');")
            connection.commit()
        else:
            print("Student table data exists.")

