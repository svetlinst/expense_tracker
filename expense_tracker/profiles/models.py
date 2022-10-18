from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from expense_tracker.profiles.validators import max_file_size_validator, only_letters_validator


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 15
    LAST_NAME_MAX_LENGTH = 15

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(2),
            only_letters_validator,
        ],
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(2),
            only_letters_validator,
        ],
        null=False,
        blank=False,
    )

    budget = models.FloatField(
        default=0,
        validators=[
            MinValueValidator(0),
        ],
        null=False,
        blank=False,
    )

    profile_image = models.ImageField(
        null=True,
        blank=True,
        validators=[
            max_file_size_validator,
        ],
        upload_to='uploads/',
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
