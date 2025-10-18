"""
Make sure to implement a conda environment 
so you can ensure both Python, RDKit and libraries 
are in compatible versions.

You must activate the conda environment via the command on linux:
conda activate rdkit-env
"""

from rdkit import Chem          #loads important functions, "Chem" is the core library working with Python
from rdkit.Chem import Draw     #rdkit.Chem

# Construct Molecule from SMILES Formula directly
m = Chem.MolFromSmiles('Cc1ccccc1')

# Draw the Image
img = Draw.MolToImage(m)
img.show()      # To Show the Image

m2 = Chem.MolFromSmiles('c1cc1') #Will display "Can't kekulize mol" as the formula is incorrect. Also shows the Unkekulized atoms


