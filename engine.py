# Gian Luca Rivera - 18049

from gl import Render
from obj import Obj, Texture
from shaders import gooch, static, phong, toon, normalMap

# 3840 × 2160
bitmap = Render(3840, 2160)
# bitmap.glViewPort(0, 0, 3840 , 2160)

background = Texture('./background.bmp')
bitmap.pixels = background.pixels


bitmap.active_texture = Texture('./Models/Textures/Stormtrooper.bmp')
bitmap.active_normalMap = Texture('./Models/Textures/Stormtrooper_N.bmp')
bitmap.lookAt((1, 0, 5), (0,0,0))
bitmap.active_shader = normalMap
bitmap.loadObjModel('./Models/stormtrooper2.obj', (2600, 200, 0), (150, 150, 150), (0, -110, 0))

# bitmap.active_texture = Texture('./Models/Textures/Body_Diffuse.bmp')
# bitmap.active_shader = phong
# bitmap.loadObjModel('./Models/bb-unit.obj', (900, 300, 0), (1.5, 1.5, 1.5), (0, 30, 0))

# bitmap.active_texture = Texture('./Models/Textures/arc170fighter.bmp')
# bitmap.active_shader = phong
# bitmap.loadObjModel('./Models/Arc170.obj', (2300, 1700, 0), (0.5, 0.5, 0.5), (0, 180, 0))

# bitmap.active_texture = Texture('./Models/Textures/XWing2.bmp')
# bitmap.active_shader = phong
# bitmap.loadObjModel('./Models/X-Fighter.obj', (600, 1200, 0), (0.4, 0.4, 0.4), (0, 25, 0))

# bitmap.active_texture = Texture('./Models/Textures/R2D2_Diffuse.bmp')
# bitmap.active_shader = phong
# bitmap.loadObjModel('./Models/R2-Unit.obj', (3000, 200, 0), (2.5, 2.5, 2.5), (0, -110, 0))

# bitmap.active_texture = Texture('./Models/Textures/Water_Vaporator_Reflectivity.bmp')
# bitmap.active_shader = phong
# bitmap.loadObjModel('./Models/Vaporator.obj', (210, 280, 0), (3, 3, 3), (0, 0, 0))



bitmap.glFinish('output.bmp')
# bitmap.glZBuffer('outputZbuffer.bmp')

print("El bitmap se genero exitosamente, revisa la carpeta contenedora")




