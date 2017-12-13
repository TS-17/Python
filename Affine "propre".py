#ici c'est la fonction entrée
#on va demander 2 valeurs : a et b à l'utilisateur
#elle va renvoyer a et b
def entrée ():
    a=int(input("Valeur de a :"))
    b=int(input("Valeur de b :"))
    return a,b;
#ici c'est la fonction métier
#c'est donc le calcul ax+b d'une fonction affine
#elle va renvoyer le résultat    
def métier():
        r=a*x+b
        return r;
#ici c'est la fonction sortie
#elle affiche f(x)=r
def sortie ():
    print("f(",x,") =",r)
#on va donc demander les deux valeurs a et b
#puis on va executer les fonctions métier et sortie en boucle
a,b=entrée()
for x in range(0,10):
    r=métier()
    sortie()


    
