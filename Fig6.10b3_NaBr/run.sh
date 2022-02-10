echo 'Band calculation will start. It may take a few minites.'
pw.x < NaBr.scf.in > NaBr.scf.out
pw.x < NaBr.nscf.in > NaBr.nscf.out
bands.x < NaBr.band.in > NaBr.band.out
gnuplot NaBr.band.plt
echo 'NaBr.band.eps is generated.'
