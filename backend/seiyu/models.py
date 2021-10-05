from django.db import models

class Seiyu(models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='images/', null=True, blank=True)
  
  def __str__(self):
      return self.name
    
  
