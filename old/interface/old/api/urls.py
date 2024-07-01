from django.urls import path
from .views import *


urlpatterns = [
    path('project', project),
    path('sprint', sprint),
    path('iteration', iteration),
    path('log', log)
]
