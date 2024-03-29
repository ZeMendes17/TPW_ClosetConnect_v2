# ClosetConnect
Project for TPW class 2023/2024

## Project Description

The project encompasses a robust Django REST application designed to seamlessly handle incoming HTTP requests and execute server-side actions with efficiency.

## Setup

To facilitate the setup of the project, we have the necessary requirements in the requirements.txt file.

Also, we created a python script, "insertData.py" to insert some data into the database, so that the project is not empty.
The users inserted just need to be inserted in the Users table (Authentication and Authorization) in the Django Admin page, with the same username and password.

main commands:
```bash
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python insertData.py
- python manage.py runserver
```

## Functionalities

### User with no account initiated

- Register
- Login
- View products
- View product details

### Normal User with account initiated

- Logout
- View products
- View product details
- Add/Remove product to cart
- View cart
- Buy products in cart
- Add/Remove/View product to favorites
- View/Update/Delete profile
- View seller profile
- Follow/Unfollow seller
- Add/Remove comment to a user
- Sell a product
- Edit/Delete a product

### Admin User

- Same as Normal User
- Remove products from the website
- Remove comments from the website
- Ban users
- Search for users/products

## Accounts

### Admin
| Username | Password |
| -------- | -------- |
| manel123 | user1234 |

### Normal User
| Username | Password |
| -------- | -------- |
|   joao   | user1234 |
|   jose   | user1234 |



## Features that we would like to implement in the future

- Chat between users
- Notification system
- Checkout system
- Order history
- Search for products

## Authors

| Name             | Number    | E-Mail               |
| ---------------- | --------- | -------------------- |
| Bernardo Pinto   | 105926    | bernardopinto@ua.pt  |
| Filipe Obrist    | 107471    | filipe.obrist@ua.pt  |
| José Mendes      | 107188    | mendes.j@ua.pt       |

## Deployment

http://zemendes17.pythonanywhere.com/