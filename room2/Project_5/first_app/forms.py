from django import forms
from django.core import validators

# widgets == field to html input
class contactForm(forms.Form):
    name = forms.CharField(label= "Full Name : ", initial = "Rahim", help_text= "Total length must be between 70 charecters.", required=False, widget=forms.Textarea(attrs= {'id': 'text_area', 'class': 'class1 class2', 'placeholder': 'Enter full name'}))
    # file = forms.FileField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    email = forms.EmailField(label= "User Email")
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs= {'type': 'date'}))
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs= {'type': 'datetime-local'}))
    CHOICES = [('S',"Small"), ("M","Medium"), ("L","Large")]
    size = forms.ChoiceField(choices = CHOICES, widget=forms.RadioSelect)
    MEAL = [('P', 'Pepperoni'),('M', 'Meat'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices = MEAL, widget=forms.CheckboxSelectMultiple)

# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.EmailField(widget=forms.EmailInput)
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("Name is too short")
#     #     return valname
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Email is not valid")
#     #     return valemail
#     def clean(self):
#         cleaned_data = super().clean()
#         name = cleaned_data.get('name')
#     #   name = self.cleaned_data['name']
#         email = cleaned_data.get('email')
#         if len(name) < 10:
#             raise forms.ValidationError("Name is too short")
#             return name
#         if '.com' not in email:
#             raise forms.ValidationError("Email is not valid")
#         return cleaned_data

def len_chek(value):
    if len(value) < 10:
        raise forms.ValidationError("Text is too short")

class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10,message='Enter a valid name')])
    text = forms.CharField(widget=forms.TextInput, validators=[len_chek])
    email = forms.EmailField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a valid email')])
    age = forms.IntegerField(validators=[validators.MinValueValidator(18,message='Enter a valid age')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'], message='Only JPG and PNG files are allowed')])

class passwordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        val_name = cleaned_data.get('name')
        if password != confirm_password:
            raise forms.ValidationError("Password does not match")
        if len(val_name) < 15:
            raise forms.ValidationError("Name is too short")
