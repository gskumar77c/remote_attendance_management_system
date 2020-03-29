$find . -maxdepth 6 -path "./*/migrations/*.py" -not -name "__init__.py" -delete

# the above command is to remove all the migrations, 

$drop database ram
$create database ram