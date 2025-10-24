from rdkit import Chem

# Multiple molecules can be written to a file via

with Chem.SDWriter('Sdf_files/chebi_test1.sdf') as w:
    for m in mols:
        w.write(m)