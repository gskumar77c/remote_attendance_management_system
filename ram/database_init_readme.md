$find . -maxdepth 6 -path "./*/migrations/*.py" -not -name "__init__.py" -delete

# the above command is to remove all the migrations, 

$drop database ram
$create database ram

# below commands are obvious !
$python3 manage.py makemigrations
$python3 manage.py migrate

# below command might be missed !
$python3 manage.py createsuperuser

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# the following is to untrack files
git rm --cached:profiles/__pyache__/ -r
git rm --cached:courses/__pyache__/ -r
git rm --cached:institution/__pyache__/ -r
git rm --cached:ram/__pyache__/ -r

git rm --cached:profiles/migrations/ -r
git rm --cached:courses/migrations/ -r
git rm --cached:institution/migrations/ -r
git rm --cached:ram/migrations/ -r

git rm --cached:/media/ -r