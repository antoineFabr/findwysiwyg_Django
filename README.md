# Find the perfect wysiwyg for django 5

## Wysiwyg to test 
 - [x] TinyMCE (django-tinymce) https://pypi.org/project/django-tinymce/ - Antoine
 - [x] Quill.js (django-quill-editor) https://pypi.org/project/django-quill-editor/ - Antoine
 - [ ] DracEditor https://djangopackages.org/packages/p/draceditor/ - Evan
 - [x] Django Froala Editor https://djangopackages.org/packages/p/django-froala-editor/ - Evan
 
 ## Tableau des critères
 | Critères                         | Pondérations | django-tinymce (Jazzband)                          | django-quill-editor (LeeHanYeong)                  | martor (agusmakmun)                               | django-froala-editor (Officiel)                  | django-ckeditor-5 (hvlads)                | djangocms-text (django-cms) |
 |----------------------------------|--------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|--------------------------------------------------|-------------------------------------------|-----------------------------|
 | Dépôt analysé                   |              | jazzband/django-tinymce                           | LeeHanYeong/django-quill-editor                   | agusmakmun/django-markdown-editor                 | froala/django-froala-editor                     | hvlads/django-ckeditor-5                  | django-cms/djangocms-text   |
 | Open source / Gratuité          |              | 5 (Paquet 100% libre)                             | 5 (100% open source)                              | 5 (100% open source)                              | 1 (Nécessite licence commerciale Froala)        | 5 (open source)                          | 5 (open source)             |
 | Popularité (Étoiles GitHub)     |              | 4 (~1 400 ★)                                      | 2 (~225 ★)                                        | 3 (~895 ★)                                        | 2 (~300 ★)                                      | 2 (213 ★)                                  | 1 (20 ★)                      |
 | Activité (Dernier commit)       |              | 4 (08.12.2025)                                    | 1 (20.09.2024)                                    | 5 (19.04.2026)                                    | 4 (01.04.2026)                                  | 4 (26.02.2026)                          | 5 (26.04.2026)             |
 | Intégration Django              |              | 5 (Maintenu par la fondation Jazzband)            | 3 (Projet perso, maintenance aléatoire)           | 5                                                | 4 (Officiel, mais logique parfois très JS)      | 3 (Projet perso)                         | 5 (Maintenu par django-cms) |
 | Richesse (Tableaux, images)     |              | 5 (Passe toutes les configs JS via le widget Django) | 4 (Très propre, mais manque de tableaux avancés) | 3 (Markdown pur, rudimentaire)                   | 5 (Premium)                                     | 5                                        | 3 (moins riche que TinyMCE) |
 | Extensibilité via Python        |              | 5 (Config Python très flexible)                   | 3 (Structure backend rigide)                     | 4 (Bon système d’upload via vues)                | 4 (Flexible, doc backend basique)              | 3 (Plus complexe que TinyMCE)            | 4 (Très bien)              |
 | Poids / Performances            |              | 3 (Assez lourd)                                  | 4 (Léger)                                         | 4 (Léger)                                        | 3 (Moyen)                                       | 2 (Lourd)                               |  2 (Lourd) |                          |
 | Qualité doc (Côté Django)       |              | 5 (Complète)                                     | 3 (Correcte)                                      | 4 (Bonne, exemples précis)                        | 2 (README limité)                               | 5 (Complète)                            | 4 (Bonne)                  |
 | Support Markdown natif          |              | 2 (Non natif)                                     | 2 (Non natif)                                     | 5 (Objectif principal)                            | 2 (Non natif)                                   | 2 (Non natif)                          | 2 (Non natif)             |
 | **TOTAL**                       |              |                                                    |                                                    |                                                    |                                                  |                                           |                             |
 
 
 
 ## Final choice :
 
 **Unknown**
