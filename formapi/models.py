from django.db import models


class FormModel(models.Model):
    som = models.FloatField()
    usd = models.FloatField()
    euro = models.FloatField()

    auca_fund = models.IntegerField(default=1, choices=((1, '1'), (2, '2'), (3, '3'), (4, '4')))

    email_field = models.EmailField()
    email_confirm = models.EmailField()
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    auca_connection = models.IntegerField(default=1, choices=((1, '1'), (2, '2'), (3, '3'), (4, '4')))
    country = models.CharField(max_length=64, blank=True)
    phone_number = models.CharField(max_length=128, blank=True)

    first_comment = models.TextField(blank=True)
    last_comment = models.TextField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f"Form data ID: {self.id}"
