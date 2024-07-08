from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Company(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    industry = models.CharField(max_length=255)
    size_range = models.CharField(max_length=50)
    locality = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    linkedin_url = models.URLField()
    current_employee_estimate = models.IntegerField()
    total_employee_estimate = models.IntegerField()
    # add more fields as per the csv file
    #not able to add fields from provided csv file because file is not opening.

    def __str__(self):
        return self.name