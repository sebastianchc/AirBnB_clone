#!/usr/bin/python3
""" AirBnB console """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class """

    prompt = "(hbnb) "
    my_classes = {"BaseModel", "Amenity", "Place","State",
                  "City", "Review", "User"}

    def do_quit(self, line):
        """ quit command """
        return True

    def do_EOF(self, line):
        """ EOF command """
        return True

    def emptyline(self):
        """ emptyline """
        pass

    def do_create(self, line):
        """ create command """
        try:
            if not line:
                raise SyntaxError()
            object = eval("{}()".format(line))
            object.save()
            print("{}".format(object.id))
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ show command """
        args = line.split()
        try:
            if not args:
                raise SyntaxError()
            if args[0] not in self.my_classes:
                raise NameError()
            if len(args) < 2:
                raise IndexError()
            dict_objs = storage.all()
            obj = "{}.{}".format(args[0], args[1])
            if obj in dict_objs:
                print(dict_objs[obj])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """ destroy command """
        args = line.split()
        try:
            if not args:
                raise SyntaxError()
            if args[0] not in self.my_classes:
                raise NameError()
            if len(args) < 2:
                raise IndexError()
            dict_objs = storage.all()
            obj = "{}.{}".format(args[0], args[1])
            if obj in dict_objs:
                del (dict_objs[obj])
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """ all command """
        dict_objs = storage.all()
        all_objs = []
        if not line:
            for key, obj in dict_objs.items():
                all_objs.append(str(obj))
            print(all_objs)
            return
        try:
            args = line.split()
            if args[0] not in self.my_classes:
                raise NameError()
            for key, obj in dict_objs.items():
                the_class = key.split(".")
                if the_class[0] == args[0]:
                    all_objs.append(str(obj))
            print(all_objs)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ update command """
        try:
            if not line:
                raise SyntaxError()
            args = line.split()
            if args[0] not in self.my_classes:
                raise NameError()
            if len(args) < 2:
                raise IndexError()
            dict_objs = storage.all()
            obj = "{}.{}".format(args[0], args[1])
            if obj not in dict_objs:
                raise KeyError()
            if len(args) < 3:
                raise AttributeError()
            if len(args) < 4:
                raise ValueError()
            field = dict_objs[obj]
            try:
                field.__dict__[args[2]] = eval(args[3])
                field.save()
            except Exception:
                field.__dict__[args[2]] = args[3]
                field.save()
        except ValueError:
            print("** value missing **")
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except AttributeError:
            print("** attribute name missing **")
        except KeyError:
            print("** no instance found **")
        except IndexError:
            print("** instance id missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
