from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, send_mail,BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, phone_number, email, password, is_staff, is_superuser, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        now = timezone.now()
        #if phone_number != None:
        #    email = phone_number
        #else:
        #    phone_number = email
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        # GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        # username = GlobalUserModel.normalize_username(username)
        user = self.model(phone_number=phone_number,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          date_joined=now,
                          username=username,
                          email=email,
                          **extra_fields)

        # user.password = make_password(password)
        # user.save(using=self._db)
        if not extra_fields.get('no_password'):
            user.set_password(password)

        user.save(using=self._db)
        return user

    def create_user(self, phone_number=None, password=None, **extra_fields):
        
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, password, is_staff, is_superuser, **extra_fields)

    def create_superuser(self, phone_number, email, password, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(phone_number, email, password, is_staff, is_superuser, **extra_fields)

    def get_by_phone_number(self, phone_number):
        return self.get(**{'phone_number': phone_number})



class BaseUser(AbstractBaseUser, PermissionsMixin):
    # username = models.CharField(
    #    verbose_name= _('username'),
    #    max_length=64,
    #    unique=True,
    #    help_text=_(
    #        'Required. 32 characters or fewer. Letters, digits and . _ only.'),
    #    error_messages={
    #        'unique': _("A user with that username already exists."),
    #    },)
    phone_number = models.BigIntegerField(
        _('phone number'),
        unique=True,
        validators=[validators.RegexValidator(
            r'^09[0-3,9]\d{8}$', _('Enter a valid number phone'), 'invalid')],
        error_messages={
            'unique': _("A user with that phone number already exists."),
        },
        null=True,
    )
    #optional
    name = models.CharField(
        _('first name'), max_length=64, blank=True, null=True)
    email = models.EmailField(
        _('email address'), unique=True, null=True, blank=True)
    nick_name = models.CharField(verbose_name=_('nick name'),max_length=150,blank=True,null=True)
    avatar = models.ImageField(verbose_name=_('avatar'),upload_to='user/%Y/%m/%d/', blank=True, null=True)
    birthday = models.DateField(verbose_name=_('birthday'),null=True,blank=True)
    gender = models.BooleanField(verbose_name=_('gender'),null=True,blank=True,help_text=_('female is False,male is True,null is unset'))
    date_joined = models.DateTimeField(verbose_name=_('date joined'), default=timezone.now)
    
    is_staff = models.BooleanField(
        verbose_name=_('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    
    
    objects = UserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'users'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_loggein_user(self):
        return self.phone_number is not None or self.email is not None

    def save(self, *args, **kwargs):
        if self.email is not None and self.email.strip() == '':
            self.email = None
        super().save(*args, **kwargs)