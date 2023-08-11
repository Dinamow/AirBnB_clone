#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """the command line to mainuplate classe"""
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }
    unchangable = ["id", "created_at", "updated_at"]
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """exit the command line after pressing C+D"""
        print('')
        return True

    def do_update(self, line):
        splited = line.split(" ")
        test = False
        if len(line) == 0:
            print("** class name missing **")
        elif splited[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif splited[0] in self.classes.keys() and len(splited) == 1:
            print("** instance id missing **")
        else:
            my_storage = storage
            for key, value in my_storage.all().items():
                tmp = key.split(".")
                if splited[1] == tmp[1] and splited[0] == tmp[0]:
                    test = True
                    if len(splited) == 2:
                        print("** attribute name missing **")
                        break
                    if len(splited) == 3:
                        print("** value missing **")
                        break
                    if splited[2] in self.unchangable:
                        break
                    splited[3] = eval(splited[3])
                    setattr(storage.all()[key], splited[2], splited[3])
                    storage.all()[key].save()
                    break
            if not test:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        test = False
        splited = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
        elif splited[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif splited[0] in self.classes.keys() and len(splited) == 1:
            print("** instance id missing **")
        else:
            x = storage
            for key, value in x.all().items():
                tmp = key.split(".")
                if splited[1] == tmp[1] and splited[0] == tmp[0]:
                    test = True
                    del x.all()[key]
                    x.save()
                    break
            if not test:
                print("** no instance found **")

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """pass an emptyline"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        splited = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.classes.keys() or len(splited) > 1:
            print("** class doesn't exist **")
        else:
            for key in self.classes.keys():
                if line == key:
                    test = self.classes[key]()
                    test.save()
                    print(test.id)
                    break

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        splited = line.split(" ")
        test = False
        if len(line) == 0:
            print("** class name missing **")
        elif splited[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif splited[0] in self.classes.keys() and len(splited) == 1:
            print("** instance id missing **")
        else:
            for key, value in storage.all().items():
                tmp = key.split(".")
                if splited[1] == tmp[1] and splited[0] == tmp[0]:
                    test = True
                    print(value)
                    break
            if not test:
                print("** no instance found **")

    def do_all(self, line):
        splited = line.split(" ")
        arr = []
        if len(splited) > 1 and splited[0] not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            teto = storage.all()
            if len(line) == 0:
                for key in teto.keys():
                    arr.append(str(teto[key]))
            else:
                for key in teto.keys():
                    tmp = key.split(".")
                    if tmp[0] == splited[0]:
                        arr.append(str(teto[key]))
            print(arr)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
