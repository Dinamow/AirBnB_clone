#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """the command line to mainuplate classe"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """exit the command line after pressing C+D"""
        print('')
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """pass an emptyline"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        print(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
