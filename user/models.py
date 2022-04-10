import uuid

from django.contrib.auth.models import User
from django.db import models


class CustomUser(User):
    uuid = models.UUIDField(editable=False, db_index=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, default='')
    num_mozcoins = models.PositiveIntegerField(default=0, db_index=True)
    level = models.PositiveIntegerField(default=1, db_index=True)
