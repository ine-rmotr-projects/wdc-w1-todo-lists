from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User


class List(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

    def owned_by(self, user):
        return user == self.user


class Item(models.Model):

    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text

    def owned_by(self, user):
        return user == self.list.user
