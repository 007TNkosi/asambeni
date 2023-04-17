# My Driving Gig Web App #

This web app is designed to help me manage my driving gig, where I transport learners between Vosloorus and Germiston/Lambton/Primrose schools. The app allows me to keep track of pick-up and drop-off times, manage user accounts, and accept online payments.

## Features ##

The app includes the following features:

1. User authentication and authorization
2. User account management
3. Ride booking and scheduling
4. Real-time tracking of ride progress
5. Online payment processing
6. Song request feature for passengers

## Tech Stack ##

The app is built using Django, a Python web framework that provides a powerful toolkit for building web applications. The app also uses a PostgreSQL database for storing data.

## Installation ##

To install the app, clone the repository from GitHub and set up a virtual environment. Then, install the dependencies using pip in your shell:

```shell
$ git clone https://github.com/my-driving-gig-app.git
$ cd my-driving-gig-app
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Next, set up the database by running the following commands:

```ruby
$ python manage.py makemigrations
$ python manage.py migrate
```

Finally, start the development server:

```ruby
$ python manage.py runserver
```

The app should now be accessible at http://localhost:8000.
Usage

To use the app, create an account and log in. From there, you can book rides, track ride progress, and make payments. Passengers can also request songs by sending a message to the driver.

### Contributing ###

Contributions to the app are welcome! If you have any ideas for new features or improvements, please feel free to submit a pull request.

### License ###

This app is licensed under the MIT License. See the LICENSE file for more information.