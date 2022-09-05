from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User  # import the user database model


# use the Django pre-built register form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # class meta for options
    class Meta:
        # specify that we are using the user model
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': "150 characters or fewer. Letters, digits and @/./+/-/_ only.",
            'email': "",
            'password1': "Your password can’t be too similar to your other personal information. \
                Your password must contain at least 8 characters. \
                Your password can’t be entirely numeric.",
            'password2': "",
        }

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
