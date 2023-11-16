import turtle

def courbe_koch(n, l):
    if n == 0 :
        turtle.forward(l)
    else :
        courbe_koch(n-1, l/3)
        turtle.left(60)
        courbe_koch(n-1, l/3)
        turtle.left(-120)
        courbe_koch(n-1, l/3)
        turtle.left(60)
        courbe_koch(n-1, l/3)

courbe_koch(2,200)





def flocon(n,l,i=3):
    if i != 0: 
        courbe_koch(n,l)
        turtle.left(-120)
        flocon(n,l,i-1)

turtle.setheading(0) # orientation intiale de la tête : vers la droite de l'écran
turtle.hideturtle() # on cache la tortue
turtle.speed(0)	 # on accélère la tortue
turtle.color('green')
#flocon(2,300)
#courbe_koch(1,400)
print(8)

