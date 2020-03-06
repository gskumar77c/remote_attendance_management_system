# Temporary remote_attendance_management_system

See this architecture. I think it follows the layered architecture as in design model and the modularity as in DFD level 2 in seperate layers. Tell me if there are any disadvantages of this model or if it is not feasible or anything.

I read that this will help in unplugging and plugging easier. You just have to change configsettings in settings.py and add new app config settings.

To run the code : 

change the database settings in settings.py

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
