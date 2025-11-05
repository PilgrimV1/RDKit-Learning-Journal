from rdkit import Chem

# You cna find information on the rings of a molecule in its atoms or bonds
# Atoms and Bonds both carry information about the molecule's rings:

m = Chem.MolFromSmiles('OC1C2C1CC2')

m.GetAtomWithIdx(0).IsInRing()

m.GetAtomWithIdx(1).IsInRing()

m.GetAtomWithIdx(2).IsInRing()


# Check whether an atom at a certain index point is within a certain ring size
m.GetAtomWithIdx(2).IsInRingSize(3)    

m.GetAtomWithIdx(2).IsInRingSize(4)

m.GetAtomWithIdx(2).IsInRingSize(5)

# But the information is only about the smallest rings!

m.getAtomwithIdx(1).IsInRingSize(5)

'''
Details about the smallest set of smallest rings (SSSR) is also available. via the Chem.GetSSSR() function. 
Where within the () you use the variable you set for the given molecule. In this case m.

The .GetSymmSSSR() function gets us the symmetrical SSSR


The .GetSSSR() function gets us the "true SSSR"
'''

ssr = Chem.GetSymmSSSR(m)       # Gets us the Symmetrical SSSR

len(ssr)   # Length from the Variable that was assigned for the smallest set of smallest rings

list(ssr[0])
list(ssr[1])

# in order to find out the length of the "True" SSSR

len(Chem.GetSSSR(m))


# For more efficient queries about a molecule’s ring systems (avoiding repeated calls to Mol.GetAtomWithIdx) use the rdkit.Chem.rdchem.RingInfo class

m.Chem.MolFromSmiles('OC1C2C1CC2')

ri = m.GetRingInfo()
ri.NumAtomRings(0)      # Number of Atom Rings at index 0. Should return 0.

ri.NumAtomRings(1)      # Number of Atom Rings at index 1. Should return 1 (given C1)

ri.NumAtomRings(2)      # Number of Atom Rings at index 2. Should return 2 (given C2)

ri.IsAtomInRingOfSize(1, 3)     # Asks Whether Atom at index 1 is in ring size of 3

ri.IsBondInRingOfSize(1, 3)     # Asks whether Bond at index 1 is in ring size of 3