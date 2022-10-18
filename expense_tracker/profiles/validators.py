from django.core.exceptions import ValidationError


def only_letters_validator(value):
    for c in str(value):
        if not c.isalpha():
            raise ValidationError('Ensure this value contains only letters.')


def max_file_size_validator(value):
    limit = 5 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Max file size is 5.00 MB')
