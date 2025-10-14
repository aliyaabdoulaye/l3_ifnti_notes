from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.statistiques, name='statistiques'),
    path('<int:niveau_id>/', views.statistiques, name='statistiques_niveau'),
    path('enseignants', views.enseignants, name='enseignants'),
    path('note', views.note, name='notes'),
    path('eleves/', views.eleves, name='eleves'),
    path('eleve/<int:eleve_id>/', views.eleve, name='eleve'),
    path('matieres/', views.matieres, name='matieres'),
    path('matiere/<int:matiere_id>/', views.matiere, name='matiere'),
    path('niveau/<int:niveau_id>/', views.niveau, name='niveau'),
]
