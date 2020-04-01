from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        # Validations for the email
        email = postData['email']
        if '@' not in email:
            errors['email'] = "Invalid email"
        if '.' not in email:
            errors['email'] = "Invalid email"

        # Valitdations for the password
        if len(postData['password']) < 8:
            errors['password'] = "Password must be greater than 7 characters"

        return errors

class PasswordManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['company']) < 1:
            errors['length'] = "Company must be provided."

        if len(postData['email']) < 1:
            errors['length'] = "Email must be provided."

        if len(postData['password']) < 1:
            errors['length'] = "Password must be provided."

        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 15)
    last_name = models.CharField(max_length = 15)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 25)
    objects = UserManager()

class Password(models.Model):
    company = models.CharField(max_length = 1)
    email = models.CharField(max_length = 1)
    password = models.CharField(max_length = 1)
    the_user = models.ForeignKey(User, related_name = 'my_passwords', on_delete = models.CASCADE, null = True)
    objects = PasswordManager()
