from django.db import models


class User(models.Model):
    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    password = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    source_addres = models.CharField(
        max_length=100
    )

    wallet_name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user'
