#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """the command line to mainuplate classe"""
    ModleNames = ["BaseModel", "User"]
    y = {}
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
        elif splited[0] not in self.ModleNames:
            print("** class doesn't exist **")
        elif splited[0] in self.ModleNames and len(splited) == 1:
            print("** instance id missing **")
        else:
            my_storage = storage
            for key, value in my_storage.all().items():
                tmp = key.split(".")
                if splited[1] == tmp[1]:
                    test = True
                    if len(splited) == 2:
                        print("** attribute name missing **")
                        break
                    if len(splited) == 3:
                        print("** value missing **")
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
        elif splited[0] not in self.ModleNames:
            print("** class doesn't exist **")
        elif splited[0] in self.ModleNames and len(splited) == 1:
            print("** instance id missing **")
        else:
            x = storage
            for key, value in x.all().items():
                tmp = key.split(".")
                if splited[1] == tmp[1]:
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
        elif line not in self.ModleNames or len(splited) > 1:
            print("** class doesn't exist **")
        else:
            test = BaseModel()
            test.save()
            print(test.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        splited = line.split(" ")
        test = False
        if len(line) == 0:
            print("** class name missing **")
        elif splited[0] not in self.ModleNames:
            print("** class doesn't exist **")
        elif splited[0] in self.ModleNames and len(splited) == 1:
            print("** instance id missing **")
        else:
            for key, value in storage.all().items():
                tmp = key.split(".")
                if splited[1] == tmp[1]:
                    test = True
                    print(value)
                    break
            if not test:
                print("** no instance found **")

    def do_all(self, line):
        splited = line.split(" ")
        arr = []
        if len(splited) > 1 and splited[0] not in self.ModleNames:
            print("** class doesn't exist **")
        else:
            teto = storage.all()
            for i in teto.keys():
                arr.append(str(teto[i]))
            print(arr)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
