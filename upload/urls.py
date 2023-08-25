from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.goes,name='goes'),
    path('allfiles',views.allfiles,name='allfiles'),
    path('modify/<int:id>',views.modify,name='modify')
    
]