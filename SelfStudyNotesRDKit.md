# Self Study Notes for the RDKit Library


# Chapter 1

**To import the RDKit library you need to use the command:**

- from *rdkit* 

**Commands for importing modules:**

- from rdkit import *Chem* \
This imports the Chem module of RDKit. To load and save molecules. Handle atoms, bonds and rings and read or write molecules.
- from *rdkit.Chem* import *Draw* \
imports the functions to visualize molecules into .svg or .jpg \
**!Important:** Make sure to use *rdkit.Chem* to import the Draw module

- **Commands in the *Chem* module:**

| Syntax      | Description |
| ----------- | ----------- |
| Chem.*MolFromSmiles('')* & Chem.*MolFromMolFile('')*, etc,.. | Responsible for loading molecules  |
| mol.*getAtoms()* & mol.*getBonds()*  | handle atoms, bonds and rings (mol is just another variable.. you can use m)|
| Chem.*MolToSmiles(mol)* | *or any variables can be used instead of mol... (like m for mol or even a)* to use and read the molecule | 
| Chem.*MolFromMolFile()*, Chem.*SDWriter()* | Reads and writes molecular files |

- **Commands in the *Draw* module:**

| Syntax      | Description |
| ----------- | ----------- |
| Chem.*MolToImage()* | Reveals the compound *(make sure to use img.show() to reveal the compound)* |