from ase import Atoms
from ase.io import write
import os
import shutil


for i in range(1, 21):
    os.makedirs(f'./dimer_data/{i}')
    distance = 1 + i*0.1
    dimer = Atoms(symbols=['U',  'U'], positions=[(0, 0, 0), (0, 0, distance)], pbc=[True, True, True], cell=(20, 30, 40))
    write(f'./dimer_data/{i}/POSCAR', dimer, format='vasp')
    shutil.copy('./INCAR', f'./dimer_data/{i}/')
    shutil.copy('./POTCAR', f'./dimer_data/{i}/')
    shutil.copy('./vasp3.pbs', f'./dimer_data/{i}/')

os.system("sh sub.sh")


