from django.db import models
from acc.models import User
# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    comment = models.TextField(blank=True)
    url = models.TextField(blank=True)

    def __str__(self):
        return f"이름 :{self.site_name}, 주소 :{self.url}"