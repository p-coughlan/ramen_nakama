from django.db import models

# Create your models here.
class OrderWindow(models.Model):
    is_open = models.BooleanField(default=False)
    next_delivery_date = models.DateField(null=True, blank=True)

    def __str__(self):
        status = "Open" if self.is_open else "Closed"
        return f"Order Window ({status}) - Next Delivery: {self.next_delivery_date}"