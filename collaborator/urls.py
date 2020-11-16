from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('organizational_chart/', views.organizational_chart, name='orga'),
    path('development_modules/', views.development_modules, name='dev_mod'),
    path('collective_initiatives/', views.collective_initiative, name='collec_init'),
    path('new_project', views.new_project, name='new_project'),
    path('other_projects/', views.other_projects, name='other_projects'),
    path('project/<int:project_id>', views.project, name='project'),
    path('change_values/<int:project_id>', views.change_values, name='change_values'),
    path('show_member/<int:role_id>', views.show_member, name="show_member"),
    path('ask_money/<int:project_id>', views.ask_money, name='ask_money'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('barometers/', views.barometers, name='baro'),
    path('help/', views.help, name='help'),
]
