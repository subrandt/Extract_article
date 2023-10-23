import requests
from bs4 import BeautifulSoup

# Spécifiez l'URL du site
url = 'https://www.charentelibre.fr/sport/athletisme/g2a/athletisme-le-g2a-en-argent-aux-france-de-5-km-17176854.php'  # Remplacez par l'URL réelle

# Téléchargez le contenu de la page
response = requests.get(url)

# Vérifiez si la requête a réussi (code de statut 200)
if response.status_code == 200:
    # Récupérez le contenu HTML de la page
    html_content = response.content

    # Analysez le HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Sélectionnez le div avec la classe spécifiée
    div_article = soup.find('div', class_='article-body-wrapper visible-premium')

    # Extraire le texte
    texte = div_article.get_text()

    # Imprimer le texte extrait
    print(texte)
else:
    print(f"Erreur {response.status_code}: Impossible de récupérer le contenu de la page.")
