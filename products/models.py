from django.db import models
import uuid


class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    seller = models.ForeignKey(
        "users.Users",
        on_delete=models.CASCADE,
        related_name="products",
        null=True
    )
