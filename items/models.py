from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length = 64)
    description = models.TextField()
    enrolled_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    entry_clerk = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    price = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.name
