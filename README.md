# Django-LGW

This is a Django application used to load some orders and retrieve them using API's endpoint

### Setup

- Clone this repo
- run `source env/bin/activate`
- `cd Django`
- install dependencies `pip install -r requirements.txt`
- `python manage.py makemigrations && python manage.py migrate`

### Import Data

In order to feed the database you can import a local xml file using this command:

- `python manage.py importData <path/to/your/xml/file>`

Where `<path/to/your/xml/file>` should be replaced with valid path to your xml file


### Tests

Run `python manage.py test` to run all unit tests