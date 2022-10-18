from django.db import models


class Expense(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        null=False,
        blank=False,
    )

    expense_image = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )