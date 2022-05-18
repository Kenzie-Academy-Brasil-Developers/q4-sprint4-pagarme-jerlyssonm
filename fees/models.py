from django.db import models
import uuid


class Fees(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    credit_fee = models.FloatField()
    debit_fee = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)