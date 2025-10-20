from rdkit import Chem 


# The .sdf file is not a given but you have to extract it from another repo
suppl = Chem.SDMolSupplier('Sdf_files/chebi_test.sdf')   # suppl being the variable you can name... in reality it can be anything you name it 
for mol in suppl:                              # mol standing for the molecules in the suppl variable.. variable within the overall 
    print(mol.GetNumAtoms())                     # GetNumAtoms() function shows the number of Atoms within the Chemical Compound.. the print() function prints it on the terminal

    