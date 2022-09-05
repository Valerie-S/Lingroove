from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # import the user database model


class SignUpForm(UserCreationForm):
    # class meta for options
    class Meta:
        # specify that we are using the user model
        model = User
        fields = ['username', 'password1', 'password2']
