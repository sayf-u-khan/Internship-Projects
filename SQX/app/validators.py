# Defining the custom password validation class

import os
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 8:
            raise ValidationError(_('Password must be at least 8 characters.'))
        if not any(char.isdigit() for char in password):
            raise ValidationError(_('Password must contain at least one digit.'))
        if not any(char.isupper() for char in password):
            raise ValidationError(_('Password must contain at least one uppercase letter.'))
        if not any(char.islower() for char in password):
            raise ValidationError(_('Password must contain at least one lowercase letter.'))
        if not any(char in '!@#$%^&*()-_=+[]{};:,.<>?/' for char in password):
            raise ValidationError(_('Password must contain at least one special character.'))

    def get_help_text(self):
        return _('Your password must contain at least 8 characters, one digit, one uppercase letter, one lowercase letter, and one special character.')
    
# Picture format validator

def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1]  # get the extension
    valid_extensions = ['.jpg', '.jpeg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError(_('Unsupported file extension.'))