from django.db import models

# Create your models here.

class OlxRequest(models.Model):
    url = models.URLField(verbose_name='Url for analis')
    email = models.EmailField(verbose_name='Yor email')
    datetime_add_request = models.DateTimeField(auto_now_add=True)
