from django.db import models


class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user'
