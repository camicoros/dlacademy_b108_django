from django.db import models

from core.models import CustomUser


'''
! не забываем добавить posts в INSTALLED_APPS в settings.py
'''


def post_image_path(instance, filename):
    user_id = instance.id
    return "posts/user-{}/{}".format(user_id, filename)


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    description = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to=post_image_path)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(CustomUser, related_name='users_like_it', blank=True)

    @property
    def like_count(self):
        return self.likes.count()

    def __str__(self):
        return "Post from {} with #{}".format(self.author, self.id)
