from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('obras/', views.obras, name='obras'),
    path('documentacao/1/', views.documentacao_1, name='documentacao-1'),
    path('documentacao/2/', views.documentacao_2, name='documentacao-2'),
    path('documentacao/3/', views.documentacao_3, name='documentacao-3'),
    path('documentacao/categorias/', views.documentacao_categorias, name='documentacao-categorias'),
    path('upload/', views.upload, name='upload'),
]