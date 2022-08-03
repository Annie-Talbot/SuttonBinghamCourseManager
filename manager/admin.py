from django.contrib import admin

from manager.models import DingyInstructor, AssistantInstructor, Helper


class DingyInstructorAdmin(admin.ModelAdmin):
    model = DingyInstructor
    list_display = ['name', 'experience']


class AssistantInstructorAdmin(admin.ModelAdmin):
    model = AssistantInstructor
    list_display = ['name', 'experience']


class HelperAdmin(admin.ModelAdmin):
    model = Helper
    list_display = ['name', 'experience']


admin.site.register(DingyInstructor)
admin.site.register(AssistantInstructor)
admin.site.register(Helper)