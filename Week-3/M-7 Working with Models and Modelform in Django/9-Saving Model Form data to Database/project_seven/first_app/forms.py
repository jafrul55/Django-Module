from django import forms
from first_app.models import StudentModel


class StudentForms(forms.ModelForm):
    # create a meta class:
    class Meta:
        model = StudentModel
        fields = '__all__'
        # If you want to specifically show field:
        # fields = ['name', 'roll']

        # We use 'exclude' if we want to all values instead of exclude value
        # when we use field that time we never use exclude
        # exclude = ['roll']
        # use labels to label field
        labels = {
            'name': 'Student Name',
            'roll': "Student Roll"
        }
        # To use button for name field:
        widgets = {
            'name': forms.TextInput(),
        }

        help_texts = {
            'name': "Write your full name"
        }

        error_messages = {
            'name': {'required': 'Your name is required'}
        }
