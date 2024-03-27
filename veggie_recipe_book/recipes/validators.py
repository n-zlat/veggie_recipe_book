from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


def validate_image_size(value):
    max_image_size = 5 * 1024 * 1024

    if value.size > max_image_size:
        raise ValidationError(gettext_lazy('Image size should not exceed 5MB.'))
