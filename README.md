# 0x00. AirBnB clone - The console

Welcome to the AirBnB clone project! (The Holberton B&B)
![AirBnB clone logo](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUZGDONYM4%2F20200220%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200220T041738Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=036ae4144de1edbdef5a2d5a73e3d72a445fb4806075e8bd53c2151f569311cc)

## Description
This is the first step towards building your first full web application: the **AirBnB clone**. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…
Each task is linked and will help you to:

* put in place a parent class (called **BaseModel**) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

## What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

---

## Execution
Shell work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
----------------------------------------
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

But also in non-interactive mode:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
----------------------------------------
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
----------------------------------------
EOF  help  quit
(hbnb)
$

---

## Commands
These are the interpreter commands:

### quit
* Exit the program (also you can use EOF). **Usage:** quit


### help
* Show the documentation of a command and their documantacion status. **Usage:** help (for documantation status) - help <command name> (for comand documantation)


### create
* Creates a new instance of a HBNB class, saves it (to the JSON file) and prints the id. **Usage:** create <class name>


### show
* Prints the string representation of an instance based on the class name and id. **Usage:** show <class name> <instance id> or <class name>.show("<instance id>")


### destroy
* Deletes an instance based on the class name and id (save the change into the JSON file). **Usage:** destroy <class name> <instance id> or <class name>.destroy("<instance id>")


### all
* Prints all string representation of all instances based or not on the class name. **Usage:** all (for all instances), all <class name> or <class name>.all() (for all instances of a class)


### update
* Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). **Usage:** update <class name> <instance id> <attribute name> "<attribute value>" or <class name>.update(<instance id>, <attribute name>, <attribute value>) or <class name>.update(<instance id>, <dictionary representation>) (for update an instance based on his ID with a dictionary)

---

## Installing
Clone the repository of the project from Github. This repository contain the console and all classes.

* git clone https://github.com/Nzparra/AirBnB_clone.git

---

## Built
Ubuntu 14.04, Emacs, Vim and Python3.

---

## Authors
* **Nicolas Sanchez Parra** - [Nicolas Sanchez Parra](https://github.com/Nzparra)
* **Sebastian Chingate Cepeda** - [Sebastian Chingate Cepeda](https://github.com/sebastianchc)