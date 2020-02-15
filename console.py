#!/usr/bin/python3
"""The AirBnb Console"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"
    my_classes = {"BaseModel", "Amenity", "Place", "State", "City",
                  "Review", "User"}

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Pass"""
        pass

    def do_EOF(self, line):
        """Quit command to exit the program at the end of file"""
        return True

    def do_create(self, line):
        """create"""
        try:
            if not line:
                raise SyntaxError()
            args = line.split()
            obj = eval("{}()".format(args[0]))
            obj.save()
            print("{}".format(obj.id))
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't sdst **")

    def do_show(self, line):
        try:
            if not line:
                raise SyntaxError()
            args = line.split()
            if args[0] not in self.my_classes:
                raise NameError()
            if len(args) < 2:
                raise IndexError()
            value = storage.all()
            key = args[0] + '.' + args[1]
            if key in value:
                print(value[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")
        except KeyError:
            print("** no instance found**")

    def do_destroy(self, line):
        try:
            if not line:
                raise SyntaxError()
            args = line.split()
            if args[0] not in self.my_classes:
                raise NameError()
            if len(args) < 2:
                raise IndexError()
            value = storage.all()
            key = args[0] + '.' + args[1]
            if key in value:
                del (value[key])
            else:
                storage.save()
        except SyntaxError:
            print("** class name missing **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")
        except KeyError:
            print("** no instance found**")

    def do_all(self, line):
        obj = storage.all()
        args = []
        if not line:
            for key, val in obj.items():
                args.append(str(val))
            print(args)
            return
        try:
            args = line.split()
            if args[0] not in self.my_classes:
                raise NameError()
            for key, val in obj.items():
                n = key.split('.')
                if n[0] == args[0]:
                    args.append(str(val))
            print(args)
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
