from django.db import models
from django.utils import timezone # timezone will enable use to have a date that updated when we want to 
from django.contrib.auth.models import User

# Create your models here.
# Remember Django created the user model so we wont define it under Posts class. We will import it

class Post(models.Model):
 title = models.CharField(max_length= 100)
 content = models.TextField()
 date_posted= models.DateTimeField(default=timezone.now) 
 author = models.ForeignKey(User, on_delete= models.CASCADE) # on delete= models.CASCADE. This means that if a user is deleted, all of his/ her posts will be deleted as well.

 def __str__(self):
  return self.title
  