from django.db import models

# Create your models here.

class Room(models.Model):
    roomNo = models.IntegerField()

    def __str__(self) -> str:
        return str(self.roomNo)


class Guest(models.Model):
    name = models.CharField(max_length=25)
    room = models.OneToOneField(Room , on_delete=models.CASCADE )

    def __str__(self) -> str:
        return self.name