from django.db import models

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField('date published')
    def __str__(self):
    	return self.title

class Contact(models.Model):
  Name = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  Message = models.CharField(max_length=200)
  def __str__(self):
    return self.Name
class Projects(models.Model):
  ProjectName = models.CharField(max_length=100)
  technologies = models.CharField(max_length=200) 
  details = models.CharField(max_length=200) 
  def __str__(self):
    return self.ProjectName
