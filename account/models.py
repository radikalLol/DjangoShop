from django.db import models
import jwt
from datetime import datetime, timedelta
# Create your models here.
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
  # token = models.CharField(max_length=500, null=True, default="")
  # username = models.CharField(max_length=500, null=True, default="")

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

class UserManager(BaseUserManager):

    def create_user(self, first_name, username, email, password2, password=None):

        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(first_name=first_name, username=username, email=self.normalize_email(email))

        if password != password2:
            raise TypeError('Passwords don\'t match.')
        else:
            user.set_password(password)
            user.save()
        profile = Profile.objects.create(user=user)
        return user

    def create_superuser(self, username, email, password):

        if password is None:
            raise TypeError('Superusers must have a password.')
        
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        profile = Profile.objects.create(user=user)
        return user

class user(AbstractUser,models.Model):

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), blank=True, unique=True, error_messages={
            'unique': _("A user with that email already exists."),
        }, 
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
    date_joined = models.DateTimeField( _('date joined'), default=timezone.now)
    UserBalance = models.DecimalField( _('balance'), default=0, max_digits=18, decimal_places=6)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']
    
    objects = UserManager()

    def __str__(self):

        return self.email

    @property
    def token(self):

        return self._generate_jwt_token()

    def get_short_name(self):

        return self.username

    def _generate_jwt_token(self):
        
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    def uniqueId(self):
         return self.uid()
    def uid(self):
        uniqueId = urlsafe_base64_decode(self.pk).decode()
        return uniqueId
  #  USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = ['first_name']
 
   # def save(self, *args, **kwargs):
      #  super(User, self).save(*args, **kwargs)
      #  return self

