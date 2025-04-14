from datetime import datetime, timedelta, time
from django.db import models
from django.utils import timezone

class OrderWindow(models.Model):
    is_open = models.BooleanField(default=False)
    next_delivery_date = models.DateField(null=True, blank=True)

    def __str__(self):
        status = "Open" if self.is_ordering_active else "Closed"
        return f"Order Window ({status}) - Next Delivery: {self.next_delivery_date}"

    @property
    def is_ordering_active(self):
        # Check that ordering is enabled and a delivery date is set.
        if not self.is_open or not self.next_delivery_date:
            return False
        # Create a datetime for the delivery date at midnight and make it timezone-aware.
        cutoff_naive = datetime.combine(self.next_delivery_date, time())
        cutoff = timezone.make_aware(cutoff_naive) - timedelta(days=2)  # 48 hours before delivery.
        return timezone.now() < cutoff

    @property
    def ordering_message(self):
        if self.is_ordering_active:
            return (f"Orders are now open for delivery on {self.next_delivery_date.strftime('%B %d, %Y')}. "
                    "Order processing will be disabled 48 hours beforehand.")
        elif self.next_delivery_date:
            return (f"Ordering is currently closed. Next delivery is scheduled for "
                    f"{self.next_delivery_date.strftime('%B %d, %Y')}.")
        else:
            return "Ordering is currently closed."
