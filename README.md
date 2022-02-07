# Discount Code Service

This is a Django App to get create and get discount codes.
- I used default django authentication for the sake of speed, and it's adaptability.
- I also exposed the default login, logout and admin interface of django for test purposes
- That project took me around 3 hours to finish, 2 hours on design and 1 hour on coding
- Model definitions are under the api app
- I only introduced DiscountCode table in the service in the favor of loose coupling

# Installation

### Docker ###

[Docker](https://www.docker.com/) must be installed on your system.

You can also check [getting started](https://www.docker.com/get-started) if you are not familiar with Docker.

To run the server on background with Docker on your system just run the command:
```
docker-compose up -d
```
This will expose your 0.0.0.0:8000 route to accept connections.
### Python ###
You can also run the project without using docker.
In this case [python](https://www.python.org/) and [pip](https://pypi.org/project/pip/) must be installed on your system.

After above requirements are installed you can run the commands:
```
pip install requirements.txt
python manage.py runserver 0.0.0.0:8000
```
This will also expose 0.0.0.0:8000 route to accept connections.


# Usage
When the app is up and running following routes will be accepting connections to create and get discount codes.

Both views are password protected.

Every query parameter except brand is non-mandatory for create view
Percentage field has a limit of 100 and count field has a limit of 2000.
```
- 0.0.0.0:8000/api/create?brand=<int>&count=<int>&percentage=<int>
```

```
- 0.0.0.0:8000/api/get?brand=<int>
```


I have populated the user db to include a number of users with credentials:
```
username: user<id> 
password: pass<id>
```
The exception to this rule is user id with 1 and 2.

User with id 1 is django admin user and user with id 2 have (secure) credentials of:
```
username: guest
password: guest
```
To logout you can just send a get request to url:
```
http://0.0.0.0:8000/accounts/logout/
```

Example data requests:
```
http://0.0.0.0:8000/api/create/?brand=1&count=10&percentage=20
http://0.0.0.0:8000/api/get/?brand=1
```

Author : Yalin Aksoy

Written for a Technical interview with Billogram
