echo 'Band calculation will start. It may take a few minites.'
pw.x < NaCl.scf.in > NaCl.scf.out
pw.x < NaCl.nscf.in > NaCl.nscf.out
bands.x < NaCl.band.in > NaCl.band.out
gnuplot NaCl.band.plt
echo 'NaCl.band.eps is generated.'
