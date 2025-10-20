from rdkit import Chem
from rdkit import Draw

suppl = Chem.SDMolSupplier('')
for mol in suppl:
    print(mol.GetNumAtoms)