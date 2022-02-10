#!/usr/local/bin/gnuplot -persist
# Last modified: 2019/10/30 16:28
set terminal postscript enhanced eps
set output "NaI.band.eps"
set size 0.3,1
unset key 

## *** Plot range ***
x1=0.8660
x2=1.8660
x3=2.21955
xmax=3.2802
set xrange [0:xmax]
set yrange [-3:15]

ef=0.9091

set xzeroaxis
set grid x

set ylabel "Energy (eV)"
set xtics ("{L}" 0, "{/Symbol G}" x1, "{X}" x2, "{K}" x3, "{/Symbol G}" xmax)

plot "NaI.band.gnu" u 1:($2-ef) w l
