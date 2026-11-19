from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='lista_de_tarefas'),
    path('new/', views.create, name='form_add'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.task_list, name="task_list"),
#     path("new/", views.create, name="form_add"),  # para o botão "Nova Tarefa"
# ]
