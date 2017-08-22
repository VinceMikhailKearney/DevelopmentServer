.PHONY: static

ENTER_VENV := . venv/bin/activate

venv:
	virtualenv -p python3 venv
	$(ENTER_VENV); pip3 install -r requirements.txt

run:
	$(ENTER_VENV); python3 manage.py runserver

heroku.local:
	heroku local web

heroku.leaders:
	heroku open leaders/mlas

heroku.collect.static:
	heroku run python manage.py collectstatic
