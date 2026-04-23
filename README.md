Django – Atelier 1 : Application Products sur la branch main
Description du projet

Dans le cadre de cet atelier de développement web avec Django, j’ai réalisé une première application web simple en suivant l’architecture MVT (Model-View-Template). L’objectif principal était de comprendre la structure d’un projet Django, la création d’une application, ainsi que la mise en place des routes, des vues et des templates pour afficher du contenu dynamique.

Travail réalisé

J’ai commencé par installer l’environnement de développement en configurant Python, pip et un environnement virtuel afin d’isoler les dépendances du projet. Ensuite, j’ai créé un projet Django nommé ecommerce, qui constitue la base de l’application.

Après cela, j’ai développé une application appelée products, intégrée au projet via le fichier settings.py. Cette application contient les différents fichiers nécessaires au fonctionnement d’une application Django, notamment les vues, les modèles et la configuration de l’administration.

J’ai ensuite implémenté plusieurs vues dans le fichier views.py permettant de gérer l’affichage des données. Ces vues sont reliées à des URLs définies dans les fichiers urls.py (au niveau du projet et de l’application), ce qui permet de naviguer entre les différentes pages.

Pour la partie interface utilisateur, j’ai créé un dossier templates contenant deux صفحات HTML : une page affichant la liste des produits (products_list.html) et une page affichant le détail d’un produit spécifique (product_detail.html). Ces templates sont rendus dynamiquement grâce aux vues.

Enfin, j’ai testé le bon fonctionnement de l’application en lançant le serveur de développement Django et en accédant aux différentes routes via le navigateur, notamment l’affichage de la liste des produits et le détail d’un produit en fonction de son identifiant.

Résultat

Le projet aboutit à une application web fonctionnelle permettant de naviguer entre une liste de produits et une page de détail, illustrant les concepts fondamentaux de Django tels que le routage, la séparation des responsabilités . Ce travail constitue une base solide pour le développement d’applications web plus complexes avec Django.


Atelier 2 : Branch ATERLIER_2

Dans le fichier models.py, j’ai défini le modèle Product avec ses attributs, puis le modèle Category et j’ai établi une relation plusieurs-à-un entre eux.
J’ai effectué les migrations avec makemigrations et migrate pour créer les tables dans la base de données.
Les deux modèles ont été enregistrés dans l’administration Django.
J’ai écrit quatre vues (liste produits, détail produit, liste catégories, détail catégorie) et leurs URLs.
J’ai créé les templates correspondants pour afficher les données.
J’ai configuré la gestion des images avec Pillow, le dossier images/products et les paramètres MEDIA_ROOT et MEDIA_URL.
Enfin, j’ai modifié les paramètres de base de données pour passer de SQLite à MySQL avec le connecteur mysqlclient.
