from django.urls import path
from .views import nosotras_view
app_name = 'nosotras'

urlpatterns = [
    path('', nosotras_view, name='nosotras'),
]