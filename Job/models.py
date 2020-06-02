from django.db import models

# Create your models here.
'''
django model field:
    -html widget
    -validation
    -db size

'''

JOB_TYPE = (
    ('Full time', 'Full time'),
    ('Part time', 'Part time'),

)


class Job(models.Model):  # tables
    title = models.CharField(max_length=100)  # column
    #location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=12, choices=JOB_TYPE)
    descriptions = models.TextField(max_length=1000)
    published = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title
