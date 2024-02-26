
from django.urls import path
from movieapp import views

urlpatterns = [
 
    # path('',views.print_hello),
    path('hello',views.print_hello),
    path('details/<int:id>',views.detail,name="details"),
    

]
