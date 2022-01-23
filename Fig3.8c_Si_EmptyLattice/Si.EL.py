import math
import cmath
import numpy as np
import sys
import pprint

def ene(kx,ky,kz,mx,my,mz):
    x = (-kx+ky+kz) + float(-mx+my+mz)
    y = ( kx-ky+kz) + float( mx-my+mz)
    z = ( kx+ky-kz) + float( mx+my-mz)
    return x*x+y*y+z*z
        
kpoints = []
kpoints.append([ 0.5 , 0.5  , 0.5  , 40]) # L
kpoints.append([ 0.0 , 0.0  , 0.0  , 60]) # Gamma
kpoints.append([ 0.0 , 0.5  , 0.5  , 20]) # X
kpoints.append([ 0.0 , 0.375, 0.625, 60]) # U,K
kpoints.append([ 0.0 , 0.0  , 1.0  , 40]) # Gamma

Gpoints = []
#Gpoints.append([[0,0,0],[-1,-1,-1],[-1,0,0],[-1,-1,0],[0,0,1],[1,1,1],[0,1,1],[-2,-1,-1],[-2,-2,-1],[-2,-2,-2],[-1,0,1],[1,1,2],[-2,-1,0]]) # L --> Gamma
#Gpoints.append([[0,0,0],[0,-1,-1],[1,0,0],[-1,0,0],[-1,-1,0],[0,1,1],[-1,-2,-1],[-1,-2,-2],[-2,-1,-1],[-1,0,1]]) # Gamma --> X
#Gpoints.append([[0,0,0],[0,0,-1],[-1,-1,-1],[0,-1,0],[-1,-1,-2],[-1,-2,-1],[0,-1,-2],[-1,-2,-2],[0,-2,-1],[0,0,-2],[-1,0,-2]]) # X ---> U,K
#Gpoints.append([[0,0,-1],[0,0,0],[-1,-1,-1],[-1,-1,-2],[0,0,-1],[0,-1,0],[0,-1,-2],[-1,0,-2],[-1,-2,-2],[-1,-2,-1],[0,-2,-1],[-2,-1,-2],[-1,-1,-3],[0,1,-2]]) # U ---> Gamma
mmax = 4
emax = 9.0
tol = 0.00001
for i in range(len(kpoints)-1):
    kps = kpoints[i]
    kpe = kpoints[i+1]
    kxs = kps[0]
    kys = kps[1]
    kzs = kps[2]            
    kxe = kpe[0]
    kye = kpe[1]
    kze = kpe[2]            
    Garray = []
    for mx in range(-mmax,mmax+1):
        for my in range(-mmax,mmax+1):
            for mz in range(-mmax,mmax+1):
                d1 = ene(kxs,kys,kzs,mx,my,mz)
                d2 = ene(kxe,kye,kze,mx,my,mz)
                Garray.append([min([d1,d2]),d1,d2,mx,my,mz])
    Garray2 = sorted(Garray)
    j=0
    d1 = -1.0
    d2 = -1.0
    Garray3 = []
    while j<len(Garray2):
        G = Garray2[j]
        if G[0] < emax:
            if (math.sqrt((d1-G[1])**2+(d2-G[2])**2)>tol):
                Garray3.append([G[3],G[4],G[5]])
                d1 = G[1]
                d2 = G[2]
        j = j + 1
    Gpoints.append(Garray3)
#print(Gpoints)
#sys.exit()

kcount = 0
kaxis = 0.0
band_bottom = -11.8
a_in_Bohr = 5.46872800/0.529177210903
eV_at_X = 0.5*(2.*math.pi/a_in_Bohr)**2*27.2
for i in range(len(kpoints)-1):
    kxs = kpoints[i  ][0]
    kxe = kpoints[i+1][0]
    kys = kpoints[i  ][1]
    kye = kpoints[i+1][1]
    kzs = kpoints[i  ][2]
    kze = kpoints[i+1][2]
    nk  = kpoints[i][3]
    pxs = (-kxs+kys+kzs)
    pys = ( kxs-kys+kzs)
    pzs = ( kxs+kys-kzs)
    pxe = (-kxe+kye+kze)
    pye = ( kxe-kye+kze)
    pze = ( kxe+kye-kze)
    ph  = math.sqrt((pxe-pxs)*(pxe-pxs) + (pye-pys)*(pye-pys) + (pze-pzs)*(pze-pzs))/float(nk)
    kxh = (kxe-kxs)/float(nk)
    kyh = (kye-kys)/float(nk)
    kzh = (kze-kzs)/float(nk)
    Gp = Gpoints[i]
    energy_levels = []
    karray = []
    for j in range(nk+1):
        kx = kxs + kxh*float(j)
        ky = kys + kyh*float(j)
        kz = kzs + kzh*float(j)
        karray.append(kaxis+ph*j)
        eneset = []
        for G in Gp:
            eneset.append(ene(kx,ky,kz,G[0],G[1],G[2]))
        energy_levels.append(eneset)                
    for k in range(len(Gp)):
        for j in range(len(karray)):
            print("{} {}".format(karray[j]*0.4966*2.0,
                                 energy_levels[j][k]*eV_at_X+band_bottom))
        print("")
    kaxis = kaxis + ph*nk
    
