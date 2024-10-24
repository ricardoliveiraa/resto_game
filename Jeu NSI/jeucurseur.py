""" Dessiner des rectangles"""
""" Création d'un rectangle avec ses options, dans l'ordre :
    - l'objet auquee il est rattaché,
    - sa couleur (en RVB),
    - un tuple de 4 nombres
        * Coordonnées de son coin supérieur gauche
        * sa largeur et sa hauteur
    - un nombre indiquant l'épaisseur de son pourtour (mettre 0 s'il est rempli) """

import pygame, sys
from pygame.locals import *
from random import randint
from PIL import Image


pygame.mixer.init()
pygame.init()

# Création de l'objet fenêtre
mafenetre=pygame.display.set_mode((300,350))
pygame.display.set_caption('Exemples de rectangles')
mafenetre.fill((0,0,0))

deplacement=0
l1=0
h1=0
score=0
T1=1
T2=7
regeneration=True


police=pygame.font.Font(None,20)
position_text=(10,305)

# Initialisation de l'horloge
clock = pygame.time.Clock()

regeneration=True
while True:
    clock.tick(60)

    # Mise à jour de l'affichage de la fenêtre
    mafenetre.fill((0,0,0))
    pygame.draw.rect(mafenetre, (255,0,0),(0,h1,300,10),0)                          #Définit la barre horizontal
    pygame.draw.rect(mafenetre, (255,0,0),(l1,0,10,300),0)                           #Dafinit la barre vertical
    pygame.draw.rect(mafenetre , (255,255,255), (0 ,0 ,300 ,300), 5)        #Carré vide qui détoure la zone de jeu


    texte_score=police.render("Score : " + str(score) , True , (255,255,255))
    mafenetre.blit(texte_score,position_text)

    temps_ecoule = pygame.time.get_ticks() // 1000  # Divise par 1000 pour avoir des secondes
    texte_chronometre = police.render("Temps : " + str(temps_ecoule), True , (255, 255, 255))
    mafenetre.blit(texte_chronometre, (10, 325))     # Affiche le chronomètre juste en dessous du score

    texte_deplacement=police.render("Tu es à "+str(deplacement)+" déplacements !", True, (255,255,255))
    position_deplacement=(100,315)
    mafenetre.blit(texte_deplacement,position_deplacement)







    if regeneration==True :
        pos_l_carre=round(randint(5,285),-1)         #Génere la valeur qui servira pour la position du carré en longeur
        pos_h_carre=round(randint(5,285),-1)       #Génere la valeur qui servira pour la position du carré en hauteur
        T1=temps_ecoule
        regeneration=False
    pygame.draw.rect(mafenetre, (0,0,255),(pos_l_carre,pos_h_carre,10,10),0)        #Fait apparaitre le carré avec les positions généré

    if h1==pos_h_carre and l1==pos_l_carre:     #Vérifie si le "curseur" à les meme coordonées que le carré
        score=score+1
        son=pygame.mixer.Sound('bruitpointjeu.wav')
        son.play(loops=0, maxtime=0, fade_ms=0)
        T2=temps_ecoule
        if T2-T1<3:
            score=score+1
        regeneration=True                       #Réactive l'apparition du carré








    # Détection d'évènement(s)
    pygame.display.flip()
    for evenement in pygame.event.get():
        # Si l'utilisateur clique sur la fermeture de la fenêtre, on ferme pygame
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evenement.type == pygame.KEYDOWN:                    #Cette boucle sert à faire déplacer les deux barres rouges
            if evenement.key == pygame.K_UP and h1>10:          #Si on est dans la zone de jeu et qu'on appuis sur flèche du haut, on fait monter la barre horizontal
                h1=h1-10
            elif evenement.key == pygame.K_DOWN and h1<290:     #Si on est dans la zone de jeu et qu'on appuis surflèche du bas,on fait descendre la barre horizontal
                h1=h1+10
            elif evenement.key == pygame.K_LEFT and l1>5:       #Si on est dans la zone de jeu et qu'on appuis sur fleche gauche,on déplace à gauche la barre vertical
                l1=l1-10
            elif evenement.key == pygame.K_RIGHT and l1<290:    #Si on est dans la zone de jeu et qu'on appuis sur fleche droite, on déplace à droite la barre vertical
                l1=l1+10
            deplacement=deplacement+1

    if score >= 5:
        while True:
            pygame.display.flip()
            mafenetre.fill((0,0,0))
            text_ecran_fin = police.render (" Bravo tu as atteint " + str(score) + " points en " + str(temps_ecoule) + " secondes !" , True , (255,255,255) )
            text_fin_dep = police.render ("En " + str(deplacement) + " déplacements !" , True , (255,255,255))
            mafenetre.blit(text_ecran_fin,(20,150))
            mafenetre.blit(text_fin_dep,(80,170))

            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()