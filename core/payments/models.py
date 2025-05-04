from django.db import models
from users.models import User
from decimal import Decimal

class Transactions(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'))
    payer = models.ForeignKey(User, on_delete=models.DO_NOTHING, editable=False)
    payee = models.ForeignKey(User, on_delete=models.DO_NOTHING, editable=False)
    date = models.DateTimeField(auto_now_add=True)
