from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now)
    # Optional: A boolean if you wish to have a "featured" marker
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title
