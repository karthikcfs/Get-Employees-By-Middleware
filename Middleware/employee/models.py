from django.db import models

# Create your models here.

class emp(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    emp_id = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)

