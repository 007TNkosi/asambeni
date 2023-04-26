# My Driving Gig Web App #

This web app is designed to help me manage my driving gig, where I transport learners between Vosloorus and Germiston/Lambton/Primrose schools. The app allows me to keep track of pick-up and drop-off times, manage user accounts, and accept online payments.

## Features ##

The app includes the following features:

1. Drivers can create and manage their routes
2. Students and parents can sign up, schedule rides, and make payments
3. Students and parents can view the estimated time of arrival for their ride
4. Students can request special songs to be played during their ride
5. The application supports real-time data updates
6. Drivers can sign up and manage their own transportation services, expanding the user base of the application.

## Tech Stack ##

The app is built using Django, a Python web framework that provides a powerful toolkit for building web applications. The app also uses a PostgreSQL database for storing data.

1. Backend: Django, Python
2. Frontend: ReactJS
3. Database: SQLite
4. Other libraries: Bootstrap

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

## Usage ##

To use the app, create an account and log in. From there, you can book rides, track ride progress, and make payments. Passengers can also request songs by sending a message to the driver.

### Future Enhancements ###

- Implement a mobile app for a better user experience on-the-go
- Integrate with a payment gateway for seamless and secure payments
- Implement real-time location tracking for improved route management

### Contributing ###

Contributions to the app are welcome! If you have any ideas for new features or improvements, please feel free to submit a pull request. <br>
For any inquiries or feedback, please contact tnkosi.code@gmail.com.

### License ###

This app is licensed under the MIT License. See the LICENSE file for more information.