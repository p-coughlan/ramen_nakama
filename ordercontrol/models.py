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
        today = timezone.now().date()

        # 1) If the delivery date is today or in the past, just say closed
        if self.next_delivery_date and self.next_delivery_date <= today:
            return "Ordering is now closed."

        # 2) If ordering is still active (more than 48 hours before next_delivery_date)…
        if self.is_ordering_active:
            return (
                f"Place your order now for delivery on "
                f"{self.next_delivery_date.strftime('%B %d, %Y')}. "
                "Order processing will be closed 48 hours earlier."
            )

        # 3) If ordering is closed but there’s a future delivery date scheduled…
        if self.next_delivery_date:
            return (
                "Ordering is currently closed. Next delivery is scheduled for "
                f"{self.next_delivery_date.strftime('%B %d, %Y')}."
            )

        # 4) No next_delivery_date set at all
        return "Ordering is currently closed."
