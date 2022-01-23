echo 'Band calculation will start. It may take a few minites.'
pw.x < Si.scf.in > Si.scf.out
pw.x < Si.nscf.in > Si.nscf.out
bands.x < Si.band.in > Si.band.out
gnuplot Si.band.plt
echo 'Si.band.eps is generated.'
