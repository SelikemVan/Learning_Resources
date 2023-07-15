# 1. VARIABLES ASSIGNMENT
# Define a variable named "file_1" and assign a number (integer) to it
# integer is a whole number (no decimals) that could be positive or negative

file_1 = 5000
# Let's view "file_1"
print(file_1)
# Output = 5000
# Define a variable named "file_2" and assign a number (float) to it
# Float are real numbers with a decimal point dividing the integer and fractional parts

file_2 = 2000.5
# Let's view "file_2"
print(file_2)
# Output = 2000.5

# Let's overwrite "file_2" (assume your file value increased)
file_2 = 3000.5

# Notice that "file_2" will only contain the most recent value
print(file_2)
# Output = 3000.5

# Get the type of "file_1" which is integer
#  This is a whole number (no decimals) that could be positive or negative
type(file_1)
# Output = int

# Get the type of "file_2" which is float
# These are real numbers with a decimal point dividing the integer and fractional parts
type(file_2)
# Output = float
# **MINI CHALLENGE #1:**
# - **We defined a variable student_id, and we assigned these 3 values listed below to it.
# Without executing any code cells, what will these lines of code generate?**
# - **Verify your answer by executing the code cells**

# ```
student_id = 3324
student_id = 3400
student_id = 3530
print(student_id)
# ```
# **MINI CHALLENGE #2:**
# - **We defined a variable unicorn_id, and we assigned these 2 values listed below to it.
# Without executing any code cells, what will these lines of code generate?**
# - **Verify your answer by executing the code cells**

# ```
unicorn_id = 112
unicorn_id = 115.3
type(unicorn_id)
# ```

# 2. MATH OPERATIONS
# Define a variable named unicorn_students and initialize it with 5
# Let's assume that we had an additional student now we have 6 students instead of 5
# We can increment unicorn_students by 1 as follows:
unicorn_students = 5
unicorn_students = unicorn_students + 1
print(unicorn_students)
# Output = 6

# Alternatively, we can increment the variable unicorn_students by 1 as follows:
unicorn_students = 5
unicorn_students += 1
print(unicorn_students)
# Output = 6

# Let's assume that the tuition is $260, and we currently have 5 students in our file
# We can calculate the total file value (account balance) as follows:
student_count = 5
student_price = 260
account_balance = student_count * student_price
print(account_balance)
# Output = 1300

# Let's assume we have $20000 USD in our account
# We want to pay the tutors using the total amount
# A tutor is paid $3116 each

account_balance = 20000
print(account_balance)
# Output = 20000

# Divide the account balance by the amount paid to each tutor and place the answer in units
tutor_fee = 3116
units = account_balance/tutor_fee
print(units)
# Output = 6..418485237483954

# **MINI CHALLENGE #3:**
# Write a code that calculates the total amount of money unicorn developers spend on tutor fees
# The total number of tutors are 23 and each tutor is paid 2500 GhC**

# MINI CHALLENGE #4:

# Write a code that takes in the amount students paid a day
# And calculate the total amount of money received after two days:
# fees paid on day 1 = 260 cedis
# fees paid on day 2 = 280 cedis

# 3. ORDER OF OPERATIONS (PRECEDENCE)

# add 3 and 4 and then multiply the answer by 5
# Note that parentheses have the highest precedence
print((3 + 4) * 5)
# Output == 35

# Multiplication has higher precedence compared to addition
print(1 + 2 * 3)
# Output = 7

# Division has higher precedence compared to addition
print(16 / 4 + 25 / 5)
# Output = 9.0

# MINI CHALLENGE 5
# - **Assume that 15 students joined the coding program at a fee of 300 cedis per a student.
# Unicorn developers later increased the fee to 500 cedis per a student. Calculate the profit that will be made.**

# **MINI CHALLENGE #6:**
# - **Write a code that performs the following mathematical operation: z = (x − y) * (x + y)**

# 4. PRINT OPERATION

# Print function is used to print elements on the screen
# Define a string x
# A string in Python is a sequence of characters
# String in python are surrounded by single or double quotation marks
x = "Welcome to Python towards data science track"

# Obtain the data type for 'x'
type(x)
# Output = str

# Print x
print(x)
# Output = Welcome to Python towards data science track

# Define a string and put 'Unicorn Developers' in it
company_name = "Unicorn Developers"

# The format() method formats the specified value and insert it in the placeholder.
# The placeholder is defined using curly braces: {}
print("Student name at {} is Barbara".format(company_name))
# Output = Student name at Unicorn Developers is Barbara

# **MINI CHALLENGE #7:**
# - **Write a code that print out the above statement along with your name**
# - **i.e.: The total number of students at Unicorn Developers are 30. (Barbara)**

# 5. GET USER INPUT

# input is a built-in function in python
# Get student name as an input and print it out on the screen
name = input("Welcome to unicorn developers, What's your name: ")
print('Hello', name)
# Output = Welcome to unicorn developers, What's your name: Barbara
# Hello Barbara

# Obtain student data such as name, age and course and print them all out on the screen
name = input("Welcome to unicorn developers, please enter your name: ")
age = input("Enter your age: ")
course = input("Enter the name of your course: ")
print("My name is {}, I am {} years old, and i am studying {} at unicorn developers".format(name, age, course))
# Output = Welcome to unicorn developers, please enter your name: Barbara
# Enter your age: 19
# Enter the name of your course: python
# My name is Barbara, I am 19 years old, and I am studying python at unicorn developers

# Obtain user inputs, perform mathematical operation, and print the results
# Note: Are you getting an error? Move to the next code cell
x = input("Enter the tuition fees: ")
y = input("Enter the number of courses that you want to take: ")
print('The total funds required to take {} courses at {} cedis Is {}'.format(y, x, x * y))
#

# Convert from string datatype to integer datatype prior to performing addition

x = input("Enter the course fees: ")
x = int(x)
y = input("Enter the number of courses that you want to take: ")
y = int(y)
print('The total funds required to take {} courses at {} cedis per a course is {}'.format(y, x, x*y))
# Output =Enter the course fees: 399
# Enter the number of courses that you want to take: 5
# The total funds required to take 5 courses at 399 cedis per a course is 1995

# **MINI CHALLENGE #8:**
# Write a code that takes in the name of the company,
# course fee,
# the number of courses that you want to study and prints out the total funds required to pay for the courses.
# Find a sample expected output below:**
#
#   - Enter the fee for a course you want to study: 3000
#   - Enter the number of courses that you want to pay for: 5
#   - Enter the name of the company that you want to study at: UniDev
#   - The total funds required to pay for 5 number of UniDev courses at 3000 is 15000

# EXCELLENT JOB
