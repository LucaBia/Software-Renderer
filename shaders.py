# from gl import *
from mathLib import *
import random


# http://www.lighthouse3d.com/tutorials/glsl-12-tutorial/toon-shader-version-ii/
def toon(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tax, tbx, tcx, tay, tby, tcy = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tax * u + tbx * v + tcx * w
        ty = tay * u + tby * v + tcy * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = (nx, ny, nz)

    intensity = dot(normal, render.lightX,render.lightY,render.lightZ)

    if (intensity >= 0 and intensity <= 0.15):
        intensity = 0.3
    elif (intensity > 0.15 and intensity <= 0.3):
        intensity = 0.45
    elif (intensity > 0.3 and intensity <= 0.45):
        intensity = 0.6
    elif (intensity > 0.45 and intensity <= 0.6):
        intensity = 0.8
    elif (intensity > 0.6 and intensity <= 0.85):
        intensity = 0.9
    # elif (intensity > 0.9 and intensity<= 1):
    #     intensity = 1
    elif (intensity > 0.85):
        intensity = 1
    else:
        intensity = 0

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

# Intento de goooch shader
# https://rendermeapangolin.wordpress.com/2015/05/07/gooch-shading/
def gooch(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tax, tbx, tcx, tay, tby, tcy = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tax * u + tbx * v + tcx * w
        ty = tay * u + tby * v + tcy * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = (nx, ny, nz)

    intensity = dot(normal, render.lightX,render.lightY,render.lightZ )

    # diffuse
    a = 0.2
    b = 0.6

    it = ((1 + intensity) / 2)

    p1 = 1 -it

    p2_1, p2_2, p2_3 = p1 * 0, p1 * 0, p1 * 0.4
    # p2 = (p2_1, p2_2, p2_3)

    p3_1, p3_2, p3_3 = p2_1 + a, p2_2 + a, p2_3 + a
    # p3 = (p3_1, p3_2, p3_3)

    p4_1, p4_2, p4_3 = p3_1 * render.bitmap_color[0], p3_2 * render.bitmap_color[1], p3_3 * render.bitmap_color[2]
    # p4 = (p4_1, p4_2, p4_3)

    p5_1, p5_2, p5_3 = it * 0.4, it * 0.4, it * 0
    # p5 = (p5_1, p5_2, p5_3)

    p6_1, p6_2, p6_3 = b * render.bitmap_color[0], b * render.bitmap_color[1], b * render.bitmap_color[2]
    # p6 = (p6_1, p6_2, p6_3)

    # itColor = p4 + p5 + p6
    itColorX, itColorY, itColorZ = p4_1 + p5_1 + p6_1, p4_2 + p5_2 + p6_2, p4_3 + p5_3 + p6_3
    # itColor = (itColorX, itColorY, itColorZ)

    if intensity > 0.8:
        b *= 0.4
        g *= 0.4
        r *= 0.4
    else:
        b *= itColorX
        g *= itColorY 
        r *= itColorZ


    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def static(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tax, tbx, tcx, tay, tby, tcy = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tax * u + tbx * v + tcx * w
        ty = tay * u + tby * v + tcy * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = (nx, ny, nz)

    intensity = dot(normal, render.lightX,render.lightY,render.lightZ )

    b *= intensity
    g *= intensity
    r *= intensity

    # Un numero entero random entre 1 y 5 
    randomNumber = random.randint(1, 5)

    # Si el numero random es mayor o igual a 4 entonces (2 posibiilidades) se pinta rgb
    if (intensity > 0 and randomNumber >= 4):
        return r, g, b
    # de lo contrario se pinta negro (3 posiilidades, de manera que se vea mas puntos negros)
    else:
        return 0,0,0

def sand(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tax, tbx, tcx, tay, tby, tcy = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tax * u + tbx * v + tcx * w
        ty = tay * u + tby * v + tcy * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = (nx, ny, nz)

    intensity = dot(normal, render.lightX,render.lightY,render.lightZ )

    b *= intensity
    g *= intensity
    r *= intensity
 
    randomNumber = random.randint(1, 5)

    if (intensity > 0 and randomNumber >= 2):
        return r, g, b
    elif (intensity > 0 and randomNumber == 1):
        # Field sand color
        return 0.501, 0.314, 0.235
    else:
        return 0.250, 0.145, 0.118

def moss(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tax, tbx, tcx, tay, tby, tcy = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tax * u + tbx * v + tcx * w
        ty = tay * u + tby * v + tcy * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = (nx, ny, nz)

    intensity = dot(normal, render.lightX,render.lightY,render.lightZ)

    b *= intensity
    g *= intensity
    r *= intensity

    if (intensity >= 0.1 and intensity <= 0.4 and tax > 0.4 and tbx > 0.4 and tcx > 0.4 and tay > 0.5 and tby > 0.5 and tcy > 0.5):
        return r*0.2, g*0.4, b*0


    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def phong (render, **kwargs):
    u, v, w = kwargs['baryCoords']
    taX, tbX, tcX, taY, tbY, tcY = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g ,r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # ta, tb, tc = texcoords
        tx = taX * u + tbX * v + tcX * w
        ty = taY * u + tbY * v + tcY * w

        texColor = render.active_texture.getColor(tx, ty)

        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255
    
    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = (nx, ny, nz)
    # print("shaders: ", normal)
    intensity = dot(normal, render.lightX, render.lightY, render.lightZ)

    r *= intensity
    g *= intensity
    b *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0

def normalMap(render, **kwargs):
    Ax, Bx, Cx, Ay, By, Cy, Az, Bz, Cz = kwargs['verts']
    A, B, C = kwargs['vecVerts']
    u, v, w = kwargs['baryCoords']
    taX, tbX, tcX, taY, tbY, tcY = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g ,r = kwargs['color']

    # A = (Ax, Ay, Az)
    # B = (Bx, By, Bz)
    # C = (Cx, Cy, Cz)

    ta = (taX, taY)
    tb = (tbX, tbY)
    tc = (tcX, tcY)

    b /= 255
    g /= 255
    r /= 255

    tx = taX * u + tbX * v + tcX * w
    ty = taY * u + tbY * v + tcY * w

    if render.active_texture:
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w
    normal = (nx, ny, nz)

    if render.active_normalMap:
        texNormal = render.active_normalMap.getColor(tx, ty)
        texNormal = [ (texNormal[2] / 255) * 2 - 1,
                      (texNormal[1] / 255) * 2 - 1,
                      (texNormal[0] / 255) * 2 - 1]

        texNormal = div(texNormal, frobeniusNorm(texNormal))

        # B - A
        edge1 = sub(B[0], A[0], B[1], A[1], B[2], A[2])
        # C - A
        edge2 = sub(C[0], A[0], C[1], A[1], C[2], A[2])
        # tb - ta 
        deltaUV1 = sub2(tb[0], ta[0], tb[1], ta[1])
        # tc - ta
        deltaUV2 = sub2(tc[0], ta[0], tc[1], ta[1])

        tangent = [0,0,0]
        f = 1 / (deltaUV1[0] * deltaUV2[1] - deltaUV2[0] * deltaUV1[1])
        tangent[0] = f * (deltaUV2[1] * edge1[0] - deltaUV1[1] * edge2[0])
        tangent[1] = f * (deltaUV2[1] * edge1[1] - deltaUV1[1] * edge2[1])
        tangent[2] = f * (deltaUV2[1] * edge1[2] - deltaUV1[1] * edge2[2])
        tangent = div(tangent, frobeniusNorm(tangent))
        tangent = div(tangent, frobeniusNorm(tangent))
        tangent = subVectors(tangent, multiply(dot(tangent, normal[0], normal[1], normal[2]), normal))
        tangent = tangent / frobeniusNorm(tangent)

        bitangent = cross(normal, tangent)
        bitangent = bitangent / frobeniusNorm(bitangent)


        tangentMatrix = [
            [tangent[0],bitangent[0],normal[0]],
            [tangent[1],bitangent[1],normal[1]],
            [tangent[2],bitangent[2],normal[2]]
        ]

        light = render.light
        light = multiplyVM(light, tangentMatrix)
        light = div(light, frobeniusNorm(light))

        intensity = dot(texNormal, light[0], light[1], light[2])
    else:
        intensity = dot(normal, render.light[0], render.light[1], render.light[2])

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0



