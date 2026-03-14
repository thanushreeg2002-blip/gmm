import csv
import os
from datetime import date

file_name = "users.csv"

# Create CSV file with header if it doesn't exist
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["User_ID","Full_Name","Email","Age","Country","Signup_Date"])


def register_user():
    name = input("Enter Full Name: ")
    email = input("Enter Email: ")
    age = input("Enter Age: ")
    country = input("Enter Country: ")

    # Get next user ID
    with open(file_name, "r") as file:
        reader = list(csv.reader(file))
        user_id = len(reader)

    signup_date = date.today()

    # Save to CSV
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([user_id, name, email, age, country, signup_date])

    print("User registered successfully!")


register_user()