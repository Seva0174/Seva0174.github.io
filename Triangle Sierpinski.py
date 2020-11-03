import turtle
turtle.tracer(0,0)            # accÃ©lÃ©ration du tracÃ©
turtle.screensize(2000,2000)  # taille fenÃªtre graphique
turtle.pu()
turtle.goto(-500,0)
turtle.pd()

def dessiner(courbe, longueur, angle):
    """ rÃ©alise une reprÃ©sentation graphique d'une courbe donnÃ©e par des chaines de caractÃ¨res """
    for caractere in courbe:
        if caractere == '+': turtle.left(angle)
        elif caractere == '-': turtle.right(angle)
        elif caractere in ['F', 'G']: turtle.forward(longueur)


#dessiner('F', 50, 60)

def regleKoch(chaine):
    nouvelleChaine = ''    # on crÃ©e une nouvelle chaine de caractÃ¨res VIDE
    for lettre in chaine:  # on Ã©pelle la chaine de caractÃ¨res donnÃ©e en paramÃ¨tres
        if lettre == 'F':  # si dans l'ancienne chaine, il y a un 'F'
            nouvelleChaine = nouvelleChaine + 'F-G+F+G-F'  # alors, on Ã©crit F+F--F+F dans la nouvelle chaine
        else :
            nouvelleChaine = nouvelleChaine + lettre  # sinon, on reporte la lettre telle quelle
        if lettre=='G':
            nouvelleChaine = nouvelleChaine + 'GG'
        else:
            nouvelleChaine = nouvelleChaine + lettre
    return nouvelleChaine


def courbeKoch(motifInitial, niter):
    """
        appelle niter fois regleKoch pour crÃ©er la courbe de Koch
    """
    courbe = 'F-G-G' # on part du motif initial donnÃ© par l'utilisateur en paramÃ¨tres
    for i in range(niter):
        nouveauMotif = regleKoch(courbe)  # on trouve le nouveau Motif Ã  partir du motif de dÃ©part
        courbe = nouveauMotif # on dit que le nouveau Motif est maintenant le motif de dÃ©part
    return courbe



#courbe = courbeKoch('F',3)
#dessiner(courbe,50, 60)

def flocon(motifInitial, niter):
    courbe = courbeKoch(motifInitial, niter)
    flocon = ''
    for _ in range(3):
        flocon += courbe
        flocon += '--'
    return flocon

longueur = 10
angle = 120
niter =6
dessiner(courbeKoch('F',niter), longueur, angle)


turtle.update()      # accÃ©lÃ©ration du tracÃ©
turtle.exitonclick() # permet la fermeture de la fenÃªtre graphique