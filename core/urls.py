from django.urls import path, include
from . import views  # Certifique-se de que 'views' está importado corretamente

urlpatterns = [
    path('', views.landing_page, name='landing_page'),

    path('painel/', views.painel_controle, name='painel_controle'),

    path('agendar/', views.agendar_visita, name='agendar_visita'),
    path('agendamentos/', views.lista_agendamentos, name='lista_agendamentos'),
    path('agendamentos/adicionar/', views.adicionar_agendamento, name='adicionar_agendamento'),
    path('agendamentos/<int:pk>/editar/', views.editar_agendamento, name='editar_agendamento'),
    path('agendamento-sucesso/', views.agendamento_sucesso, name='agendamento_sucesso'),
    path('agendamentos/<int:pk>/excluir/', views.excluir_agendamento, name='excluir_agendamento'),

    # URLs para gerenciamento de Banners
    path('banners/', views.lista_banners, name='lista_banners'),
    path('banners/adicionar/', views.adicionar_banner, name='adicionar_banner'),
    path('banners/<int:pk>/editar/', views.editar_banner, name='editar_banner'),  # URL para editar banner
    path('banners/<int:pk>/excluir/', views.excluir_banner, name='excluir_banner'),

    # URLs para gerenciamento de Seções de Ensino
    path('secoes/', views.lista_secoes, name='lista_secoes'),
    path('secoes/adicionar/', views.adicionar_secao, name='adicionar_secao'),
    path('secoes/<int:pk>/editar/', views.editar_secao, name='editar_secao'),  # URL para editar seção
    path('secoes/<int:pk>/excluir/', views.excluir_secao, name='excluir_secao'),
    # URL para excluir seçãoath('secoes/adicionar/', views.adicionar_secao, name='adicionar_secao'),

    # Projetos
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('projetos/<int:pk>/', views.detalhes_projeto, name='detalhes_projeto'),
    path('projetos/adicionar/', views.adicionar_projeto, name='adicionar_projeto'),
    path('projetos/<int:pk>/editar/', views.editar_projeto, name='editar_projeto'),
    path('projetos/<int:pk>/excluir/', views.excluir_projeto, name='excluir_projeto'),

    # URLs para gerenciamento de Agendamentos



]
