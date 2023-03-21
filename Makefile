run:
	python crm/manage.py runserver
migr:
	python crm/manage.py makemigrations && python crm/manage.py migrate
user:
	python crm/manage.py createsuperuser
req:
	pip freeze > requirements.txt
runbot:
	python bot/main.py