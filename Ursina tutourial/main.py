from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Voxel(Button):
  def __init__(self, position = (0,0,0)):
    super().__init__(
      parent = scene,
      position = position,
      model = 'cube',
      originy = 0.5,
      texture = 'white_cube',
      color = color.color(0,0,random.uniform(0.9,1)),
      highlight_color = color.lime,
      )
  def input(self, key):
    if self.hovered:
      if key == "left mouse down":
        voxel = Voxel(position = (self.position + mouse.normal))
      if key == "right mouse down":
        destroy(self)
    
    

    
app = Ursina()

for z in range(15):
  for x in range(15):
    voxel = Voxel(position = (x, 0, z))
    
def update():
  if held_keys['r']:
    player.x = 0
    player.z = 0
    player.y = 10
    
player = FirstPersonController()
player.y = 1

app.run()

