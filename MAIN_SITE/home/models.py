from django.db import models

class AutoShare(models.Model):

    image = models.ImageField(upload_to='cars/', max_length=100, height_field=None, width_field=None, default=None)
    image_link = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    motor_type = models.CharField(max_length=20)
    power = models.CharField(max_length=20)
    transmition = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Auto info'
        verbose_name_plural = 'Auto info'
