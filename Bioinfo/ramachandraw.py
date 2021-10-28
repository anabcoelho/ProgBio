import os
import RamachanDraw as rd

rd.fetch ('1ubq')
#phi e psi
rd.phi_psi ('PDB/pdb1ubq.ent', True)

#plot
rd.plot("PDB/pdb1ubq.ent", cmap= 'viridis', alpha=0.75, dpi= 100, save=True, show=False)