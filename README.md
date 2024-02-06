
# Test Task Api

This project was done as a test task for intern position in Vention. 

### Documentation
Redoc documentation will be available after successful deployment by link : 

http://127.0.0.1:8000/docs/

### Features
2 models - Category and Task which are related by One to Many relationship.
Serializers for both models and for registration.

Available endpoints also include 'refresh-login/' for refreshing auth token, 'login/' for obtaining auth token by entering username and password, and 'register/' - for registration.

For endpoint 'category' and 'task' pagination is included.

Admin page is also configured to have the best view on the data.


## Deployment

To deploy this project you need to clone this repository and put .env file with DJANGO_SECRET_KEY in root directory of the project(same dir as manage.py).

```bash
  docker-compose up -d
```


## Screenshots

Documentation overview
[![Screenshot-2024-02-06-at-22-03-52.png](https://i.postimg.cc/W1R6XMRv/Screenshot-2024-02-06-at-22-03-52.png)](https://postimg.cc/tY5xgnCS)

Admin panel overview
[![Screenshot-2024-02-06-at-22-06-21.png](https://i.postimg.cc/2SF9szf3/Screenshot-2024-02-06-at-22-06-21.png)](https://postimg.cc/68qhRxqN)

Quick view at available endpoints
[![Screenshot-2024-02-06-at-22-06-42.png](https://i.postimg.cc/Df9CmWv8/Screenshot-2024-02-06-at-22-06-42.png)](https://postimg.cc/yWThb8SH)