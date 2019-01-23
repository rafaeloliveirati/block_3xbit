from django import forms

from block_3xbit.models import User


class LoginForm(forms.Form):
    class Meta:
        model = User
        # Campos que estarão no form
        fields = [
            'email',
            'password'
        ]
