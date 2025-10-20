"""
Make sure to implement a conda environment 
so you can ensure both Python, RDKit and libraries 
are in compatible versions.

You must activate the conda environment via the command on linux:
conda activate rdkit-env
"""

from rdkit import Chem          # loads important functions, "Chem" is the core library working with Python
from rdkit.Chem import Draw     # rdkit.Chem

# Construct Molecule from SMILES Formula directly
m = Chem.MolFromSmiles('Cc1ccccc1')

img = Draw.MolToImage(m) # Draw the Image
img.show()      # To Show the Image

m1 = Chem.MolFromSmiles('CO(C)C') # Explicit valence for atom # 1 0, 3 is greater permitted (SMILES Formula does not exist)

m2 = Chem.MolFromSmiles('c1cc1')  # Will display "Can't kekulize mol" as the formula is incorrect. Also shows the Unkekulized atoms

# In each case of m1 and m2 the value "None" is returned 

#m1 is None 
print(m1 is None) # Outputs "True" because the value of "None" was returned

#m2 is None 
print(m2 is None) # Outputs "True" because the value of "None" was returned as well

print(m is None) # Will output "False" because m had a viable SMILES formula