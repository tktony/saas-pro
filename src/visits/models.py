from django.db import models

# Create your models here.
class PageVisit(models.Model):
    # this maps to the - db -> table
    # when we add new data to this it will be new rows
    # invisible colum = id -> primary key -> autofield -> 1,2,3,4,5
    path = models.TextField(blank=True, null=True) # column
    timestamp = models.DateTimeField(auto_now_add=True) # column
    pass