# Self Study Notes for RDKit

Chapter 1

- from rdkit import Chem  
imports the Chem module of RDKit. To load and save molecules. Handle atoms, bonds and rings and read or write molecules


- Commands: 
Chem.MolFromSmiles('')   (Loading molecules.... also MolFromMolFile etc,....)\
Chem.MolToSmiles(mol)    (Or any variable can be used.. like m for mol or... a.... this is used to save the molecule)\
mol.getAtoms() and mol.getBonds()   (Handle atoms and bonds and rings)\
Chem.MolFromMolFile(), Chem.SDWriter() (Read and write molecular files)\

- from rdkit import Draw 
imports the functions to visualize molecules into .svg or .jpg

- Command(s):
- Chem.MolToImage()   (then use img.show() to reveal the compound)


| This   | is    | a       |
| ------ | ----- | ------- |
| simple | table | example |