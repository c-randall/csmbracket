from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('master/', views.masterpage, name='master'),
    path('standings/<str:show_img>/<int:sort>', views.standingspage, name='standings'),
    path('submission/', views.submissionpage, name='submission'),
]
