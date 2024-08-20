from turtle import Turtle, done

# Possíveis formatos
# -> arrow (seta)
# -> blank (invisível)
# -> circle (círculo)
# -> classic (clássica)
# -> square (quadrado)
# -> triangle (triângulo)
# -> turtle (tartaruga)

donatello = Turtle()
donatello.shape("turtle")
donatello.color("dark green")
donatello.forward(100)
donatello.right(90)
donatello.forward(100)
donatello.right(90)
donatello.forward(100)
donatello.right(90)
donatello.forward(100)

jisooTurtleRabbitKim = Turtle()
jisooTurtleRabbitKim.color("purple")
jisooTurtleRabbitKim.shape("circle")
jisooTurtleRabbitKim.circle(50)

donatello.left(135)
donatello.forward(141.4)
donatello.left(135)
donatello.forward(130)

done()