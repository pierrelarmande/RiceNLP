from testepd import *
from pubmed_lookup import PubMedLookup
from pubmed_lookup import Publication


def recup_Abstract(gene):
    '''Cette fonction permet de récupérer des abstracts dans un fichier'''
    email = 'jcricklin@gmail.com'
    url = 'http://www.ncbi.nlm.nih.gov/pubmed/'
    ecrire_Id(gene)
    with open('abstract.txt','w') as nouveau_fichier:
        with open('pubmed.txt','r') as mon_fichier :
            str_id=mon_fichier.read()
            liste_id=str_id.split('\t')
            for idpm in liste_id :
                lookup = PubMedLookup(url+idpm, email)
                publication = Publication(lookup)
                nouveau_fichier.write('{pubmed}\t{title}\t{year}\t{journal}\t{abstract}\n'
                                        .format(**{
                                            'pubmed': idpm,
                                            'title': publication.title,
                                            'year': publication.year,
                                            'journal': publication.journal,
                                            'abstract': publication.abstract,
                                        }))
    return nouveau_fichier


recup_Abstract('RAC1')
#    print(
#    """
#    TITLE:\n{title}\n
#    AUTHORS:\n{authors}\n
#    JOURNAL:\n{journal}\n
#    YEAR:\n{year}\n
#    MONTH:\n{month}\n
#    DAY:\n{day}\n
#    URL:\n{url}\n
#    PUBMED:\n{pubmed}\n
#    CITATION:\n{citation}\n
#    MINICITATION:\n{mini_citation}\n
#    ABSTRACT:\n{abstract}\n
#    """
#    .format(**{
#        'title': publication.title,
#        'authors': publication.authors,
#        'journal': publication.journal,
#        'year': publication.year,
#        'month': publication.month,
#        'day': publication.day,
#        'url': publication.url,
#        'pubmed': publication.pubmed_url,
#        'citation': publication.cite(),
#        'mini_citation': publication.cite_mini(),
#        'abstract': repr(publication.abstract),
#    }))
