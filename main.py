from connect import connectDatabase
from crud import getAllStudents, addStudent, updateStudentEmail, deleteStudent
from database import tableExist, dataExist
"""
The main python app file. This contails the control flow for the command line interface program.
The user can pick from five selections, including the CRUD operations and exiting the program.
The user will be prompted to type in information based on the selection needs.
A connection to the databse is set up at the beginning, and closed when the program interface loop is exited.
Once the script is connected to the database, it will check if the students table and data exist. If either
do not exist, it will create the table and/or populate the data with default data.
"""
def main():
    try:
        connection = connectDatabase() 
        tableExist(connection)
        dataExist(connection)

        selection = -1
        while (selection != 0):
            print("\nSelect an option:")
            print("1: Print all users")
            print("2: Add a user")
            print("3: Update a user")
            print("4: Remove a user")
            print("0: Exit.\n")
            while (selection<0 or selection>4 ):
                selection = int(input("Enter your selection: "))

            if (selection == 0):
                return
            
            elif(selection == 1):
                getAllStudents(connection)

            elif(selection == 2):
                userInput = [0,0,0,0]
                userInput[0] = input("Enter the student first name: ")
                userInput[1] = input("Enter the student last name: ")
                userInput[2] = input("Enter the student email: ")
                userInput[3] = input("Enter the student enrollment date (year-month-date):")
                addStudent(connection, userInput[0], userInput[1], userInput[2], userInput[3])

            elif(selection == 3):
                userInput = [0,0]
                userInput[0] = input("Enter student id: ")
                userInput[1] = input("Enter new email address: ")
                updateStudentEmail(connection, userInput[0], userInput[1])

            elif(selection == 4):
                userSelect = ""
                while userSelect.lower() not in ["yes", "y"]:
                    userInput = input("Enter student id: ")
                    userSelect = input(f"Are you sure you want to delete student {userInput} (y/n): ")
                    print(userSelect)
                
                deleteStudent(connection, userInput)

            selection = -1
        connection.close()
    except:
        print("Exiting from program...")
    

    
if __name__ == "__main__":
    main()