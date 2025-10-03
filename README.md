#  Application de gestion de notes - Django IFNTI

Application web de gestion de notes d'étudiants développée dans le cadre des TPs Django à l'IFNTI Sokodé.

---

## Fonctionnalités
- Gestion des élèves, enseignants et matières
- Attribution et consultation des notes
- Interface d'administration complète (Django Admin)
- Navigation entre les différentes pages

---

## Technologies utilisées
- Python **3.12.3**
- Django **5.2.6**
- Postgresql **14**

---

## Installation

1. **Cloner le repository**
   ```bash
   git clone https://github.com/aliyaabdoulaye/l3_ifnti_notes.git
   cd l3_ifnti_notes
````

2. **Créer et activer un environnement virtuel (recommandé)**
 
	```bash
	python -m venv venv
	````
# Sur Linux/Mac
	```bash
	source venv/bin/activate
	````
# Sur Windows (PowerShell)
	```
	.\venv\Scripts\Activate.ps1
   	````

3. **Installer les dépendances**

   ```bash
   pip install -r requirements.txt
   ````

4. **Appliquer les migrations**

   ```bash
   python manage.py migrate
   ````

5. **Créer un superutilisateur (pour accéder à l’admin Django)**

   ```bash
   python manage.py createsuperuser
   ````

6. **Lancer le serveur**

   ```bash
   python manage.py runserver
   ````

   Puis ouvrir ton navigateur à l’adresse :
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

##  Structure du projet

```
l3_ifnti_notes/
│── ifnti_l3/              # Fichiers principaux de configuration Django
│── notes/                 # Application principale (models, views, templates)
│── manage.py              # Commandes Django
│── requirements.txt       # Dépendances Python
│── README.md              # Documentation du projet
│── .gitignore             # Fichiers ignorés par Git
````

---

##  Auteur

 **Aliya Abdoulaye** – Étudiante en Génie Logiciel à l’IFNTI
