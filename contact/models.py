from django.db import models
from django.utils import timezone

#id é gerado automaticamente pelo django
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

