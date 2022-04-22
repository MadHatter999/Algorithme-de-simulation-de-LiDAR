import turtle
import time
from math import *
 
def dessiner_piste(longext,largext,longint,largint):
    turtle.up()  #Lève le crayon
    turtle.goto(-longext/2, 0)
    turtle.down()
    for i in range(2):
        turtle.forward(longext)  #Côté
        turtle.circle(0, 90)
        turtle.forward(largext)
        turtle.circle(0, 90)
        
    turtle.up()  #Lève le crayon
    turtle.goto(((longext-longint)/2)-longext/2, (largext-largint)/2)
    turtle.down()

    for i in range(2):
        turtle.forward(longint)  #Côté
        turtle.circle(0, 90)
        turtle.forward(largint)
        turtle.circle(0, 90)

def dessiner_voiture(xv,yv,av,longv,largv):
    turtle.up()  #Lève le crayon
    turtle.goto(xv+cos(radians(av))*longv/2,yv+sin(radians(av))*longv/2)
    turtle.circle(0,90+av)
    turtle.down()
    turtle.color("blue")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(largv/2)
        turtle.circle(0, 90)
        turtle.forward(longv)  #Côté
        turtle.circle(0, 90)
        turtle.forward(largv/2)

    turtle.end_fill()
    turtle.color("black")
    turtle.up()  #Lève le crayon
    turtle.goto(xv,yv)
    turtle.setheading(radians(av))
    turtle.down()


def segment(x,y):#dessine le segment limited by la position de la voiture et (x,y) 
    turtle.up() #Lève le cray
    turtle.goto(x_voiture,y_voiture)
    #turtle.circle(0,atan(angle_voiture+(y-y_voiture)/(x-x_voiture)))
    turtle.down()
    turtle.goto(x,y)
    turtle.dot(5, "red") #colorer le pt d'intersection

################################################################################

#               d4->  ######################################################
#                     #                                                     #
#                     #                                                     #
#                     #                                                     #
#                     # d3->  #########################################     #
#                     #       #                                       #     #
#                     #       #                                       #     #
#                     #       #                                       #     #
#                     # d2->  #########################################     #
#                     #       ^                                       ^     #
#                     #       |                                       |     #
#                     #       d6                                      d7    #
#               d1->  ###########################+###########################
#                     ^                          O                          ^
#                     |                                                     |
#                     d5                                                    d8
#O:origine du repere de coord.(0,0)
#d1,d2,d3,d4,d5,d6,d7,d8 segements

def vert_intersect_d1(c,d):#verifie s'il y a une intersection entre la droite verticale passant par la voiture et d1
    return (not((abs(c)<=longueur_int/2) and (d>(largeur_ext+largeur_int)/2)))

def vert_intersect_d4(c,d):#verifie s'il y a une intersection entre la droite verticale passant par la voiture et d4
    return (not((abs(c)<=longueur_int/2)and(d<(largeur_ext-largeur_int)/2)))

def vert_intersect_d3(c,d):#verifie s'il y a une intersection entre la droite verticale passant par la voiture et d3
    return (((abs(c)<=longueur_int/2) and (d>(largeur_ext+largeur_int)/2)))

def vert_intersect_d2(c,d):#verifie s'il y a une intersection entre la droite verticale passant par la voiture et d2
    return (((abs(c)<=longueur_int/2) and (d<(largeur_ext-largeur_int)/2)))

def intersect_d1(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et d1
    y=0
    if (a==0):
        return (False)
    return ((abs((y-b)/a)<=longueur_ext/2))

def intersect_d4(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et d4
    y=largeur_ext
    if (a==0):
        return (False)
    return ((abs((y-b)/a)<=longueur_ext/2))

def intersect_d2(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et d2
    y=(largeur_ext-largeur_int)/2
    if (a==0):
        return (False)
    return ((abs((y-b)/a)<=longueur_int/2))

def intersect_d3(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et d3
    y=(largeur_ext+largeur_int)/2
    if (a==0):
        return (False)
    return ((abs((y-b)/a)<=longueur_int/2))

def intersect_d5(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et d5
    return((-a*longueur_ext/2+b<=largeur_ext) and (-a*longueur_ext/2+b>=0))

def intersect_d8(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et d8
    return((a*longueur_ext/2+b<=largeur_ext) and (a*longueur_ext/2+b>=0))

def intersect_d6(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et d6
    return((-a*longueur_int/2+b<=(largeur_ext+largeur_int)/2) and (-a*longueur_int/2+b>=(largeur_ext-largeur_int)/2))

def intersect_d7(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et d7
    return((a*longueur_int/2+b<=(largeur_ext+largeur_int)/2) and (a*longueur_int/2+b>=(largeur_ext-largeur_int)/2))

def calcul_intersect_d1(a,b):#calcule le pt d'intersection entre la droite d'eq y=ax+b passant par la voiture et d1
    if intersect_d1(a,b):
        l.append((-b/a,0))
        segment(-b/a,0)

def calcul_intersect_vert_d1(c,d):#calcule le pt d'intersection entre la droite d'eq x=c passant par la voiture et d1
    if vert_intersect_d1(c,d):
        l.append((c,0))
        segment(c,0)

def calcul_intersect_vert_d4(c,d):#calcule le pt d'intersection entre la droite d'eq x=c passant par la voiture et d4
    if vert_intersect_d4(c,d):
        l.append((c,largeur_ext))
        segment(c,largeur_ext)

def calcul_intersect_vert_d2(c,d):#calcule le pt d'intersection entre la droite d'eq x=c passant par la voiture et d2
    if vert_intersect_d2(c,d):
        l.append((c,(largeur_ext-largeur_int)/2))
        segment(c,(largeur_ext-largeur_int)/2)

def calcul_intersect_vert_d3(c,d):#calcule le pt d'intersection entre la droite d'eq x=c passant par la voiture et d3
    if vert_intersect_d3(c,d):
        l.append((c,(largeur_ext+largeur_int)/2))
        segment(c,(largeur_ext+largeur_int)/2)

def calcul_intersect_d2(a,b):#calcule le pt d'intersection entre la droite d'eq y=ax+b passant par la voiture et d2
    if intersect_d2(a,b):
        yy=(largeur_ext-largeur_int)/2
        l.append(((yy-b)/a,yy))
        segment((yy-b)/a,yy)

def calcul_intersect_d3(a,b):#calcule le pt d'intersection entre la droite d'eq y=ax+b passant par la voiture et d3
    if intersect_d3(a,b):
        yy=(largeur_ext+largeur_int)/2
        l.append(((yy-b)/a,yy))
        segment((yy-b)/a,yy)

def calcul_intersect_d4(a,b):#calcule le pt d'intersection entre la droite d'eq y=ax+b passant par la voiture et d4
    if intersect_d4(a,b):
        yy=(largeur_ext)
        l.append(((yy-b)/a,yy))
        segment((yy-b)/a,yy)

def calcul_intersect_d5(a,b):#calcule le pt d'intersection entre la droite d'eq y=ax+b passant par la voiture et d5
    if intersect_d5(a,b):
        xx=-longueur_ext/2
        l.append((xx,a*xx+b))
        segment(xx,a*xx+b)


def calcul_intersect_d6(a,b):#calcule le pt d'intersection entre la droite d'eq y=ax+b passant par la voiture et d6
    if intersect_d6(a,b):
        xx=-longueur_int/2
        l.append((xx,a*xx+b))
        segment(xx,a*xx+b)

def calcul_intersect_d7(a,b):#calcule le pt d'intersection entre la droite d'eq y=ax+b passant par la voiture et d7
    if intersect_d7(a,b):
        xx=longueur_int/2
        l.append((xx,a*xx+b))
        segment(xx,a*xx+b)

def calcul_intersect_d8(a,b):#calcule le pt d'intersection entre la droite d'eq y=ax+b passant par la voiture et d8
    if intersect_d8(a,b):
        xx=longueur_ext/2
        l.append((xx,a*xx+b))
        segment(xx,a*xx+b)


def intersect_piste(a,b):#calcule le pt d'intersection entre la droite d'eq y=ax+b passant par la voiture et la piste
    if (abs(x_voiture)<=largeur_int/2):
        if (y_voiture<(largeur_ext-largeur_int)/2):
            calcul_intersect_d1(a,b)
            calcul_intersect_d2(a,b)
            if not(intersect_d2(a,b)):
                calcul_intersect_d5(a,b)
                calcul_intersect_d8(a,b)
        else:
            calcul_intersect_d3(a,b)
            calcul_intersect_d4(a,b)
            if not(intersect_d3(a,b)):
                calcul_intersect_d5(a,b)
                calcul_intersect_d8(a,b)
    elif ((y_voiture>=(largeur_ext-largeur_int)/2) and (y_voiture<=(largeur_ext+largeur_int)/2)):
        if (x_voiture<=(-largeur_int/2)):
            calcul_intersect_d5(a,b)
            calcul_intersect_d6(a,b)
            if not(intersect_d6(a,b)):
                calcul_intersect_d1(a,b)
                calcul_intersect_d4(a,b)
        else:
            calcul_intersect_d7(a,b)
            calcul_intersect_d8(a,b)
            if not(intersect_d7(a,b)):
                calcul_intersect_d1(a,b)
                calcul_intersect_d4(a,b)
    elif (x_voiture<=-longueur_int/2) and (y_voiture<=(largeur_ext-largeur_int)/2):
        calcul_intersect_d1(a,b)
        calcul_intersect_d5(a,b)
        calcul_intersect_d2(a,b)
        calcul_intersect_d6(a,b)
        if (not(intersect_d2(a,b)) and not(intersect_d6(a,b))):
            calcul_intersect_d8(a,b)
            calcul_intersect_d4(a,b)
    elif (x_voiture>=longueur_int/2) and (y_voiture<=(largeur_ext-largeur_int)/2):
        calcul_intersect_d1(a,b)
        calcul_intersect_d8(a,b)
        calcul_intersect_d7(a,b)
        calcul_intersect_d2(a,b)
        if (not(intersect_d2(a,b)) and not(intersect_d7(a,b))):
            calcul_intersect_d4(a,b)
            calcul_intersect_d5(a,b)
        
    elif (x_voiture>=longueur_int/2) and (y_voiture>=(largeur_ext+largeur_int)/2):
        calcul_intersect_d3(a,b)
        calcul_intersect_d4(a,b)
        calcul_intersect_d7(a,b)
        calcul_intersect_d8(a,b)
        if (not(intersect_d3(a,b)) and not(intersect_d7(a,b))):
            calcul_intersect_d5(a,b)
            calcul_intersect_d1(a,b)
    else:
        calcul_intersect_d5(a,b)
        calcul_intersect_d3(a,b)
        calcul_intersect_d4(a,b)
        calcul_intersect_d6(a,b)
        if (not(intersect_d3(a,b)) and not(intersect_d6(a,b))):
            calcul_intersect_d8(a,b)
            calcul_intersect_d1(a,b)


 #############################################################
 #########################  MAIN  ############################  
 #############################################################        

drawing_area=turtle.Screen() 
drawing_area.title("Piste")
turtle.speed(0)# si vous voulez dessiner avec la vitesse la plus rapide
turtle.tracer(False)# pour ne pas attendre le dessin 
#dimensions de la piste
longueur_ext=550
longueur_int=450
largeur_ext=250  
largeur_int=150

#position de la voiture : default(0,25)
#si vous voulez changer la position de la voiture il faut verifier les conditions ci-dessous
#pour que la voiture soit sur la piste il faut que :
#(-275,0)<(x_v,y_v)<(275,250)
# et (x_v,y_v) n'appartient pas au rectongle interieur
# c'est-a-dire not((-225,50)<=(x_v,y_v)<(225,200))   

x_voiture=-250
y_voiture=225
angle_voiture=225
#dimensions de la voiture
longueur_voiture=25
largeur_voiture=10

#les positions de references de tests qui sont les corners et les milieux des droites de la piste
p1=[0,(largeur_ext-largeur_int)/4,0]
p2=[(longueur_ext+longueur_int)/4,p1[1],45]
p3=[p2[0],largeur_ext/2,90]
p4=[p2[0],(3*largeur_ext+largeur_int)/4,135]
p5=[0,p4[1],180]
p6=[(-longueur_ext-longueur_int)/4,p5[1],225]
p7=[p6[0],p3[1],270]
p8=[p6[0],p1[1],315]

liste_positions=[p1,p2,p3,p4,p5,p6,p7,p8]

#nombre de droites a construire
nbr=8
while(True):
   nbr=int(input("Donnez le nombre de droites a construire (strictement positif) : "))
   if (nbr>0):
       break

j=0
while(True):
    #tableau ou on met les points d'intersections de la droite de pente tan(theta) passant par les coordonnees de la voiture  avec la piste
    #theta=indice du tableau*360/nbr 
    tableau_intersect=[]
    x_voiture=liste_positions[j][0]
    y_voiture=liste_positions[j][1]
    angle_voiture=liste_positions[j][2]

    turtle.reset() #effacer pour creer une autre frame
    turtle.tracer(False)
    dessiner_piste(longueur_ext,largeur_ext,longueur_int,largeur_int)
    turtle.up()  #Lève le crayon
    turtle.goto(x_voiture,y_voiture)
    turtle.down()

    for i in range(nbr):
        theta=((180/nbr)*i+angle_voiture)%180
        l=[]
        if ((theta!=90)):     
            intersect_piste(tan(radians(theta)),y_voiture-tan(radians(theta))*x_voiture)
            tableau_intersect.append(l)
        else:
            calcul_intersect_vert_d2(x_voiture,y_voiture)
            calcul_intersect_vert_d4(x_voiture,y_voiture)
            calcul_intersect_vert_d1(x_voiture,y_voiture)
            calcul_intersect_vert_d3(x_voiture,y_voiture)
            tableau_intersect.append(l)

    dessiner_voiture(x_voiture,y_voiture,angle_voiture,25,10)
    turtle.tracer(True)
    turtle.up()  #Lève le crayon
    turtle.goto(x_voiture,y_voiture)
    turtle.circle(0,angle_voiture)
    turtle.down()

    print("x_voiture: ",x_voiture,"        y_voiture: ",y_voiture,"        angle_voiture :",angle_voiture)
    for k in range(nbr):
        print("theta=",(180/nbr)*k," : ")
        print(tableau_intersect[k])
    while(True):
        if (j<7):
            ans=(input("Voulez vous passer a l'autre position de test?[y,n] "))
            if (ans=="y"):
                print("\n")
                break
            elif (ans=="n"):
                print("Le test de position est fini! Veuillez cliquer sur l'ecran de la piste pour la fermer.")
                break
        else:
            print("Le test de position est fini! Veuillez cliquer sur la fenetre de piste pour la fermer.")
            break

    j+=1
    if (j==8) or (ans=="n"):
        break        
    # time.sleep(2)
    
turtle.exitonclick()


