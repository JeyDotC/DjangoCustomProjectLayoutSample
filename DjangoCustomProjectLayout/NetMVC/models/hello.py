from django.db import models

class Hello(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        app_label = "my_app"