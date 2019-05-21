from django.db import models


class Board(models.Model):
    message = models.TextField()
    writer = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    

    def __str__(self): # 제목을 message로 해주기 위해서는 필수
        return self.message
    
# Create your models here.
