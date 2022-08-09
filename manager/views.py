from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from manager.forms import DingyInstructorForm, AssistantInstructorForm, \
    HelperForm, CourseForm
from manager.models import DingyInstructor, AssistantInstructor, Helper, \
    Course, DingyInstructorAvailability


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        template = loader.get_template("home.html")
        instructors = DingyInstructor.objects.all()
        assistants = AssistantInstructor.objects.all()
        helpers = Helper.objects.all()
        courses = Course.objects.all()
        context = {
            'title': "Home",
            'instructors': instructors,
            'assistants': assistants,
            'helpers': helpers,
            'courses': courses
        }
        return HttpResponse(template.render(context, request))


class DingyInstructorCreateView(CreateView):
    model = DingyInstructor
    template_name = "staff_create_form.html"
    fields = ['name', 'experience']
    success_url = "/home/"


class DingyInstructorDeleteView(DeleteView):
    model = DingyInstructor
    success_url = "/home/"
    pk_url_kwarg = 'pk'


class DingyInstructorUpdateView(UpdateView):
    model = DingyInstructor
    template_name = "staff_update_form.html"
    success_url = "/home/"
    pk_url_kwarg = 'pk'
    form_class = DingyInstructorForm


class AssistantInstructorCreateView(CreateView):
    model = AssistantInstructor
    template_name = "staff_create_form.html"
    fields = ['name', 'experience']
    success_url = "/home/"


class AssistantInstructorDeleteView(DeleteView):
    model = AssistantInstructor
    success_url = "/home/"
    pk_url_kwarg = 'pk'


class AssistantInstructorUpdateView(UpdateView):
    model = AssistantInstructor
    template_name = "staff_update_form.html"
    success_url = "/home/"
    pk_url_kwarg = 'pk'
    form_class = AssistantInstructorForm


class HelperCreateView(CreateView):
    model = Helper
    template_name = "staff_create_form.html"
    fields = ['name', 'experience']
    success_url = "/home/"


class HelperDeleteView(DeleteView):
    model = Helper
    success_url = "/home/"
    pk_url_kwarg = 'pk'


class HelperUpdateView(UpdateView):
    model = Helper
    template_name = "staff_update_form.html"
    success_url = "/home/"
    pk_url_kwarg = 'pk'
    form_class = HelperForm


class CourseCreateView(CreateView):
    model = Course
    fields = "__all__"
    template_name = "course_create_form.html"

    def get_success_url(self):
        return reverse("course-add-DIs", args=[self.object.id])


class CourseDeleteView(DeleteView):
    model = Course
    success_url = "/home/"
    pk_url_kwarg = 'pk'


class CourseUpdateView(UpdateView):
    model = Course
    template_name = "course_create_form.html"
    pk_url_kwarg = 'pk'
    form_class = CourseForm

    def get_success_url(self):
        return reverse("course-availability-add-DIs", args=[self.object.id])


def course_availability_add_DIs(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == "GET":
            course = Course.objects.filter(id=pk)
            if not len(course) == 1:
                raise FileNotFoundError
            DIs = DingyInstructor.objects.all()
            print(list(DIs))
            availabilities = DingyInstructorAvailability.objects.filter(
                course=pk)
            for availability in availabilities:
                print(availability.instructor.id)
                DIs = DIs.exclude(id=availability.instructor.id)

            template = loader.get_template("course_add_DIs.html")
            context = {
                'title': "Add DIs",
                'DIs': DIs,
                'course': course[0],
            }
            return HttpResponse(template.render(context, request))
        else:
            raw_instructors = request.POST.getlist('instructors[]')
            course = Course.objects.filter(id=pk)[0]
            for instructor_id in raw_instructors:
                instructor = DingyInstructor.objects.filter(id=instructor_id)[0]
                # ensure this combination doesnt already exist!
                exiting_comb = DingyInstructorAvailability.objects \
                    .filter(course=course,
                            instructor=instructor)
                if len(exiting_comb) != 0:
                    continue

                # Add this availability record
                DingyInstructorAvailability.objects \
                    .create(course=course,
                            instructor=instructor,
                            assigned=False)
            return HttpResponseRedirect(reverse('course-detail',
                                                args=[course.id]))


class DIAvailabilityDeleteView(DeleteView):
    model = DingyInstructorAvailability
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse('course-detail', args=[self.kwargs['course_id']])


def course_detail_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    course = Course.objects.get(id=pk)
    template = loader.get_template("course_detail.html")
    context = {
        'title': "View Course",
        'DI_availability': DingyInstructorAvailability.objects.filter(
            course=pk, assigned=False),
        'course': course,
    }
    return HttpResponse(template.render(context, request))


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
