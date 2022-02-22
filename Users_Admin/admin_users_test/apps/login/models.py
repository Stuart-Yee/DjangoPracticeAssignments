from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("complete_order", "Can complete order"),
            ("view_orders", "Can view all orders"),
        ]

