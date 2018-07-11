from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('place/<int:place_id>', views.place,name='place'),
    path('suggestion/<int:place_id>', views.suggestion, name='suggestion'),
]