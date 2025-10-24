# Self Study Notes for the RDKit Library


# Chapter 1

**To import the RDKit library you need to use the command:**

- from *rdkit* 

**Commands for importing modules:**

- from rdkit import *Chem* 

This imports the Chem module of RDKit. To load and save molecules. Handle atoms, bonds and rings and read or write molecules.

- from *rdkit.Chem* import *Draw* 

Imports the functions to visualize molecules into .svg or .jpg. \
**!Important:** Make sure to use *rdkit.Chem* to import the Draw module!

- **Commands in the *Chem* module:**

| Syntax      | Description |
| ----------- | ----------- |
| Chem.**MolFromSmiles('')** & Chem.**MolFromMolFile('')**, etc,.. | Responsible for loading molecules  |
| mol.**getAtoms()** & mol.**getBonds()**  | handle atoms, bonds and rings (mol is just another variable.. you can use m)|
| Chem.**MolToSmiles(mol)** | *or any variables can be used instead of mol... (like m for mol or even a)* to use and read the molecule | 
| Chem.**MolFromMolFile()**, Chem.**SDWriter()** | Reads and writes molecular files |
| (Chem.**MolToMolBlock(*Variable*)**, **file=open**('python-practice/1_Reading_Drawing_Writing/PrintFile1.mol', **'w+'**))| To write a molecule to a file you can use Python file objects. This is used to create a file. *Make sure to use the print() command to encapsulate it* |

In open(filename, mode), the mode string controls two things: whether the file is for reading, writing, or both, and what happens if the file exists or doesn’t exist. \
- **'w' is *write only***. Creates the file if it doesn’t exist. Truncates (clears) it if it already exists.
- **'w+' is *write and read***. Creates the file if it doesn't exist. Truncates if it already exists.


- **Commands in the *Draw* module:**

| Syntax      | Description |
| ----------- | ----------- |
| Chem.**MolToImage()** | Reveals the compound *(make sure to use img.show() to reveal the compound)* |