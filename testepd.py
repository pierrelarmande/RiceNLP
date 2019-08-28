import pandas as pd
import csv



df = pd.read_csv("Feuille_gene.txt", sep='\t', header = 0, delimiter=None, dtype='str', encoding ='latin1', error_bad_lines=False,quoting=csv.QUOTE_NONE)



###########Teste de lecture de la feuille #############

#print(type(df))

#print(df.shape)

############On regarde les clefs affin de considérer la data frame réduite qui permet de regrouper les genes ##########

#print(df.columns)

###########On restrain à l'étude de la data frame###########


y=df[['PubMedId','CGSNL Gene Symbol']]


###########On crée la fonction qui regroupe les génes entre eux#############


#####Petite boucle de vérification######

#for i,row in y.iterrows():
   # if type(row[0])==str and type(row[1])==str:
        #liste_gene=row[1].split(',')
        #print(liste_gene)



def liste_Voisin(gene):
    ''' Prend un gene et resort une liste de voisins et des articles où il apparait '''
    liste_voisin=[]
    liste_Id=[]
    for i,row in y.iterrows():
        if type(row[0])==str and row[0]!=0 and type(row[1])==str:
            liste_gene=row[1].split(',')
            for i1_gene in liste_gene :
                if i1_gene == gene :
                    liste_Id+=[row[0]]
                    for i2_gene in liste_gene :
                        if i2_gene != gene and i2_gene != '_' :
                            liste_voisin += [i2_gene]
    liste_voisin=list(set(liste_voisin))
    return liste_voisin,liste_Id

#exemple d'utilisation de ma fonction avec un gene

def ecrire_Id(gene):
    '''ecrit les Id pubmed dans un fichier'''
    l=liste_Voisin(gene)
    with open('pubmed.txt','w') as file :
        for pmid in l[1] :
            file.write('%s\t' %(pmid))
        file.close() 
    

    

ecrire_Id('RAC1')
#print(l[1])







        
        
        
