from django.db import models


class Contact(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
