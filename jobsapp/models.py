from django.db import models
from django.utils import timezone

from accounts.models import User

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    location = models.CharField(max_length=150,blank=True,null=True)
    type = models.CharField(choices=JOB_TYPE, max_length=50,blank=True,null=True)
    category = models.CharField(max_length=100,blank=True,null=True)
    last_date = models.DateTimeField(blank=True,null=True)
    company_name = models.CharField(max_length=100,blank=True,null=True)
    company_description = models.TextField(blank=True,null=True)
    website = models.CharField(max_length=100, blank=True,null=True)
    created_at = models.DateTimeField(default=timezone.now)
    filled = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.get_full_name()