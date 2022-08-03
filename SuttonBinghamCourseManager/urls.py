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
    HelperCreateView, HelperDeleteView, HelperUpdateView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='home', permanent=True)),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('home/', views.home, name="home"),


    path('dingy-instructor/add', DingyInstructorCreateView.as_view(), name="DI-add"),
    path('dingy-instructor/delete/<int:pk>', DingyInstructorDeleteView.as_view(), name="DI-delete"),
    path('dingy-instructor/update/<int:pk>', DingyInstructorUpdateView.as_view(), name="DI-update"),

    path('assistant-instructor/add', AssistantInstructorCreateView.as_view(), name="AI-add"),
    path('assistant-instructor/delete/<int:pk>', AssistantInstructorDeleteView.as_view(), name="AI-delete"),
    path('assistant-instructor/update/<int:pk>', AssistantInstructorUpdateView.as_view(), name="AI-update"),

    path('helper/add', HelperCreateView.as_view(), name="helper-add"),
    path('helper/delete/<int:pk>', HelperDeleteView.as_view(), name="helper-delete"),
    path('helper/update/<int:pk>', HelperUpdateView.as_view(), name="helper-update"),
]
