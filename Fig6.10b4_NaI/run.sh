echo 'Band calculation will start. It may take a few minites.'
pw.x < NaI.scf.in > NaI.scf.out
pw.x < NaI.nscf.in > NaI.nscf.out
bands.x < NaI.band.in > NaI.band.out
gnuplot NaI.band.plt
echo 'NaI.band.eps is generated.'
