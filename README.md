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

- run `python manage.py runserver`
- get all orders: http://127.0.0.1:8000/orders/
- get a specific order http://127.0.0.1:8000/orders/XXX (where XXX is the id of the order eg: http://127.0.0.1:8000/orders/111-2222222-3333333/)


### Tests

Run `python manage.py test` to run all unit tests