from django.urls import path, include
from .views import landing_page, GetTest

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('test/', GetTest.as_view(), name='test'),
]