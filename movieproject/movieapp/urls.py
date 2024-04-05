
from django.urls import path
from . import views

app_name='movieapp'
urlpatterns = [

    path('',views.index,name='index'),
    # path('movies/<int:movie_id>/',views.id,name='id'),
    path('<int:movie_id>/',views.details,name='details'),
    path('movies/',views.link,name='link'),
    path('add/',views.add, name='add'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),

]