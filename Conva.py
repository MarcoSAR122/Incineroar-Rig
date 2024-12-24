import bpy

#Funciones Extra
def ressum(lx):
    if lx < 0:
        return lx*-1
    else:
        return lx   
def asd(lz):
    if lz < 0:
        return lz
    else:
        return lz*-1

def tweakUp(lx,ly,lz,sy,salida):
    if ly < 0:
        salida += ly*10

    elif ly > 0:
        salida += ly*10
        
    else:
        salida = ly
    salida -= ((sy-1)-((ressum(lx)-asd(lz))*2))

    print(salida)
    return salida

#region Funciones que salen
def tweakDown(lx,ly,lz,sy,salida):
    if ly < 0:
        salida += ly*10

    elif ly > 0:
        salida += ly*10
        
    else:
        salida = ly
    salida += ((sy-1)-((ressum(lx)-asd(lz))*2))
    print(salida)
    return salida*-1


bpy.app.driver_namespace["TBUP"] = tweakUp
bpy.app.driver_namespace["TBDOWN"] = tweakDown