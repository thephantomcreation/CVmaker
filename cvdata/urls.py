from django.urls import path
from . import views
from cvdata.views import *
app_name = "cvdata"


urlpatterns = [

    
    path('', CVDataView.as_view(),name= 'cv' ),
    path('test/', views.html_to_pdf_view, name = 'test'),
]