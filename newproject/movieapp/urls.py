
from django.urls import path
from movieapp import views

urlpatterns = [
 
    # path('',views.print_hello),
    path('hello/',views.print_hello,name='hello'),
    path('details/<int:id>',views.detail,name="details"),
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    # path('delete/<int:id>',views.delete,name='delete')
    path('update/<int:id>',views.update,name='update')

]
