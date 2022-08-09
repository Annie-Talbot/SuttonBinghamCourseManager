from django.contrib import admin

from manager.models import DingyInstructor, AssistantInstructor, Helper, \
    Course, DingyInstructorAvailability, Stage


class DingyInstructorAdmin(admin.ModelAdmin):
    model = DingyInstructor
    list_display = ['id', 'name', 'experience']


class AssistantInstructorAdmin(admin.ModelAdmin):
    model = AssistantInstructor
    list_display = ['id', 'name', 'experience']


class HelperAdmin(admin.ModelAdmin):
    model = Helper
    list_display = ['id', 'name', 'experience']


class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ["id", "name", "start_date"]


class DingyInstructorAvailabilityAdmin(admin.ModelAdmin):
    model = DingyInstructorAvailability
    list_display = ["id", "course", "instructor", "assigned"]


class StageAdmin(admin.ModelAdmin):
    model = Stage
    list_display = ['id', 'name', 'no_kids']


admin.site.register(DingyInstructor, DingyInstructorAdmin)
admin.site.register(AssistantInstructor, AssistantInstructorAdmin)
admin.site.register(Helper, HelperAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(DingyInstructorAvailability,
                    DingyInstructorAvailabilityAdmin)
admin.site.register(Stage, StageAdmin)