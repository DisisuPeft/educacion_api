# from django.contrib.auth.models import AbstractUser, BaseUserManager
# from django.db import models
#
# # Create your models here.
#
# class MyUserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError('El usuario debe contar con un correo electronico')
#         user = self.model(email=self.normalize_email(email))
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password):
#         user = self.create_user(email, password)
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

