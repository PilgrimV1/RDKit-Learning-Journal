from rdkit import Chem

m = Chem.MolFromMolFile('molfiles/MolView.mol') # get a mol file from MolView.org website
print(Chem.MolToSmiles(m))

Chem.MolToSmiles(m,isomericSmiles=False)        # removing the isomericSmiles