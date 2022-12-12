import uuid
from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    phoneNo = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    address = models.CharField(max_length=100)
    id = models.UUIDField(unique=True, default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

