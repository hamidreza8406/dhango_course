from django.db import models
from django.shortcuts import reverse

class Post(models.Model):
    STATUS_CHOICES = {

        ('pub' , 'published'),
        ('drf' , 'draft'),
    }

    title = models.CharField(max_length=50)
    text = models.TextField()
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} : {self.title}"

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])













