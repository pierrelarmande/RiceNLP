# you need to install Biopython:
# pip install biopython

# Full discussion:
# https://marcobonzanini.wordpress.com/2015/01/12/searching-pubmed-with-python/

from Bio import Entrez

def search(query):
    '''Donne la liste des articles dans les quels le nom d'un gene apparait '''
    Entrez.email = 'jcricklinl@gmail.com'
    handle = Entrez.esearch(db='pubmed', sort='relevance', retmax='20', retmode='xml', term=query)
    results = Entrez.read(handle)
    return results

def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'jcricklin@gmail.com'
    handle = Entrez.efetch(db='pubmed', retmode='xml', id=ids)
    results = Entrez.read(handle)
    return results

if __name__ == '__main__':
    results = search('sphingolipid elicitors')
    id_list = results['IdList']
    print(id_list)
    papers = fetch_details(id_list)
    for i, paper in enumerate(papers['PubmedArticle']):
        print("%d) %s" % (i+1, paper['MedlineCitation']['Article']['ArticleTitle']))




# Pretty print the first paper in full
#import json
#print(json.dumps(papers[0], indent=2, separators=(',', ':')))
