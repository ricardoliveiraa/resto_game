import pygame, sys
from pygame.locals import *
from random import randint
pygame.init()
#---------------------------------------------------------#
#Première partie pour d'abordtout setup: (Fenetre,variable,...)

#------Setup de la fenetre---------------------
mafenetre=pygame.display.set_mode((640,960))
pygame.display.set_caption('Aimlab 2')
mafenetre.fill((0,0,0))


#-------Variables----------------------------
positions_x=0            
positions_y=0            
score=0
T1=0                        
T2=0
regeneration=True
clock = pygame.time.Clock()          #Timer (aucune idée si on peut considérer ça comme une variable)

#-------Parametres des textes__________________

police=pygame.font.Font(None,80)

#-------Sprite/fond à afficher------------------
perso=pygame.image.load("sprite de base.png").convert_alpha()        #Charge l'image du perso et la convertit dans un type "reconnue par pyhton".Alpha pour garder la transparence
perso=pygame.transform.scale(perso,(130,220))






while True:
    mafenetre.fill((50,50,50)) #Fond noir A CHANGER PLUS TARD POUR UNE IMAGE (de resto ducoup..)
    mafenetre.blit(perso,(positions_x,positions_y))

    temps_ecoule = pygame.time.get_ticks() // 1000  # Divise par 1000 pour avoir des secondes
    texte_chronometre = police.render("Temps : " + str(temps_ecoule), True , (255, 255, 255))
    mafenetre.blit(texte_chronometre, (100,20))     # Affiche le chronomètre juste en dessous du score



    pygame.display.flip()
    for evenement in pygame.event.get():    #Pour fermer la fenetre grace à la croix de la fenetre.
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evenement.type == pygame.KEYDOWN:                    #Cette boucle sert à faire déplacer les deux barres rouges
            if evenement.key == pygame.K_UP and positions_y>0:          #Si on est dans la zone de jeu et qu'on appuis sur flèche du haut, on fait monter la barre horizontal
                positions_y=positions_y-10
            elif evenement.key == pygame.K_DOWN and positions_y<740:     #Si on est dans la zone de jeu et qu'on appuis surflèche du bas,on fait descendre la barre horizontal
                positions_y=positions_y+10
            elif evenement.key == pygame.K_LEFT and positions_x>0:       #Si on est dans la zone de jeu et qu'on appuis sur fleche gauche,on déplace à gauche la barre vertical
                positions_x=positions_x-10
            elif evenement.key == pygame.K_RIGHT and positions_x<510:    #Si on est dans la zone de jeu et qu'on appuis sur fleche droite, on déplace à droite la barre vertical
                positions_x=positions_x+10
