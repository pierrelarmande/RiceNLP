# Perform standard imports:
import spacy
liste=[]
nlp = spacy.load('en_core_web_sm')
with open('abstract.txt','r') as mon_fichier:
    doc1 = mon_fichier.readline()
    liste_mot=doc1.split()
    print(liste_mot)
    print(len(liste_mot))
    for mot in liste_mot:
        #print(mot)
        doc=nlp(mot)
        print([token.lemma_ for token in doc if token.pos_ == "VERB" or token.pos_ == "NOUN" or token.pos_ == "ADJ" ])
#        if token.pos == VERB or token.pos == NOUN or token.pos == ADJ :




'''['11149940', 'Essential', 'role', 'of', 'the', 'small'
 , 'GTPase', 'Rac', 'in', 'disease', 'resistance', 'of',
 'rice.', '2001', 'Proc', 'Natl', 'Acad', 'Sci', 'U', 'S', 'A',
 'Production', 'of', 'reactive', 'oxygen', 'intermediates', '(ROI)',
 'and', 'a', 'form', 'of', 'programmed', 'cell', 'death', 'called',
 'hypersensitive', 'response', '(HR)', 'are', 'often', 'associated',
 'with', 'disease', 'resistance', 'of', 'plants.',
 'We', 'have', 'previously', 'shown', 'that', 'the', 'Rac', 'homolog',
 'of', 'rice,', 'OsRac1,', 'is', 'a', 'regulator', 'of', 'ROI', 'production',
 'and', 'cell', 'death', 'in', 'rice.', 'Here', 'we', 'show', 'that',
 'the', 'constitutively', 'active', 'OsRac1', '(i)', 'causes', 'HR-like',
 'responses', 'and', 'greatly', 'reduces', 'disease', 'lesions', 'against',
 'a', 'virulent', 'race', 'of', 'the', 'rice', 'blast', 'fungus;', '(ii)',
 'causes', 'resistance', 'against', 'a', 'virulent', 'race', 'of', 'bacterial',
 'blight;', 'and', '(iii)', 'causes', 'enhanced', 'production', 'of', 'a',
 'phytoalexin', 'and', 'alters', 'expression', 'of', 'defense-related',
 'genes.', 'The', 'dominant-negative', 'OsRac1', 'suppresses',
 'elicitor-induced', 'ROI', 'production', 'in', 'transgenic', 'cell',
 'cultures,', 'and', 'in', 'plants', 'suppresses', 'the', 'HR', 'induced',
 'by', 'the', 'avirulent', 'race', 'of', 'the', 'fungus.', 'Taken',
 'together,', 'our', 'findings', 'strongly', 'suggest', 'that', 'OsRac1',
 'has', 'a', 'general', 'role', 'in', 'disease', 'resistance', 'of', 'rice.']'''

'''Je ne sais pas pour quoi il y a des mots qui ne sont ni des mots des nom
ni des adj, C'est surprenant. Exemple de résultat pour le gene '''






