from rdkit import Chem

m = Chem.MolFromSmiles('C1OC1')
for atom in m.GetAtoms():
    print(atom.GetAtomicNum())


print(m.GetBonds()[0].GetBondType())