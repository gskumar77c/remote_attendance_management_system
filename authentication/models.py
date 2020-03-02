from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,AbstractUser



class UserManager(BaseUserManager):
	#createing user
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		user = self.model(
			email=self.normalize_email(email),
		)

		user.set_password(password)
		user.save()
		return user

	def create_staffuser(self, email, password):
		#creating staffuser
		user = self.create_user(
			email,
			password=password,
		)
		user.staff = True
		user.save()
		return user

	def create_superuser(self, email, password):
		#creating superuser
		user = self.create_user(
			email,
			password=password,
		)
		user.staff = True
		user.admin = True
		user.student = False
		user.gsadmin = True
		user.save()
		return user


class User(AbstractBaseUser):
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True,
	)
	active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False) # a admin user; non super-user
	admin = models.BooleanField(default=False) # a superuser
	student = models.BooleanField(default=True)
	faculty = models.BooleanField(default=False)
	gsadmin  = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = [] # add any required fields, email and password are required by default

	objects = UserManager()

	def get_full_name(self):
		# The user is identified by their email address
		return self.email

	def get_short_name(self):
		# The user is identified by their email address
		return self.email

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		#"Does the user have a specific permission?"
		if self.is_active :
			return True
		else :
			return False

	def has_module_perms(self, app_label):
		#"Does the user have permissions to view the app `app_label`?"
		return True

	
	def is_gsadmin(self):
		#"Is the user a gsadmin?"
		return self.gsadmin

	def is_student(self):
		#"Is the user a gsadmin?"
		return self.student

	def is_faculty(self):
		#"Is the user a gsadmin?"
		return self.faculty

	@property
	def is_staff(self):
		#"Is the user a member of staff?"
		return self.staff

	@property
	def is_admin(self):
		#"Is the user a admin member?"
		return self.admin

	@property
	def is_active(self):
		#"Is the user active?"
		return self.active


class StudentRequests(models.Model):
	email  = models.CharField(max_length=250)
	password = models.CharField(max_length=100)
	fullname = models.CharField(max_length=100)
	branch  = models.CharField(max_length=50)

	def __str__(self):
		return self.email


class FacultyRequests(models.Model):
	email  = models.CharField(max_length=250)
	password = models.CharField(max_length=100)
	fullname = models.CharField(max_length=100)
	department  = models.CharField(max_length=50)

	def __str__(self):
		return self.email