from django import forms

from manager.models import Experience, DingyInstructor, AssistantInstructor, \
    Helper, Course, DingyInstructorAvailability, Stage


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

    start_date = forms.DateField()


class DingyInstructorAvailabilityForm(forms.ModelForm):
    class Meta:
        model = DingyInstructorAvailability
        fields = "__all__"


class StageFrom(forms.ModelForm):
    class Meta:
        model = Stage
        fields =  "__all__"
