# Find the perfect wysiwyg for django 5

## Wysiwyg to test 
 - [x] TinyMCE (django-tinymce) https://pypi.org/project/django-tinymce/ - Antoine
 - [x] Quill.js (django-quill-editor) https://pypi.org/project/django-quill-editor/ - Antoine
 - [ ] DracEditor https://djangopackages.org/packages/p/draceditor/ - Evan
 - [x] Django Froala Editor https://djangopackages.org/packages/p/django-froala-editor/ - Evan
 
 ## Tableau des critères
 | Critères                         | Pondérations | django-tinymce (Jazzband)                          | django-quill-editor (LeeHanYeong)                  | martor (agusmakmun)                               | django-froala-editor (Officiel)                  |
 |----------------------------------|--------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|--------------------------------------------------|
 | Dépôt analysé                   |              | jazzband/django-tinymce                           | LeeHanYeong/django-quill-editor                   | agusmakmun/django-markdown-editor                 | froala/django-froala-editor                     |
 | Open source / Gratuité          |              | 5 (Paquet 100% libre)         | 5 (100% open source)                              | 5 (100% open source)                              | 1 (Nécessite licence commerciale Froala)        |
 | Popularité (Étoiles GitHub)     |              | 4 (~1 400 ★)                                      | 2 (~225 ★)                                        | 3 (~895 ★)                                        | 2 (~300 ★)                                      |
 | Activité (Dernier commit)       |              | 4 (08.12.2025)                                    | 1 (20.09.2024)                                    | 5 (19.04.2026)                                    | 4 (01.04.2026)                                  |
 | Intégration Django              |              | 5 (Maintenu par la fondation Jazzband)            | 3 (Projet perso, maintenance aléatoire)           | 5                                                | 4 (Officiel, mais logique parfois très JS)      |
 | Richesse (Tableaux, images)     |              | 5 (Passe toutes les configs JS via le widget Django) | 4 (Très propre, mais l'éditeur manque de tableaux poussés) | 3 (Markdown pur, rudimentaire)                   | 5 (Premium)                                     |
 | Extensibilité via Python        |              | 5 (Dictionnaires de config Python ultra flexibles) | 3 (Structure un peu rigide côté backend)          | 4 (Bon système pour intercepter les uploads via les vues) | 4 (Flexible, mais la doc backend est basique)  |
 | Poids / Performances            |              | 2 (Lourd à charger côté front)                    | 4 (Léger)                                         | 4 (Très léger)                                    | 3 (Moyen)                                       |
 | Qualité doc (Côté Django)       |              | 5 (complète) | 3 (correcte mais sans plus) | 4 (bien, exemples précis)     | 2 (Un simple README GitHub un peu sec)          |
 | Support Markdown natif          |              | 2 (Non natif)                                     | 2 (Non natif)                                     | 5 (C'est le but du paquet)                       | 2 (Non natif)                                   |
 | **TOTAL**                       |              |                                                    |                                                    |                                                    |                                                  |
 
 
 
 ## Final choice :
 
 **Unknown**
