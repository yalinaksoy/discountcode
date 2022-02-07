from django.urls import path
from billogram.api.views import create_view, get_view


urlpatterns = [
    path('create/', create_view, name='api_view'),
    path('get/', get_view, name='api_view'),
]
