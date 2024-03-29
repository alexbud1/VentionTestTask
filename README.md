
# Test Task Api

This project was done as a test task for intern position in Vention. 

### Documentation
Redoc documentation will be available after successful deployment by link : 

http://127.0.0.1:8000/docs/

### Features
2 models - Category and Task which are related by One to Many relationship.
There are serializers for both models and for registration.

Available endpoints also include 'refresh-login/' for refreshing auth token, 'login/' for obtaining auth token by entering username and password, and 'register/' - for registration.

For endpoint 'category' and 'task' pagination is included.

Admin page is also configured to have the best view on the data.

### Testing
Unit tests are included and will be run before the server is started automatically.
For each endpoint there are tests for both valid and invalid scenarios. Pytest is used for testing.

## Deployment

To deploy this project you need to clone this repository and put .env file with DJANGO_SECRET_KEY in root directory of the project(same dir as manage.py).

```bash
  docker-compose up -d
```

## Access
For comfortable access to the admin panel, you can use the following credentials:

username: vention

password: vention2024

Or instead of using this credentials you can create your own custom superuser by running the following command in terminal inside of container:

```bash
  python manage.py createsuperuser
```


## Screenshots

Documentation overview
[![Screenshot-2024-02-06-at-22-03-52.png](https://i.postimg.cc/W1R6XMRv/Screenshot-2024-02-06-at-22-03-52.png)](https://postimg.cc/tY5xgnCS)

Admin panel overview
[![Screenshot-2024-02-06-at-22-06-21.png](https://i.postimg.cc/2SF9szf3/Screenshot-2024-02-06-at-22-06-21.png)](https://postimg.cc/68qhRxqN)

Quick view at available endpoints
[![Screenshot-2024-02-06-at-22-06-42.png](https://i.postimg.cc/Df9CmWv8/Screenshot-2024-02-06-at-22-06-42.png)](https://postimg.cc/yWThb8SH)

Unit tests are running before the server is started
[![Screenshot-2024-02-08-at-00-12-38.png](https://i.postimg.cc/J0t6HMWr/Screenshot-2024-02-08-at-00-12-38.png)](https://postimg.cc/m1fN0xDJ)
