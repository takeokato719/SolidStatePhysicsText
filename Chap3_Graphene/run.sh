pw.x < graphene.scf.in > graphene.scf.out
echo 'Band calculation will start. It may take a few minites.'
pw.x < graphene.nscf.in > graphene.nscf.out
bands.x < graphene.band.in > graphene.band.out
python3 band.py > band.dat
gnuplot band.plt
echo 'band.eps is generated.'
evince band.eps &

