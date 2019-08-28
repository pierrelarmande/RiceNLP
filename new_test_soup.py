import requests
from bs4 import BeautifulSoup

'''Ce Code permet de trouver des mots clés déjà présent dans pubmed'''

def getBalise(url):
    result = requests.get(url)
    c = result.content
    soup = BeautifulSoup(c,"html.parser")
    for bal in soup.find_all('meta'):
        if bal.get("name")=="keywords":
            print(bal)
            

url = 'https://www.ncbi.nlm.nih.gov/pubmed/11149940'
art=getBalise(url)
print(art)
