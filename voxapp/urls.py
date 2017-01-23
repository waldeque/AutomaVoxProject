from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
#Criação das URLs relacionando-as às respectivas Views
urlpatterns = [
    url(r'^$', views.home), # A sequencia vazia '^$' indica que para a URL http://127.0.0.1:8000, deve-se ir para a view.home
    url(r'^cadastrar/$', views.cadastrar), # Para a URL '^cadastrar/$', deve-se ir para a view Cadastrar, onde teremos o cadastro do usuário no Sistema.
    url(r'^cadastrar_conta/$', views.cadastrar_conta),  #URL para o cadastro de contas no sistema
    url(r'^cadastrar_condominio/$', views.cadastrar_condominio), #URL para o cadastro de condominios no sistema
    url(r'^cadastrar_grupo/$', views.cadastrar_grupo), #URL para o cadastro de grupos de contas no sistema
    url(r'^cadastrar_inquilino/$', views.cadastrar_inquilino), #URL para o cadastro de inquilinos no sistema
    url(r'^login/$', views.logar), #URL para o login do usuário no Sistema.
    url(r'^home/$', views.home), # URL da página inicial do sistema.
    url(r'^incricaoevento/$', views.incricao_evento), # URL da página inscrição de usuário em evento.
    url(r'^relatorio/$', views.relatorio), # URL da página busca de eventos no Sistema.
    url(r'^logout/$', views.logout_view),
    url(r'^homeu/$', views.homeu),
    url(r'^erro/$', views.erro),
]
urlpatterns += staticfiles_urlpatterns()