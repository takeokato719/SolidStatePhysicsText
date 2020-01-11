import math

def energy(kx,ky):
    sq3 = math.sqrt(3.0)
    fr = math.cos(kx*0.5 + ky*0.5*sq3) + math.cos(kx*0.5 - ky*0.5*sq3) + math.cos(-kx)
    fi = math.sin(kx*0.5 + ky*0.5*sq3) + math.sin(kx*0.5 - ky*0.5*sq3) + math.sin(-kx)
    return math.sqrt(fr*fr + fi*fi)

D = 8.3738
nd = 100
for i in range(nd+1):
    x = float(i)/float(nd)
    kx = 2.*math.pi/3.*x
    ky = 2.*math.pi/3./math.sqrt(3.)*x
    ene = energy(kx,ky)*D/3.
    print('{} {}'.format(x*2./3.,-ene))

for i in range(nd):
    x = float(i+1)/float(nd)
    kx = 2.*math.pi/3.
    ky = 2.*math.pi/3./math.sqrt(3.)*(1.0-x)
    ene = energy(kx,ky)*D/3.
    print('{} {}'.format((2.+x)/3.,-ene))

for i in range(nd):
    x = float(i+1)/float(nd)
    kx = 2.*math.pi/3.*(1.0-x)
    ky = 0.
    ene = energy(kx,ky)*D/3.
    print('{} {}'.format(1.+x/math.sqrt(3.),-ene))
print('\n')
    
for i in range(nd+1):
    x = float(i)/float(nd)
    kx = 2.*math.pi/3.*x
    ky = 2.*math.pi/3./math.sqrt(3.)*x
    ene = energy(kx,ky)*D/3.
    print('{} {}'.format(x*2./3.,ene))

for i in range(nd):
    x = float(i+1)/float(nd)
    kx = 2.*math.pi/3.
    ky = 2.*math.pi/3./math.sqrt(3.)*(1.0-x)
    ene = energy(kx,ky)*D/3.
    print('{} {}'.format((2.+x)/3.,ene))

for i in range(nd):
    x = float(i+1)/float(nd)
    kx = 2.*math.pi/3.*(1.0-x)
    ky = 0.
    ene = energy(kx,ky)*D/3.
    print('{} {}'.format(1.+x/math.sqrt(3.),ene))
