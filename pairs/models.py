from django.db import models

# Create your models here.
import uuid

class KVPairTable(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)
    uuid_val = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)