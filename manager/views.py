from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from manager.forms import DingyInstructorForm, AssistantInstructorForm, \
    HelperForm, CourseForm
from manager.models import DingyInstructor, AssistantInstructor, Helper, \
    Course, DingyInstructorAvailability, Stage, AssistantInstructorAvailability


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
        return reverse("course-availability-add-DIs", args=[self.object.id])


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


def course_export_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    template = loader.get_template("course_export.html")
    context = {
        'title': "Add DIs",
        'course': Course.objects.get(id=pk),
    }
    return HttpResponse(template.render(context, request))


def availability_add_view(request, pk, staff_type, staff_availability):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == "GET":
            course = Course.objects.filter(id=pk)
            if not len(course) == 1:
                raise FileNotFoundError
            staffs = staff_type.objects.all()
            availabilities = staff_availability.objects.filter(
                course=pk)
            for availability in availabilities:
                print(availability.staff.id)
                staffs = staffs.exclude(id=availability.staff.id)

            template = loader.get_template("course_add_DIs.html")
            context = {
                'title': "Add DIs",
                'staffs': staffs,
                'course': course[0],
            }
            return HttpResponse(template.render(context, request))
        else:
            raw_staff = request.POST.getlist('instructors[]')
            course = Course.objects.filter(id=pk)[0]
            for staff_id in raw_staff:
                staff = staff_type.objects.filter(id=staff_id)[
                    0]
                # ensure this combination doesnt already exist!
                exiting_comb = staff_availability.objects \
                    .filter(course=course,
                            staff=staff)
                if len(exiting_comb) != 0:
                    continue

                # Add this availability record
                staff_availability.objects \
                    .create(course=course,
                            staff=staff,
                            assigned=False)
            return HttpResponseRedirect(reverse('course-availability-add-AIs',
                                                args=[course.id]))


def course_availability_add_DIs(request, pk):
    return availability_add_view(request, pk, DingyInstructor,
                                 DingyInstructorAvailability)


def course_availability_add_AIs(request, pk):
    return availability_add_view(request, pk, AssistantInstructor,
                                 AssistantInstructorAvailability)


class DIAvailabilityDeleteView(DeleteView):
    model = DingyInstructorAvailability
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse('course-detail', args=[self.kwargs['course_id']])


def course_detail_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    course = Course.objects.get(id=pk)
    stages = Stage.objects.filter(course=course.id)
    template = loader.get_template("course_detail.html")
    context = {
        'title': "View Course",
        'DI_availability': DingyInstructorAvailability.objects.filter(
            course=pk, assigned=False),
        'AI_availability': AssistantInstructorAvailability.objects.filter(
            course=pk, assigned=False),
        'course': course,
        'stages': stages
    }
    return HttpResponse(template.render(context, request))


class StageCreateView(CreateView):
    model = Stage
    fields = "__all__"
    template_name = "stage_create_form.html"

    def get_context_data(self, **kwargs):
        context = super(StageCreateView, self).get_context_data(**kwargs)
        context['course_id'] = self.kwargs['course_id']
        return context

    def get_success_url(self):
        return reverse("course-detail", args=[self.kwargs['course_id']])


class StageUpdateView(CreateView):
    model = Stage
    fields = "__all__"
    template_name = "stage_create_form.html"

    def get_context_data(self, **kwargs):
        context = super(StageUpdateView, self).get_context_data(**kwargs)
        context['course_id'] = self.kwargs['course_id']
        return context

    def get_success_url(self):
        return reverse("course-detail", args=[self.kwargs['course_id']])


class StageDeleteView(DeleteView):
    model = Stage
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super(StageDeleteView, self).get_context_data(**kwargs)
        context['course_id'] = self.kwargs['course_id']
        return context

    def get_success_url(self):
        return reverse("course-detail", args=[self.kwargs['course_id']])

    def form_valid(self, form, **kwargs):
        id = self.kwargs.get('pk')
        stage = Stage.objects.get(id=id)
        stage.dingyinstructoravailability_set.update(assigned=False,
                                                     stage=None)
        return super().form_valid(form)


def stage_add_DIs(request, course_id, stage_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == "GET":
            course = Course.objects.get(id=course_id)
            available_DIs = DingyInstructorAvailability.objects \
                .exclude(assigned=True) \
                .filter(course=course)

            template = loader.get_template("stage_add_DIs.html")
            context = {
                'title': "Add DIs",
                'DIs': available_DIs,
                'course': course,
            }
            return HttpResponse(template.render(context, request))
        else:
            raw_instructors = request.POST.getlist('instructors[]')
            course = Course.objects.get(id=course_id)
            for instructor_id in raw_instructors:
                instructor = DingyInstructor.objects.get(id=instructor_id)
                # ensure this combination doesnt already exist!
                DingyInstructorAvailability.objects \
                    .filter(course=course,
                            instructor=instructor) \
                    .update(assigned=True, stage=stage_id)

            return HttpResponseRedirect(reverse('course-detail',
                                                args=[course.id]))


def stage_return_DI(request, course_id, stage_id, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        DingyInstructorAvailability.objects.filter(id=pk).update(
            assigned=False,
            stage=None)
        return HttpResponseRedirect(reverse("course-detail", args=[course_id]))


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
