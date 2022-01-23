import math
import cmath
import numpy as np

def ene(kx,ky,kz):
    Es = 0.0
    Ep = 7.2
    Vss = -8.13
    Vsp = 5.88
    Vpp1 = 1.71
    Vpp2 = 7.51
    e1 = cmath.exp(1j*0.25*( kx+ky+kz))
    e2 = cmath.exp(1j*0.25*( kx-ky-kz))
    e3 = cmath.exp(1j*0.25*(-kx+ky-kz))
    e4 = cmath.exp(1j*0.25*(-kx-ky+kz))
    g0 = (e1 + e2 + e3 + e4)/4.;
    g1 = (e1 + e2 - e3 - e4)/4.;
    g2 = (e1 - e2 + e3 - e4)/4.;
    g3 = (e1 - e2 - e3 + e4)/4.;
    H = np.zeros((8, 8), dtype=np.complex)
    H[0][0] = Es
    H[1][1] = Ep
    H[2][2] = Ep
    H[3][3] = Ep
    H[4][4] = Es
    H[5][5] = Ep
    H[6][6] = Ep
    H[7][7] = Ep
    H[0][4] = g0*Vss
    H[0][5] = g1*Vsp
    H[0][6] = g2*Vsp
    H[0][7] = g3*Vsp
    H[1][4] =-g1*Vsp
    H[1][5] = g0*Vpp1
    H[1][6] = g3*Vpp2
    H[1][7] = g2*Vpp2
    H[2][4] =-g2*Vsp
    H[2][5] = g3*Vpp2
    H[2][6] = g0*Vpp1
    H[2][7] = g1*Vpp2
    H[3][4] =-g3*Vsp
    H[3][5] = g2*Vpp2
    H[3][6] = g1*Vpp2
    H[3][7] = g0*Vpp1
    for i in range(4):
        for j in range(4):
            H[j+4][i] = H[i][j+4].conjugate()        
    return np.linalg.eigh(H)
        
kpoints = []
kpoints.append([ 0.5  , 0.5  , 0.5  , 40]) # L
kpoints.append([ 0.0  , 0.0  , 0.0  , 60]) # Gamma
kpoints.append([ 0.0  , 0.5  , 0.5  , 20]) # X
kpoints.append([ 0.0  , 0.375, 0.625, 60]) # U,K
kpoints.append([ 0.0  , 0.0  , 1.0  , 40]) # Gamma

kaxis = 0.0
for i in range(len(kpoints)-1):
    kxs = kpoints[i  ][0]
    kxe = kpoints[i+1][0]
    kys = kpoints[i  ][1]
    kye = kpoints[i+1][1]
    kzs = kpoints[i  ][2]
    kze = kpoints[i+1][2]
    nk  = kpoints[i][3]    
    pxs = -kxs+kys+kzs
    pys =  kxs-kys+kzs
    pzs =  kxs+kys-kzs
    pxe = -kxe+kye+kze
    pye =  kxe-kye+kze
    pze =  kxe+kye-kze
    pxh = (pxe-pxs)/float(nk)
    pyh = (pye-pys)/float(nk)
    pzh = (pze-pzs)/float(nk)
    ph = math.sqrt(pxh**2 + pyh**2 + pzh**2)
    energy_levels = []
    karray = []
    for j in range(nk+1):
        kx = 2.*math.pi*(pxs + pxh*float(j))
        ky = 2.*math.pi*(pys + pyh*float(j))
        kz = 2.*math.pi*(pzs + pzh*float(j))
        e,w = ene(kx,ky,kz)
        energy_levels.append(e)
        karray.append(kaxis+ph*float(j))

    for j in range(8):
        for i in range(nk+1):
            print("{} {}".format(karray[i],energy_levels[i][j]-5.49))
        print("")
    kaxis = kaxis + ph*nk
        


