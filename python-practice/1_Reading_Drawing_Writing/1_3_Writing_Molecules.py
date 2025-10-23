from rdkit import Chem

m = Chem.MolFromMolFile('molfiles/Pyridine.mol') # get a mol file from MolView.org website
print(Chem.MolToSmiles(m))

print(Chem.MolToSmiles(m,isomericSmiles=False))


# removing the isomericSmiles... thought the SMILES provided is canonical so it should print out the same result no matter how a 
# particular molecule is input
print(Chem.MolToSmiles(Chem.MolFromSmiles('C1=CC=CN=C1')))
print(Chem.MolToSmiles(Chem.MolFromSmiles('c1cccnc1')))
print(Chem.MolToSmiles(Chem.MolFromSmiles('n1ccccc1')))
