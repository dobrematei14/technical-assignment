from django.db import models
import uuid


class DataEntry(models.Model):
    url = models.URLField()  # string0
    datetime = models.DateTimeField()  # string1
    category = models.CharField(max_length=100, blank=True, null=True)  # string2
    postal_code = models.CharField(max_length=20)  # string3
    additional_info = models.CharField(max_length=100, blank=True, null=True)  # string4
    numeric_data = models.CharField(max_length=100, blank=True, null=True)  # string5
    external_id = models.CharField(max_length=100, blank=True)  # string6
    grade = models.CharField(max_length=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - Grade: {self.grade}"
