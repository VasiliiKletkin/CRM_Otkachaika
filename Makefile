run:
	python osenezator/manage.py runserver
migr:
	python osenezator/manage.py makemigrations && python osenezator/manage.py migrate
sup:
	python osenezator/manage.py createsuperuser
req:
	pip freeze > requirements.txt
runbot:
	python bot/main.py