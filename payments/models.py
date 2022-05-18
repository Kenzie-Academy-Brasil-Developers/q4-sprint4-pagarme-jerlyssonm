import uuid
from django.db import models


class PaymentInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment_method = models.CharField(max_length=150)
    card_number = models.CharField(max_length=150)
    cardholders_name = models.CharField(max_length=150)
    card_expiring_date = models.DateField()
    cvv = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    customer = models.ForeignKey(
        "users.Users", on_delete=models.CASCADE, related_name="payments_infos", null=True
    )