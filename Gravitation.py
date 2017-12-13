#fonction entrée avec des inputs classiques
#la fonction va renvoyer les valeurs de a et b
def entrée ():
    a=int(input("Valeur de a :"))
    b=int(input("Valeur de b :"))
    return a,b;
#fonction métier avec le calcul de la force de gravitation entre les 2 solides
#le résultat f sera renvoyer
def métier ():
    k=6.67*(10/10/10/10/10/10/10/10/10/10/10)
    m=10000*10000
    d=a*a
    i=m/d
    f=k*i
    return f;
#fonction sortie pour afficher le résultat ainsi que la valeur de a correspondante
def sortie ():
    print("f (",a,") =",f,"N")
#dans le code en lui même nous allons définir a et b avec la fonction entrée
#on va ensuite lancer une boucle non bornée
#tant que a<b, le calcul de la gravitation se fera avec la fonction métier et sera afficher avec la fonction sortie
#a deviens son double et si a*2<b la bucle va se répéter, sinon elle s'arrête
a,b=entrée()
while (a<b):
    f=métier()
    sortie()
    a=a*2

    
    

    
