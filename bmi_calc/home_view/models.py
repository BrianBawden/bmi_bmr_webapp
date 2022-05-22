from django.db import models

# Create your models here.
class Bmr(models.Model):
    weight = models.DecimalField(blank=False, max_digits=5, decimal_places=2)
    height = models.DecimalField(blank=False, max_digits=5, decimal_places=2)
    Male = 'M'
    Female = "F"
    gender_choice = [
        (Male, 'Male'),
        (Female,'Female'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=gender_choice,
        default=Male,
    )