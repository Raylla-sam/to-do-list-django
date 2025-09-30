from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('lista/', views.lista, name='lista_de_tarefas'),
    path('new/', views.create, name='form_add'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('register/', views.register, name='register'),
    path('', CustomLoginView.as_view(), name='login'),
]
