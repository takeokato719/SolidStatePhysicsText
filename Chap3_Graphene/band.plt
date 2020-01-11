#!/usr/local/bin/gnuplot -persist
# Last modified: 2019/10/30 16:28
set terminal postscript eps enhanced 28 lw 2
set output "band.eps"
set size 2,1

set multiplot layout 1,2 rowsfirst downwards
set ylabel 'Energy (eV)'
set ytics 5
unset key
x1 = 0.66666666
x2 = 1
xmax = 1.5773
ymin = -20
ymax = 10
ef = -0.4661
set xrange [0:xmax]
set yrange [ymin:ymax]
set xtics ("{/Symbol G}" 0, "K" x1, "M" x2, "{/Symbol G}" xmax)
set arrow 1 nohead from x1,ymin to x1,ymax lt 2
set arrow 2 nohead from x2,ymin to x2,ymax lt 2
set arrow 3 nohead from 0,0 to xmax,0 lt 2
set title '(a) Tight-binding model'
set size 1
set origin 0,0
plot 'band.dat' using 1:2 w l
set title '(b) Band calculation'
set size 1
set origin 1,0
plot 'graphene.band.gnu' using 1:($2-ef) w l
unset multiplot
