from rdkit import Chem

# Multiple molecules can be written to a file via
# 3 examples of molecules then placed into an array

m1 = Chem.MolFromSmiles('CC(=O)OC1=CC=CC=C1C(=O)O')     # Aspirin
m2 = Chem.MolFromSmiles('C([C@@H](C(=O)O)N)S')          # Cystein
m3 = Chem.MolFromSmiles('CCCCC(=O)O')                   # Valeric Acid


mols = [m1, m2, m3]

with Chem.SDWriter('Sdf_files/1_4_Set1.sdf') as w:      # To create the file and name it
    for m in mols:
        w.write(m)


# How to intialize an SD

from io import StringIO   # io (standard Python Module) that provides classes and functions for handling input/output (I/O)

'''
StringIO is a class that creates an object behaving similar to a file, except:
- It stores its contents on a string(in memory) instead of on a disk
- you can write to it, read from it, seek and close it ... like a file handle
'''

sio = StringIO()        # Creates an in-memory file (basically an object you can store) by using the "data = sio.getvalue()" after using sio.write() and then promptly using print("data captured:", data)
with Chem.SDWriter(sio) as w:
    for m in mols:
        w.write(m)
print(sio.getvalue())   # 