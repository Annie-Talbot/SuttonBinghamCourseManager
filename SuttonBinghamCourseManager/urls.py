"""SuttonBinghamCourseManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from manager import views
from manager.views import DingyInstructorCreateView, DingyInstructorDeleteView, \
    DingyInstructorUpdateView, AssistantInstructorUpdateView, \
    AssistantInstructorDeleteView, AssistantInstructorCreateView, \
    HelperCreateView, HelperDeleteView, HelperUpdateView, CourseCreateView, \
    CourseDeleteView, CourseUpdateView, DIAvailabilityDeleteView, \
    StageCreateView, StageUpdateView, StageDeleteView, \
    AIAvailabilityDeleteView, HelperAvailabilityDeleteView

urlpatterns = [
    # General
    path('', RedirectView.as_view(pattern_name='home', permanent=True)),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('home/', views.home, name="home"),

    # Dingy Instructor Management
    path('dingy-instructor/add', DingyInstructorCreateView.as_view(),
         name="DI-add"),
    path('dingy-instructor/delete/<int:pk>',
         DingyInstructorDeleteView.as_view(), name="DI-delete"),
    path('dingy-instructor/update/<int:pk>',
         DingyInstructorUpdateView.as_view(), name="DI-update"),

    # Assistant Instructor Management
    path('assistant-instructor/add', AssistantInstructorCreateView.as_view(),
         name="AI-add"),
    path('assistant-instructor/delete/<int:pk>',
         AssistantInstructorDeleteView.as_view(), name="AI-delete"),
    path('assistant-instructor/update/<int:pk>',
         AssistantInstructorUpdateView.as_view(), name="AI-update"),

    # Helper Management
    path('helper/add',
         HelperCreateView.as_view(), name="helper-add"),
    path('helper/delete/<int:pk>',
         HelperDeleteView.as_view(), name="helper-delete"),
    path('helper/update/<int:pk>',
         HelperUpdateView.as_view(), name="helper-update"),

    # Course General Management
    path('course/add',
         CourseCreateView.as_view(), name="course-add"),
    path('course/<int:pk>/update',
         CourseUpdateView.as_view(), name="course-update"),
    path('course/<int:pk>/delete',
         CourseDeleteView.as_view(), name="course-delete"),
    path('course/<int:pk>/view',
         views.course_detail_view, name="course-detail"),
    path('course/<int:pk>/export',
         views.course_export_view, name="course-export"),

    # Course DI Availability Management
    path('course/<int:pk>/availability/DIs/add',
         views.course_availability_add_DIs,
         name="course-availability-add-DIs"),
    path('course/<int:course_id>/availability/DIs/remove/<int:pk>',
         DIAvailabilityDeleteView.as_view(),
         name="course-availability-remove-DI"),

    # Course AI Availability Management
    path('course/<int:pk>/availability/AIs/add',
         views.course_availability_add_AIs,
         name="course-availability-add-AIs"),
    path('course/<int:course_id>/availability/AIs/remove/<int:pk>',
         AIAvailabilityDeleteView.as_view(),
         name="course-availability-remove-AI"),

    # Course Helper Availability Management
    path('course/<int:pk>/availability/helpers/add',
         views.course_availability_add_helpers,
         name="course-availability-add-helpers"),
    path('course/<int:course_id>/availability/helpers/remove/<int:pk>',
         HelperAvailabilityDeleteView.as_view(),
         name="course-availability-remove-helper"),

    # Stage General Management
    path('course/<int:course_id>/stage/add',
         StageCreateView.as_view(), name='stage-create'),
    path('course/<int:course_id>/stage/<int:pk>/update',
         StageUpdateView.as_view(), name='stage-update'),
    path('course/<int:course_id>/stage/<int:pk>/delete',
         StageDeleteView.as_view(), name='stage-delete'),

    # Stage DI Management
    path('course/<int:course_id>/stage/<int:stage_id>/DIs/add',
         views.stage_add_DIs,
         name='stage-add-DIs'),
    path('course/<int:course_id>/stage/<int:stage_id>/DIs/<int:pk>/return',
         views.stage_return_DI,
         name='stage-return-DI'),

    # Stage AI Management
    path('course/<int:course_id>/stage/<int:stage_id>/AIs/add',
         views.stage_add_AIs,
         name='stage-add-AIs'),
    path('course/<int:course_id>/stage/<int:stage_id>/AIs/<int:pk>/return',
         views.stage_return_AI,
         name='stage-return-AI'),

    # Stage Helper Management
    path('course/<int:course_id>/stage/<int:stage_id>/helpers/add',
         views.stage_add_helpers,
         name='stage-add-helpers'),
    path('course/<int:course_id>/stage/<int:stage_id>/helpers/<int:pk>/return',
         views.stage_return_helper,
         name='stage-return-helper'),
]

handler404 = "manager.views.page_not_found_view"
