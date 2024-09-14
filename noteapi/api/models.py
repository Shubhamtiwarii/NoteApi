from django.db import models

# Create your models here.


class Note(models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()