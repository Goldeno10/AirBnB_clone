# AirBnB Clone Project - The Console

The console is the first segment of the AirBnB project at alx, a project will be undertaken in segments.
collectively all sections cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). 
A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

### Functionalities of this command interpreter:
- Create a new object (Ex: a new User, Place, State etc)
- Retrieve an object from a storage location(Ex: file, database etc...)
- Do operations on objects (count, compute stats, etc...)
- Update attributes of an object
- Destroy an object

This project was interpreted/tested on Ubuntu 14.04 LTS and Ubuntu 22.0 LTS using python3 (version 3.10.4)

## Installation
1. Clone this repository: `git clone "https://github.com/Goldeno10/AirBnB_clone.git"`
2. Access AirBnb directory: `cd AirBnB_clone`
3. Run hbnb(interactively): `./console` and enter command
4. Run hbnb(non-interactively): `echo "<command>" | ./console.py`

## The Console Commands
[console.py](https://github.com/Goldeno10/AirBnB_clone/blob/main/console.py) - the console contains the entry point of the command interpreter. List of commands this console current supports:

- `EOF` - exits the console
- `quit` - exits the console
- `<emptyline>` - overwrites default emptyline method and does nothing
- `create` - Creates a new instance of class_name, saves it (to the JSON file) and prints the id
- `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file).
- `show` - Prints the string representation of an instance based on the class name and id.
- `all` - Prints string representation of all instances based or not on the class name.
- `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
 
