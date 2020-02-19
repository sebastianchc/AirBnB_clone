#!/usr/bin/python3
""" AirBnB console """
import cmd
import re
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class """

    prompt = "(hbnb) "
    my_classes = {"BaseModel", "Amenity", "Place", "State",
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
            args = line.split()
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
