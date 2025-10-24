# Self Study Notes for the RDKit Library


# Chapter 1

**To import the RDKit library you need to use the command:**

- from *rdkit* \

And use modules

- from rdkit import *Chem* \
This imports the Chem module of RDKit. To load and save molecules. Handle atoms, bonds and rings and read or write molecules |
- from rdkit import Draw \
imports the functions to visualize molecules into .svg or .jpg

- **Commands in the *Chem* module:**

| Syntax      | Description |
| ----------- | ----------- |
| Chem.MolFromSmiles('') & MolFromMolFile(''), etc,.. | Responsible for loading molecules  |
| mol.getAtoms() & mol.getBonds()  | handle atoms, bonds and rings|
| Chem.MolToSmiles(mol) | *or any variables can be used instead of mol... (like m for mol or even a)* to use and read the molecule | 
| Chem.MolFromMolFile(), Chem.SDWriter() | Reads and writes molecular files |

- **Commands in the *Draw* module:**

| Syntax      | Description |
| ----------- | ----------- |
| Chem.*MolToImage()* | Reveals the compound *(make sure to use img.show() to reveal the compound)* |