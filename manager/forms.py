from django import forms

from manager.models import Experience, DingyInstructor, AssistantInstructor, \
    Helper


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