from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy


class UsernameValidator(RegexValidator):
    regex = r'^[\w-]+$'
    message = gettext_lazy(
        'Username can only contain Latin alphabet letters, numbers, underscore (_), and hyphen (-)!'
    )
    flags = 0
