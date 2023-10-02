from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from .models import CustomUser, AreaOfOperation, EndOfOperationArea, Driver

class LearnerRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text="Your preferred name.")
    last_name = forms.CharField(max_length=30, required=True, help_text="Required.")
    email = forms.EmailField(max_length=254, required=True, help_text="Enter a valid email address.")
    school = forms.CharField(max_length=70, required=True, help_text="Enter your school name.")
    age = forms.IntegerField(min_value=4, max_value=18, required=True, help_text="Enter your age.")
    my_driver = forms.ModelChoiceField(queryset=Driver.objects.all(), required=True, empty_label="Select Your Driver")

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 4 or age > 18:
            raise ValidationError("Age must be between 4 and 18.")
        return age

    class Meta:
        model = CustomUser
        fields = ('first_name','last_name', 'school', 'age', 'email', 'my_driver','username', 'password1', 'password2')

class DriverRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text="Your preferred name.")
    last_name = forms.CharField(max_length=30, required=True, help_text="Required.")
    email = forms.EmailField(max_length=254, required=True, help_text="Enter a valid email address.")
    age = forms.IntegerField(min_value=18, required=True, help_text="Enter your age.")
    phone_number = forms.CharField(max_length=10, help_text="No spaces. Should be a 10-digit number.")
    number_plate = forms.CharField(max_length=10, help_text="Desired format: alpha-numerics provice tag, i.e <br/> '<i>AA0011GP</i>' Or '<i>AAA000EC</i>'")
    my_pick_up_area = forms.ModelChoiceField(queryset=AreaOfOperation.objects.all(), empty_label="Select Your Pick-up Point")
    my_drop_off_area = forms.ModelChoiceField(queryset=EndOfOperationArea.objects.all(), empty_label="Select Your Drop-off Destination")

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number', 'age', 'email', 'my_pick_up_area', 'my_drop_off_area', 'number_plate', 'username', 'password1', 'password2')
