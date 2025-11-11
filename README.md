Python Intern Task - User API Data Fetcher
Description
This Python script fetches user data from the JSONPlaceholder API and displays it in a readable format. It demonstrates working with GET APIs, JSON data handling, loops, and error handling.

Requirements
Python 3.6 or higher

requests library

Installation
Step 1: Clone the Repository

git clone <your-repository-url>
cd <repository-name>
Step 2: Install Required Package

pip install requests
How to Run
Run the script using Python:


python main.py
What the Script Does
Fetches Data: Makes a GET request to https://jsonplaceholder.typicode.com/users

Displays All Users: Shows Name, Username, Email, and City for each user

Bonus Feature: Filters and displays only users from cities starting with 'S'

Error Handling: Handles API errors and connection issues gracefully

Expected Output
text
=== ALL USERS ===

User 1:
  Name: Leanne Graham
  Username: Bret
  Email: Sincere@april.biz
  City: Gwenborough
------------------------
...

=== BONUS: USERS FROM CITIES STARTING WITH 'S' ===

User 1:
  Name: Patricia Lebsack
  Username: Karianne
  Email: Julianne.OConner@kory.org
  City: South Elvis
------------------------
Features Implemented
✅ GET API call using requests library
✅ JSON data parsing
✅ Loop through users and display formatted data
✅ Extract nested data (address.city)
✅ Bonus: Filter users by city starting with 'S'
✅ Bonus: Error handling for API failures

Author
Naman Srivastava

License
This project is created for internship assessment purposes.