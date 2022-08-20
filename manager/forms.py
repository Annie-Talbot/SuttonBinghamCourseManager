from django import forms
from django.forms import DateInput

from manager.models import Experience, DingyInstructor, AssistantInstructor, \
    Helper, Course, DingyInstructorAvailability, Stage, \
    AssistantInstructorAvailability


class DingyInstructorForm(forms.ModelForm):
    class Meta:
        model = DingyInstructor
        fields = '__all__'


class AssistantInstructorForm(forms.ModelForm):
    class Meta:
        model = AssistantInstructor
        fields = '__all__'


class HelperForm(forms.ModelForm):
    class Meta:
        model = Helper
        fields = '__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
        }


class DingyInstructorAvailabilityForm(forms.ModelForm):
    class Meta:
        model = DingyInstructorAvailability
        fields = "__all__"


class AssistantInstructorAvailabilityForm(forms.ModelForm):
    class Meta:
        model = AssistantInstructorAvailability
        fields = "__all__"


class StageFrom(forms.ModelForm):
    class Meta:
        model = Stage
        fields = "__all__"
