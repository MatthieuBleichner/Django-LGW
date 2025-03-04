# Django-LGW

This is a Django application used to load some orders and retrieve them using API's endpoint. SQLITE, django's SGBD is used to store all data.

### Setup

- Clone this repo
- run `python -m venv env`
- run `source env/bin/activate`
- `cd Django`
- install dependencies `pip install -r requirements.txt`
- `python manage.py makemigrations && python manage.py migrate`

### Import Data

In order to feed the database you can import a local xml file using this command:

- `python manage.py importData <path/to/your/xml/file>`

Where `<path/to/your/xml/file>` should be replaced with valid path to your xml file

### API endpoints

/!\ All endpoints are secured and need a valid JWT to be used. If you do not have created any user yet, please run following command `python manage.py createsuperuser --username admin --email admin@example.com`

- run `python manage.py runserver`
- log in by calling `curl  -X POST http://localHost:8000/api/token/ -H "Content-Type: application/json" -d '{"username": "admin", "password": "admin"}'`
- In the response you'll find your JWT token whithin `access` key. Copy paste it


Here are the two main endpoints used to retrieve orders
- get all orders: 
```curl -X GET http://127.0.0.1:8000/orders/ -H "Authorization: Bearer yourJWTToken"```
- get a specific order ```curl -X GET http://localhost:8000/orders/XXX/ -H "Authorization: Bearer yourJWTToken"``` (where XXX is the id of the order eg: http://127.0.0.1:8000/orders/111-2222222-3333333/)

[!WARNING]
/!\ Warning do not forget extra `/` at the end of the path due to Django URLs' normalization

### Tests

Run `python manage.py test` to run all unit tests