from statistics import mean as m

admins = {'Admin':'admin'}

eleveDict = {'Leo':[13,11,17],
             'Marie':[18,12,15],
             'Paul':[8,13,10]}

def entrerNote():
    entrerNom = input('Nom de l\'eleve: ')
    entrerNote = input('Note obtenue: ')

    if entrerNom in eleveDict:
        print('Ajouter une note...')
        eleveDict[entrerNom].append(float(entrerNote))
    else:
        print('Cet eleve n\'existe pas !')

    print(eleveDict)

def supprEleve():
    eleveSuppr = input('Quel eleve voulez-vous supprimer ? ')
    if eleveSuppr in eleveDict:
        print('Suppression de l\'eleve...')
        del eleveDict[eleveSuppr]

    print(eleveDict)

def eleveMoy():
    for chaqueEleve in eleveDict:
        listeNote = eleveDict[chaqueEleve]
        moyNotes = m(listeNote)

        print(chaqueEleve,'a une moyenne de: ',moyNotes) 

def main():
    print("""
    Bienvenue dans le gestionnaire de notes

    [1] - Rentrer des notes
    [2] - Supprimer un eleve
    [3] - Moyennes des eleves
    [4] - Quitter
    """)

    action = input('Que voulez-vous faire ? (Entrez un nombre) ')

    if action=='1':
        entrerNote()
    elif action=='2':
        supprEleve()
    elif action=='3':
        eleveMoy()
    elif action=='4':
        exit()
    else:
        print('Choix non valide, veuillez reessayer')

login = input('nom d\'utilisateur: ')
passw = input('mot de passe: ')

if login in admins:
    if admins[login]==passw:
        print('Bienvenue ',login)
        while True:
            main()
    else:
        print('Mot de passe invalide !!')
else:
    print('Utilisateur inconnu, contacter l\'administrateur')
