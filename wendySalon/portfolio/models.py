from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.conf import settings

class Portfolio(models.Model):
    title = models.CharField(max_length=20)
    context = models.CharField(max_length=100)
    img = models.ImageField(upload_to='portfolio/', null=False)
    created_date = models.DateTimeField("date created", default=timezone.now)
    # @admin.display(
    #     boolean=True,
    #     ordering="created_date",
    # )
    def __str__(self):
            return self.title