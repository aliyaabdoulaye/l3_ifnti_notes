import os
import django, random


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ifnti_l3.settings')

django.setup()

#from django.conf import settings


from notes.models import Eleve, Niveau

Niveau.objects.all().delete()
Eleve.objects.all().delete()



for i in range(1,4):
    Niveau.objects.create(
        nom = f"L{i}",

    )


for i in range(1, 11):
    Eleve.objects.create(
        matricule = f"MATRICULE {i}",
        nom = f"Nabila {i}",
        prenom = f"Tamba {i}",
        sexe = "F",
        date_naissance = "2000-11-12",
        niveau = random.choice(Niveau.objects.all())
    )

