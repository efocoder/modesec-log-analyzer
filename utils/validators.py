from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def file_extension_validator(value):
    print(value.path.lower().endswith('.log'))
    print("########################")
    if not value.path.lower().endswith('.log'):
        raise ValidationError(
            _('file uploaded is not valid')
        )


