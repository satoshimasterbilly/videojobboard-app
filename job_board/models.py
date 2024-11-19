from django.db import models

class JobPosting(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=255)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} | {self.company} | Active: {self.is_active}"

# makemigrations
## -> create instructions telling django how the db have changed
# migrate
## -> apply the changes to the db

################################
# CRUD operations
# Create
# Read
# Update
# Delete

# model manager -> JobPosting.objects
# model instance -> JobPosting.objects.get(id=1)
# model instance -> JobPosting.objects.filter(id=1)#
# model instance -> JobPosting.objects.all()
