from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager, PermissionsMixin
	)
from django.core.mail import send_mail
from django.urls import reverse
import datetime
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class CustomUserManager(BaseUserManager):

	def _create_user(self, matric_no, surname, first_name, email, password, **extra_fields):
		"""
		Creates and saves a User with the given username, email and password.
		"""
		if not matric_no:
			raise ValueError('The given matric_no must be set')
		email = self.normalize_email(email)
		user = self.model(matric_no=matric_no, surname=surname, first_name=first_name, email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, matric_no, surname, first_name, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(matric_no, surname, first_name, email, password, **extra_fields)

	def create_superuser(self, matric_no, surname, first_name, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(matric_no, surname, first_name, email, password, **extra_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):

	GENDER = (
		('F', 'female'),
		('M', 'male')
		)

	LEVEL = (
		(100, 1),
		(200, 2),
		(300, 3),
		(400, 4),
		(500, 5),
		)
	
	matric_no = models.CharField(
		_('matric_no'),
		max_length=12,
		unique=True,
		error_messages={
			'unique': _("A user with that matric number already exists."),
		},
	)
	surname = models.CharField(max_length=30, blank=True)
	first_name = models.CharField(max_length=30, blank=True)
	other_name = models.CharField(max_length=30, blank=True)
	email = models.EmailField(max_length=30, unique=True, blank=True)
	phone = models.CharField(max_length=11, blank=True, default='')
	gender = models.CharField('sex', max_length=1, choices=GENDER)
	part = models.IntegerField(default=1, choices=LEVEL)
	birth_date = models.DateField(null=True, blank=True,
		help_text=("You don't necessarily have to enter the"
					" correct year of birth, any year will do.")
		)
	bio = models.CharField(max_length=150, blank=True, null=True)
	image = models.ImageField(upload_to="users/img", blank=True, null=True)
	is_exco = models.BooleanField(
        _('Exco?'),
        default=False,
        help_text=_('Designates whether the user is a member of the executive commitee.'),
    )
	is_alumni = models.BooleanField(
        _('Alumni?'),
        default=False,
        help_text=_('Designates whether the user is a graduate of the department.'),
    )
	is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
	is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
	date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)


	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'matric_no'
	REQUIRED_FIELDS = ['email', 'first_name', 'surname']

	objects = CustomUserManager()

	class Meta:
		verbose_name = 'user'
		verbose_name_plural = 'users'


	def get_full_name(self):
		"""Returns the first_name plus the last_name, with a space in between."""
		full_name = '%s %s' % (self.surname, self.first_name)
		return full_name.strip()

	def get_short_name(self):
		"""Returns the short name for the user."""
		return self.first_name

	def upcoming_birthdays(self):
		today = datetime.date.today()
		bday = self.birth_date.replace(year=today.year) - today
		return (bday < datetime.timedelta(7)) and (bday > datetime.timedelta(0))

	upcoming_birthdays.boolean = True

	def email_user(self, subject, message, from_email=None, **kwargs):
		"""
		Sends an email to this User.
		"""
		send_mail(subject, message, from_email, [self.email], **kwargs)

	def get_absolute_url(self):
		return reverse('users:user_details', kwargs={'pk':self.id})