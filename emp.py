# Employee Management System
import json
import os

# Create employee.json if it doesn't exist
if not os.path.exists("employee.json"):
    with open("employee.json", "w") as file:
        json.dump([], file)

while True:
    print("\nWelcome to the Employee Management System for Hks Inc.")
    print("Menu")
    print("1. Add Employee")
    print("2. View all Employees")
    print("3. Search by ID")
    print("4. Exit")

    ch = input("Enter your choice (1/2/3/4): ")

    if ch == "1":
        EmpID = int(input("Enter Employee ID: "))
        Name = input("Enter Name: ")
        Department = input("Enter Department: ")

        employee = {
            "EmpID": EmpID,
            "Name": Name,
            "Department": Department
        }

        with open("employee.json", "r") as file:
            emp_data = json.load(file)

        emp_data.append(employee)

        with open("employee.json", "w") as file:
            json.dump(emp_data, file, indent=4)

        print("Employee added successfully!")

    elif ch == "2":
        with open("employee.json", "r") as file:
            emp_data = json.load(file)

        if len(emp_data) == 0:
            print("No employees found.")
        else:
            for emp in emp_data:
                print(f"Employee ID : {emp['EmpID']}")
                print(f"Name        : {emp['Name']}")
                print(f"Department  : {emp['Department']}")
                print("-" * 30)

    elif ch == "3":
        search_id = int(input("Enter Employee ID to search: "))

        with open("employee.json", "r") as file:
            emp_data = json.load(file)

        found = False
        for emp in emp_data:
            if emp["EmpID"] == search_id:
                print("\nEmployee Found")
                print(f"Employee ID : {emp['EmpID']}")
                print(f"Name        : {emp['Name']}")
                print(f"Department  : {emp['Department']}")
                found = True
                break

        if not found:
            print("Employee not found.")

    elif ch == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")