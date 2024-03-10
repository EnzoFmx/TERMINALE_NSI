# Module Flask : 

## 1. Utilisation :

Flask est utilisé pour créer des applications web sous le langage python. Il permettra de manipuler des pages HTML, CSS.

## 2. Débuts avec le module : 

Afin d'utiliser le module il faut créer un fichier python. Pour cela :

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenue sur la page racine!'

if __name__ == '__main__':
    app.run(debug=True)
```

Une fois le code executé ceci apparaîtra :

```python
* Serving Flask app 'flask_test'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 621-730-068
```

Cela indique que pour accéder au serveur il faut utiliser l'URL suivant : http://127.0.0.1:5000

Ce lien correspond à votre adresse IP locale, 5000 correspond au port utilisé pour le module. Sur le fichier 'racine', nous pourrions aussi créer un lien vers une page fils sous la forme '127.0.0.1:5000/acceuil'. Pour l'instant dans le fichier Python, nous en sommes à la route '/' soit la racine du site.

Il est donc possible de créer d'autres routes :

```python
@app.route('/acceuil')
def acceuil():
    return 'Bienvenue sur la page d\'accueil!'
```

Et en accédant à la page d'acceuil (avec le lien suivant : http://127.0.0.1:5000/acceuil) nous auront le message "Bienvenue sur la page d'acceuil"

## 3. Utiliser des pages HTML déjà créées :

Il est possible d'utiliser des pages html dans notre serveur web. Pour cela, il faut créer un dossier appelé 'templates' ce dossier doit impérativement se trouver au même niveau que votre fichier python.

Une fois créer, il est possible de renvoyer la page comme ceci :

```python
@app.route('/')
def test():
  return render_template('index.html')
```

Dans une page HTML, il est possible de changer des données en fonction de certains paramètres.

Par exemple une page HTML :

```html
<!doctype html>
<html lang="fr">
	<head>
		<meta charset="utf-8">
		<title>Utilisation de Flask</title>
	</head>
	<body>
	  <h1>Mon super site</h1>
	  <p>Le serveur fonctionne parfaitement, il est {{heure}} h {{minute}} minutes et {{seconde}} secondes</p>
	</body>
</html>
```

Ici nous avons 3 données qui s'adapterons aux paramètres de la fonction qui lancera la page : heure, minute et seconde. 

La page se lance donc comme ceci :

```python
@app.route('/test')
def index():
  date = datetime.datetime.now()
  h = date.hour
  m = date.minute
  s = date.second
  return render_template("resultat.html", heure = h, minute = m, seconde = s)
```

On donne une valeur aux données de la page qui seront affichées lors de l'ouverture de la page.

## 4. Intégration d'une page CSS :

L'intégration d'une page CSS se fait de la même manière qu'une page HTML, il faut créer un dossier spécifique appelé 'static' dans le quel on ajoutera un autre dossier 'css' qui condiendra notre page CSS.

Le lien de la page CSS avec la page HTML se fait comme ceci :

```html
<link href="{{ url_for('static', filename='css/page.css') }}" rel="stylesheet"/>
```

