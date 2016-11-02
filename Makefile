.PHONY: static

ENTER_VENV := . venv/bin/activate

venv:
	virtualenv -p /usr/bin/python2.7 venv
	$(ENTER_VENV); pip install -r requirements.txt

run:
	$(ENTER_VENV); python manage.py runserver
