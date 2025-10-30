from rdkit import Chem
from io import StringIO

m = Chem.MolFromSmiles('C1OC1')
for atom in m.GetAtoms():
    print(atom.GetAtomicNum())


print(m.GetBonds()[0].GetBondType())

# Requesting Individual Atoms or Bonds

print(m.GetAtomWithIdx(0).GetSymbol())

print(m.GetAtomWithIdx(0).GetExplicitValence())

print(m.GetBondBetweenAtoms(0,1).GetBondType())




# Atoms to keep track of their neighbors

atom = m.GetAtomWithIdx(0)
[x.GetAtomicNum() for x in atom.GetNeighbors()]

len(atom.GetNeighbors()[-1].GetBonds())