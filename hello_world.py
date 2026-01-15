# Importing the datetime module to get today's date
import datetime

# Asking the user to enter their name
name = input("Enter your name: ")

# Asking the user to enter their internship role
role = input("Enter your internship role: ")

# Getting today's date using datetime module
today_date = datetime.date.today()

# Printing a blank line for better output readability
print()

# Displaying the stored information
print("Name:", name)
print("Internship Role:", role)
print("Today's Date:", today_date)
