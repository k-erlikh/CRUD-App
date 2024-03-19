import psycopg
"""
This file contains all four of the CRUD operations for the database.
"""

# Retrieves and prints all of the students in the students table
def getAllStudents(connection: psycopg.Connection):
   with connection.cursor() as cur:
        cur.execute("SELECT * from students")
        request = cur.fetchall()
        print("ID  |First Name     |Last Name      |Email                         |Enrollment Date")
        print("-----------------------------------------------------------------------------------")
        for row in request:
            print(f"{row[0]:4}|{row[1]:15}|{row[2]:15}|{row[3]:30}|{row[4]}")

#Adds a student into the database
def addStudent(connection: psycopg.Connection, first_name, last_name, email, enrollment_date):
    with connection.cursor() as cur:
        cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", 
                    (first_name, last_name, email, enrollment_date))
        connection.commit()
        cur.execute("SELECT first_name, last_name, email, enrollment_date FROM students WHERE first_name = %s AND last_name = %s AND email = %s AND enrollment_date = %s", 
                    (first_name, last_name, email, enrollment_date))
        student = cur.fetchone()
        print(f"Student {first_name} {last_name} successfully added: ")
        print(student)

#Updates the email of a student based off the student id
def updateStudentEmail(connection: psycopg.Connection, student_id, new_email):
    with connection.cursor() as cur:
        cur.execute("UPDATE students SET email=%s WHERE student_id = %s", (new_email, student_id))
        connection.commit()
        cur.execute("SELECT first_name, last_name, email, enrollment_date FROM Students WHERE student_id = %s AND email = %s", 
                    (student_id, new_email))
        student = cur.fetchone()
        print(f"Student with id {student_id} email successfully updated: ")
        print(student)

#Removes a student with the given student id
def deleteStudent(connection: psycopg.Connection, student_id):
    with connection.cursor() as cur:
        cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        connection.commit()
        print(f"Student with id {student_id} successfully deleted: ")


