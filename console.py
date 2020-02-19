#!/usr/bin/python3
"""The AirBnb Console"""
import cmd
import re
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from shlex import split


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
            print(args)
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

    def do_update(self, line):
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
            if key not in value:
                raise KeyError()
            if len(args) < 3:
                raise attributeError()
            if len(args) < 4:
                raise ValueError()
            field = value[key]
            try:
                field.__dict__[args[2]] = eval(args[3])
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

    def count(self, line):
        aux = 0
        try:
            args = line.split()
            if args[0] not in self.my_classes:
                raise NameError()
            objects = storage.all()
            for key in objects:
                field = key.split('.')
                if field[0] == args[0]:
                    aux += 1
            print("{:d}".format(aux))
        except NameError:
            print("** class doesn't exist **")

    def cleaner(self, line_list):
        line_list = str(line_list).replace("update(", "")
        line_list = str(line_list).replace("show(", "")
        line_list = str(line_list).replace("destroy(", "")
        line_list = line_list.split(',')
        new = ""
        for i in range(len(line_list)):
            line_list[i] = re.sub(r"[^a-zA-Z0-9-_]", "", line_list[i])
            new += line_list[i]
            new += " "
        return(new)

    def default(self, line):
        line_list = line.split('.')
        if len(line_list) >= 2:
            if line_list[1] == "all()":
                self.do_all(line_list[0])
            elif line_list[1] == "count()":
                self.count(line_list[0])
            elif line_list[1][:4] == "show":
                self.do_show(self.cleaner(line_list))
            elif line_list[1][:7] == "destroy":
                self.do_destroy(self.cleaner(line_list))
            elif line_list[1][:6] == "update":
                result = line_list[1].find('{')
                result1 = line_list[1].find('}')
                if (result != -1 and result1 != -1):
                    line = line_list[1]
                    line = line.replace("'", '"')
                    line = line[result:result1 + 1]
                    dic = json.loads(line)
                    first = self.cleaner(line_list).split()
                    new = ""
                    for i in range(2):
                        new += first[i]
                        new += " "
                    for key, value in dic.items():
                        self.do_update(("{} {} {}".format(new, key, value)))
                else:
                    self.do_update(self.cleaner(line_list))
        else:
            cmd.Cmd.defualt(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
