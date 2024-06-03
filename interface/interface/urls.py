from django.urls import path, include


urlpatterns = [
    path('', include('core.urls')),
    path('api/v1', include('api.urls'))
]
