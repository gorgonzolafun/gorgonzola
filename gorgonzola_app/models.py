from django.db import models
from datetime import datetime


class Log(models.Model):

    status = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=datetime.utcnow)

