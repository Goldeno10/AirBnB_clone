#!/usr/bin/python3


import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    
    cls = {'BaseModel':BaseModel}
    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and
        prints the id.
        Ex: $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
        if arg:
            if arg not in type(self).cls.keys():
                print("** class doesn't exist **")
            else:
                new_instance = type(self).cls[arg]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class
        name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if len(args) > 2:
                return
            if len(args) == 1:
                if args[0] not in type(self).cls.keys():
                    print("** class doesn't exist **")
                    return
                print("** instance id missing **")
                return
            if len(args) == 2:
                arg1 = args[0]
                arg2 = args[1]
                obj_id = f'{arg1}.{arg2}'
                if arg1 in type(self).cls.keys():
                    instance = storage.all()
                    if obj_id in instance.keys():
                        print(instance[obj_id])
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id (save the change into
        the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if len(args) > 2:
                return
            if len(args) == 1:
                if args[0] not in type(self).cls.keys():
                    print("** class doesn't exist **")
                    return
                print("** instance id missing **")
                return
            if len(args) == 2:
                arg1 = args[0]
                arg2 = args[1]
                obj_id = f'{arg1}.{arg2}'
                if arg1 in type(self).cls.keys():
                    instance = storage.all()
                    if obj_id in instance.keys():
                        del instance[obj_id]
                        new_instance = type(self).cls[arg1](**instance)
                        new_instance.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the
        class name.
        Ex: $ all BaseModel or $ all.
        """
        inst_list = []
        if not line:
            instance = storage.all()
            for key in instance.keys():
                inst_list.append(str(instance[key]))
            print(inst_list)
            return
        else:
            args = line.split()
            if len(args) > 1:
                return
            if len(args) == 1:  
                if args[0] in type(self).cls.keys():
                    instance = storage.all()
                    for key in instance.keys():
                        if key.split('.')[0] == args[0]:
                            inst_list.append(str(instance[key]))
                    print(inst_list)
                    return
                else:
                    print("** class doesn't exist **")
                    return
    
    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating
        attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            obj = {}
            c_flag = 0
            id_flag = 0
            attr_flag = 0
            if len(args) >= 1:
                if args[0] not in type(self).cls.keys():
                    print("** class doesn't exist **")
                    return
                else:
                    if len(args) > 1:
                        c_flag = 1
                    else:
                        print("** instance id missing **")
                        return

            if len(args) >= 2:
                if c_flag == 0:
                    return
                else:
                    obj_id = f'{args[0]}.{args[1]}'
                    instance = storage.all()
                    if args[0] in type(self).cls.keys():
                        if obj_id in instance.keys():
                            if len(args) > 2:
                                id_flag = 1
                            else:
                                print("** attribute name missing **")
                                return
                        else:
                            print("** no instance found **")
                            return
            if len(args) >= 3:
                if id_flag == 0:
                    return
                else:
                    obj = instance[obj_id]
                    if args[2] in obj.to_dict():
                        if len(args) > 3:
                            setattr(obj, args[2], args[3].strip('"'))
                            storage.save()
                        else:
                            print("** value missing **")
                            return


    def do_quit(self, arg):
        "Quit command to exit the program"
        return True

    def do_EOF(self, arg):
        "EOF command to exit the program"
        return True

    def emptyline(self):
        """Do nothing when line is empty"""
        pass

    
if __name__ == '__main__':
        HBNBCommand().cmdloop()