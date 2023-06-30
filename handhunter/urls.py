
from django.contrib import admin
from django.urls import path
from core.views import *
from worker.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('about/', about),
    path('contacts/', contact_view),
    path('address/', address),
    path('vacancies/', vacancy_list),
    path("workers/", workers),
    path("worker/<int:id>/", worker_info),
    path("resume-list/", resume_list),
    path("resume-info/<int:id>/", resume_info),
    path("my-resume/", my_resume, name='my-resume'),
    path("vacancies-info/<int:id>/", vacancy_info),
]
