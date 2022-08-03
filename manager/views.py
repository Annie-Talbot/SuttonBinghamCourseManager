from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from manager.forms import DingyInstructorForm, AssistantInstructorForm, \
    HelperForm
from manager.models import DingyInstructor, AssistantInstructor, Helper


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        template = loader.get_template("home.html")
        instructors = DingyInstructor.objects.all()
        assistants = AssistantInstructor.objects.all()
        helpers = Helper.objects.all()
        context = {
            'title': "Home",
            'instructors': instructors,
            'assistants': assistants,
            'helpers': helpers,
        }
        return HttpResponse(template.render(context, request))


class DingyInstructorCreateView(CreateView):
    model = DingyInstructor
    template_name = "dingyinstructor_create_form.html"
    fields = ['name', 'experience']
    success_url = "/home/"


class DingyInstructorDeleteView(DeleteView):
    model = DingyInstructor
    success_url = "/home/"
    pk_url_kwarg = 'pk'


class DingyInstructorUpdateView(UpdateView):
    model = DingyInstructor
    template_name = "dingyinstructor_update_form.html"
    success_url = "/home/"
    pk_url_kwarg = 'pk'
    form_class = DingyInstructorForm


class AssistantInstructorCreateView(CreateView):
    model = AssistantInstructor
    template_name = "dingyinstructor_create_form.html"
    fields = ['name', 'experience']
    success_url = "/home/"


class AssistantInstructorDeleteView(DeleteView):
    model = AssistantInstructor
    success_url = "/home/"
    pk_url_kwarg = 'pk'


class AssistantInstructorUpdateView(UpdateView):
    model = AssistantInstructor
    template_name = "dingyinstructor_update_form.html"
    success_url = "/home/"
    pk_url_kwarg = 'pk'
    form_class = AssistantInstructorForm


class HelperCreateView(CreateView):
    model = Helper
    template_name = "dingyinstructor_create_form.html"
    fields = ['name', 'experience']
    success_url = "/home/"


class HelperDeleteView(DeleteView):
    model = Helper
    success_url = "/home/"
    pk_url_kwarg = 'pk'


class HelperUpdateView(UpdateView):
    model = Helper
    template_name = "dingyinstructor_update_form.html"
    success_url = "/home/"
    pk_url_kwarg = 'pk'
    form_class = HelperForm
