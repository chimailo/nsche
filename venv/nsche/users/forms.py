from __future__ import unicode_literals
from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from datetime import date
from django.contrib.auth.hashers import (
    UNUSABLE_PASSWORD_PREFIX, identify_hasher,
)
from .models import CustomUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField, SetPasswordForm


class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the required fields.
    """
    
    password = forms.CharField(label=("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
        )
   
    class Meta:
        model = CustomUser
        fields = ('matric_no', 'surname', 'first_name', 'other_name', 'email', 'part', 'bio',)


    def clean_password(self):
        password = self.cleaned_data.get("password")
        #password2 = self.cleaned_data.get("password2")
        if len(password) < 8:
            raise forms.ValidationError('Password length should be at least 8 characters long.')
        self.instance.matric_no = self.cleaned_data.get('matric_no')
        self.instance.email = self.cleaned_data.get('email')
        self.instance.surname = self.cleaned_data.get('surname')
        self.instance.first_name = self.cleaned_data.get('first_name')
        self.instance.other_name = self.cleaned_data.get('other_name')
        password_validation.validate_password(self.cleaned_data.get('password'), self.instance)
        return password

    def clean_matric_no(self):
        matric_no = self.cleaned_data['matric_no']
        dept, yr, s_no = matric_no.split('/')
        prefix = dept.upper()
        if int(s_no) > 150:
            raise forms.ValidationError('Your matric number should be in the range 1 - 150')
        if (prefix != 'CHE'):
            raise forms.ValidationError('Your matric number should start with \'che\'')
        if int(yr) > date.today().year:
            raise forms.ValidationError('Enter a valid matric number')
        return matric_no


    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
        	user.is_active = False
        	user.save()
        return user


class UserProfileForm(forms.ModelForm):

    image = forms.ImageField(error_messages={'invalid':'image files only'}, widget=forms.FileInput)

    class Meta:
        model = CustomUser
        fields = ('surname', 'first_name', 'other_name', 'email', 'part',
                    'gender', 'phone', 'birth_date', 'image', 'bio',
        )
        widgets = {'birth_date': forms.DateInput(attrs={'class':'datepicker', 'type':'date'}),
                   'image': forms.ClearableFileInput(attrs={'type':'file'}),
                   'bio': forms.Textarea(attrs={'class':'materialize-textarea',
                                                'placeholder':'Tell us about your office, function, experience'}),
        }


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label=("Password"),
        help_text=("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"../password/\">this form</a>."))

    class Meta:
        model = CustomUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions')
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
