#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：MyTools
@File ：ela.py
@Author ：RongYi
@Date ：2025/6/19 16:46
@E-mail ：2071914258@qq.com
"""
from wizard.calculator import MaterialCalculator
from wizard.atoms import SymbolInfo
from calorine.calculators import CPUNEP


layers = 4
# symbol_info = SymbolInfo('Al', 'fcc', 4.05)
symbol_info = SymbolInfo('Mg', 'hcp', 3.17, 5.14)
atoms = symbol_info.create_bulk_atoms()
calc = CPUNEP('nep.txt')
# calc = CPUNEP('./UNEP-v1-main.txt')
material_calculator = MaterialCalculator(atoms, calc, symbol_info)

# material_calculator.lattice_constant()
# material_calculator.elastic_constant()
material_calculator.eos_curve()
#
##  空位形成能
material_calculator.formation_energy_vacancy()
#
# # 空位迁移能
# material_calculator.migration_energy_vacancy()
#
# # 双空位形成能
# nth = 1
# material_calculator.formation_energy_divacancies(nth)
#
# # 自间隙形成能
# vector = (1, 1, 1)
# material_calculator.formation_energy_sia(vector)
#
# # 间隙原子形成能
# material_calculator.formation_energy_interstitial_atom('Al', [0, 0, 1/2],
#                                                        'octahedral')

# 表面能
# material_calculator.formation_energy_surface((1, 0, 0), layers=layers)
# material_calculator.formation_energy_surface((1, 1, 0), layers=layers)
# material_calculator.formation_energy_surface((1, 1, 1), layers=layers)
# material_calculator.formation_energy_surface((2, 1, 0), layers=layers)
# material_calculator.formation_energy_surface((2, 1, 1), layers=layers)
# material_calculator.formation_energy_surface((2, 2, 1), layers=layers)
# material_calculator.formation_energy_surface((3, 1, 0), layers=layers)
# material_calculator.formation_energy_surface((3, 1, 1), layers=layers)
# material_calculator.formation_energy_surface((3, 2, 0), layers=layers)
# material_calculator.formation_energy_surface((3, 3, 1), layers=layers)

# Mg
material_calculator.formation_energy_surface((1, 0, -1), layers=layers)
material_calculator.formation_energy_surface((2, 1, -3), layers=layers)
material_calculator.formation_energy_surface((2, -1, -1), layers=layers)
material_calculator.formation_energy_surface((2, 2, -4), layers=layers)
material_calculator.formation_energy_surface((1, 1, 2), layers=layers)

# 层错能
# lattice = 4.05
# material_calculator.stacking_fault(a=(1, 1, -1), b=(1, -1, 0), miller=[1, 1, 1], distance=lattice)

# # 声子
# material_calculator.phonon_dispersion()

