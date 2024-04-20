from django.urls import path
from todolist_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add_item, name='add_item'),
    path('toggle_complete/<int:item_id>/', views.toggle_complete, name='toggle_complete'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),

]

