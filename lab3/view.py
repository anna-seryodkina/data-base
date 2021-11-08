import controller


print("commands: \n> add\n> delete\n> update\n> exit")

while(True):
    command = input("enter command: ")

    if command == "add":
        try:
            controller.add()
        except controller.EntityException as inst:
            print(inst.message)
        except controller.InputException as inst:
            print(inst.message)
        except:
            print(">> error happened.")

    elif command == "delete":
        try:
            controller.delete()
        except controller.EntityException as inst:
            print(inst.message)
        except controller.InputException as inst:
            print(inst.message)
        except:
            print(">> error happened.")

    elif command == "update":
        try:
            controller.update()
        except controller.EntityException as inst:
            print(inst.message)
        except controller.InputException as inst:
            print(inst.message)
        except:
            print(">> error happened.")

    elif command == "exit" or command == "":
        break
    else:
        print(">> oops. wrong command")