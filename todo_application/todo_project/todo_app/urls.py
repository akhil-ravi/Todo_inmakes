from django.urls import path
from . import views

detail= 'detail'

urlpatterns = [
    path('',views.index,name='index'),
    path('delete<int:taskid>/',views.delete,name='delete'),
    path('update<int:id>/',views.update, name='update'),
    path('task/',views.task_1.as_view(),name='task'),
    path('detail/<int:pk>/',views.detail.as_view(),name='detail'),
    path('class_update/<int:pk>/',views.update_class.as_view(),name='update_class'),
    path('class_delete/<int:pk>/',views.delete_class.as_view(),name='delete_class'),
]