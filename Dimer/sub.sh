cd dimer_data

for i in {1..20}
do
cd ${i}
qsub vasp3.pbs
cd ..
done