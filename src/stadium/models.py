from django.db import models


class Stadium(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    booking_price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class StadiumImage(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='stadium_images')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.image
