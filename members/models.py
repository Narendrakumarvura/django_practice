from django.db import models

class Member(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    joined_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"