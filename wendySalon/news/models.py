from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=40)
    context = models.CharField(max_length=200)
    published_date = models.DateTimeField("date published", default=timezone.now)
    # 後台裝飾器
    @admin.display(
        boolean=True,
        ordering="published_date",
        # description="公佈日期",
    )
    def __str__(self):
            return self.title