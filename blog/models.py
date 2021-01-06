from django.contrib.auth.models import User
from django.db import models

RATE = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]


class BlogPost(models.Model):
    title = models.CharField(max_length=100, null=False)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    content = models.TextField()
    rate = models.IntegerField(choices=RATE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog post'
        verbose_name_plural = 'Blog posts'


class Comment(models.Model):
    username = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False)
    text = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(to=BlogPost, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'Comment {self.id}- {self.username} - {self.post_id}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
