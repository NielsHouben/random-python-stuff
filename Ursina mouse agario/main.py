from ursina import *

app = Ursina()


class Player(Entity):
  def __init__(self):
      super().__init__(
        parent = scene,
        model = "sphere",
        color = color.white  
      )



def update():
  print([app.mouse.position], [player.position])
  player.position = LVector3f(app.mouse.position.x, app.mouse.position.y, 0) 
  



player = Player()



app.run()


#giving up, ursina mouse.pos doesn't match player.pos, BULLSHIT