from django.db import models

# Create your models here.


class VectorLayer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='vectors/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name