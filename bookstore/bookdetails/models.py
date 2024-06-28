from django.db import models

# Create your models here.
class Blog(models.Model):
    post_title=models.CharField(max_length=255)
    post_details=models.TextField()
    post_dates=models.DateField(auto_now_add=True)
    post_updated=models.DateField(auto_now=True)

    def __str__(self):
        return self.post_title
    