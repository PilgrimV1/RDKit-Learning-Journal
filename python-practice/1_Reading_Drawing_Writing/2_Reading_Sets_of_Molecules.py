import os
script_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(script_dir, '..', '..'))
os.chdir(project_root)


sdf_path = 'Sdf_files/chebi_test1.sdf'
print("Absolute path:", os.path.abspath(sdf_path))
print("Exists?", os.path.exists(sdf_path))

from rdkit import Chem 


# The .sdf file is not a given but you have to extract it from another repo
suppl = Chem.SDMolSupplier('Sdf_files/chebi_test1.sdf')   # suppl being the variable you can name... in reality it can be anything you name it 
for mol in suppl:                              # mol standing for the molecules in the suppl variable.. variable within the overall 
    print(mol.GetNumAtoms(), '\n')                   # GetNumAtoms() function shows the number of Atoms within the Chemical Compound.. the print() function prints it on the terminal

mols = [x for x in suppl]
len(mols)
print(len(mols), '\n')        # prints the number of items within an object (or number of characters within the string but in this case the file object)

print(suppl[0].GetNumAtoms(), '\n') # random access to suppl, in its last state it was left in [0] prints out 21 and [1] prints out 11


# Another method to print out the same results of the Chem.SDMolSupplier() method
with Chem.SDMolSupplier('Sdf_files/chebi_test1.sdf') as suppl: 
    for mol in suppl:
        if mol is None: continue
        print(mol.GetNumAtoms(), '\n')  # \n space between print outs


# Alternate type of supplier with 'rb', to read from file-like objects

inf = open('Sdf_files/chebi_test1.sdf', 'rb')
with Chem.ForwardSDMolSupplier(inf) as fsuppl:
    for mol in fsuppl:
        if mol is None: continue
        print(mol.GetNumAtoms(), '\n')

# gzip compression
# linux code line: gzip Sdf_files/chebi_test1.sdf
# This will compress the file into a .gz file

import gzip
inf = gzip.open('Sdf_files/chebi_test.sdf.gz')
with Chem.ForwardSDMolSupplier(inf) as gzsuppl:
    ms = [x for x in gzsuppl if x is None]
print(len(ms))