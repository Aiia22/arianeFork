from django.db import models

# Create your models here.
class Entry(models.Model):
    name = models.CharField(max_length=42)
    comment = models.TextField()
    rate = models.IntegerField(default=5,choices=[(i, f'{i} stars') for i in range(1,6)]) ## 5 stars by default : becauce I like dark pattern!!!!

    def __str__(self) :
        return f"{self.name} ({self.rate} stars)"
    
     
