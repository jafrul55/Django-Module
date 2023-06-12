from django import forms
from django.core import validators

# widgets == Field to html input
class contactForm(forms.Form):
    # name = forms.CharField(label = "Full Name : ",initial="Jafrul",help_text="Total length must be within 70 characters",required=False,disabled=True)
    name = forms.CharField(label = "Full Name : ",
    help_text="Total length must be within 70 characters",required=False,widget=forms.Textarea(attrs= {'id': 'text_area', 'class': 'class1, class2','placeholder': 'Enter your Name'}))
    # file = forms.FileField(label= "File : ")
    email = forms.EmailField(label="User Email : ")
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # age = forms.IntegerField()
    # We can work easily all types of number:
    age = forms.CharField(widget=forms.NumberInput)
    Check = forms.BooleanField()
    Birthday = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    CHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=CHOICES, widget= forms.RadioSelect)
    MEAL = [('P','Pepperoni'),('M','Mashroom'),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices= MEAL,widget= forms.CheckboxSelectMultiple)
    
# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
    #     return valname
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("You email must contain .com")
    
    
# Without using lot of function we can use a single function to work with all field
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
        
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must contain .com")
    
# Inside BuiltIn function we can use our created function also:
def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter at least 10 characters")

# 10 Builtin Form Validators:
class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10,message="Enter name with at least 10 characters")])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid Email")])
    # Inside BuiltIn function we can use our created function also:
    Text = forms.CharField(widget= forms.TextInput,validators=[len_check])
    age = forms.IntegerField(validators=[validators.MinValueValidator(18, message="Age must be at least 18"),validators.MaxValueValidator(34,message="Age must be maximum 34")])
    #We can also take file as pdf:
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'],message="file must be PDF format")])  
    

# Password Validation project:
class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget= forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    # For use multiple field to do validation:
    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        val_pass = self.cleaned_data['password']
        val_confirm_pass = self.cleaned_data["confirm_password"]
        if val_pass != val_confirm_pass:
            raise forms.ValidationError("Password didn't match")
        
        if len(valname) < 10:
            raise forms.ValidationError("Enter at least 10 characters")
            
    
