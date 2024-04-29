from django.db import models
from stadium.models import Stadium
from user.models import User


class Booking(models.Model):
    status_choices = (
        (1, 'Active'),
        (2, 'Deactive'),
        (3, 'Delete'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_date = models.DateField(auto_now_add=True)
    status = models.SmallIntegerField(choices=status_choices, null=False, blank=False, default=1)

    def __str__(self):
        return self.stadium
