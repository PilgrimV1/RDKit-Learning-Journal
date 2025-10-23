from rdkit import Chem

m = Chem.MolFromMolFile('molfiles/Pyridine.mol') # get a mol file from MolView.org website
print(Chem.MolToSmiles(m))

print(Chem.MolToSmiles(m,isomericSmiles=False))


# removing the isomericSmiles... thought the SMILES provided is canonical so it should print out the same result no matter how a 
# particular molecule is input
m1 = Chem.MolToSmiles(Chem.MolFromSmiles('C1=CC=CN=C1'))
m2 = Chem.MolToSmiles(Chem.MolFromSmiles('c1cccnc1'))
m3 = Chem.MolToSmiles(Chem.MolFromSmiles('n1ccccc1'))

if (m1 == m2 == m3):
    print("m1, m2 and m3 notations are the same!")  # If m1, m2 and m3 are the same this message will appear
else:
    print("m1, m2 and m3 notations are different")

# Kekulize the SMILES formulas here:

Chem.Kekulize(m)
print(Chem.MolToSmiles(m, kekuleSmiles=True))

# MDL mol blocks


m4 = Chem.MolFromSmiles('C1CCC1')   # Molecule made from the SMILES Formula
m4.SetProp("_Name","cyclobutane")   
# Sets the molecules name property, must come after the variable m4 was set first (will display cyclobutane now)
print(Chem.MolToMolBlock(m4))       # turned into blocks for the molfiles


'''
The mol block needs to have atomic coordinates.
In order for the atom or bond stereochemistry to be read correctly by most software.
It is also practical for reasons such as drawing molecules. Generating a mol block
will by default generate coordinates. (These are not stored with the molecule however.)
'''

# Including 2D Coordinates below

from rdkit.Chem import AllChem
AllChem.Compute2DCoords(m4)          # Shows the 2D coordinates for the compound

print(Chem.MolToMolBlock(m4))

# Include the 3D Coordinates below
m5 = Chem.AddHs(m4)
params = AllChem.ETKDGv3()
params.randomSeed = 0xf00d
AllChem.EmbedMolecule(m3, params)