echo 'Band calculation will start. It may take a few minites.'
pw.x < NaF.scf.in > NaF.scf.out
pw.x < NaF.nscf.in > NaF.nscf.out
bands.x < NaF.band.in > NaF.band.out
gnuplot NaF.band.plt
echo 'NaF.band.eps is generated.'
