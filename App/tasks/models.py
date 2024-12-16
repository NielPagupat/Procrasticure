from django.db import models
from App.users.models import CustomUser

# Create your models here.
class task(models.Model):
    task_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    taskname = models.TextField(max_length=255)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    reccurence = models.IntegerField(null=True)
    tags = models.TextField(null=False)

    def __str__(self):
        return "{}-{}".format(self.taskname)



