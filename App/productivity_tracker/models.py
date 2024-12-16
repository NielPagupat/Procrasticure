from django.db import models
from App.users.models import CustomUser
# Create your models here.
class productivityTimer(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    taskname = models.CharField(max_length=255, null=True)
    timeStart = models.TimeField(null=True)
    timeEnd = models.TimeField(null=True)
    date = models.DateField(null=True)
    report = models.CharField(max_length=255)

    def __str__(self):
        return '{}-{}'.format(self.taskname, self.owner)