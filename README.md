Django – Atelier 1 : Application Products
Description du projet

Dans le cadre de cet atelier de développement web avec Django, j’ai réalisé une première application web simple en suivant l’architecture MVT (Model-View-Template). L’objectif principal était de comprendre la structure d’un projet Django, la création d’une application, ainsi que la mise en place des routes, des vues et des templates pour afficher du contenu dynamique.

Travail réalisé

J’ai commencé par installer l’environnement de développement en configurant Python, pip et un environnement virtuel afin d’isoler les dépendances du projet. Ensuite, j’ai créé un projet Django nommé ecommerce, qui constitue la base de l’application.

Après cela, j’ai développé une application appelée products, intégrée au projet via le fichier settings.py. Cette application contient les différents fichiers nécessaires au fonctionnement d’une application Django, notamment les vues, les modèles et la configuration de l’administration.

J’ai ensuite implémenté plusieurs vues dans le fichier views.py permettant de gérer l’affichage des données. Ces vues sont reliées à des URLs définies dans les fichiers urls.py (au niveau du projet et de l’application), ce qui permet de naviguer entre les différentes pages.

Pour la partie interface utilisateur, j’ai créé un dossier templates contenant deux صفحات HTML : une page affichant la liste des produits (products_list.html) et une page affichant le détail d’un produit spécifique (product_detail.html). Ces templates sont rendus dynamiquement grâce aux vues.

Enfin, j’ai testé le bon fonctionnement de l’application en lançant le serveur de développement Django et en accédant aux différentes routes via le navigateur, notamment l’affichage de la liste des produits et le détail d’un produit en fonction de son identifiant.

Résultat

Le projet aboutit à une application web fonctionnelle permettant de naviguer entre une liste de produits et une page de détail, illustrant les concepts fondamentaux de Django tels que le routage, la séparation des responsabilités et le rendu dynamique des صفحات. Ce travail constitue une base solide pour le développement d’applications web plus complexes avec Django.
