from FileWorker import FileWorker

dog = FileWorker("zip_dir.zip")
while 1:
    dog.print_path()
    command = input()
    if command[:command.find(' ')] == "ls" or command == "ls":
        if command[command.find(' ')+1:] == "" or command == "ls":
            dog.ls()
        else:
            dog.ls(command[command.find(' ')+1:])
    elif command[:command.find(' ')] == "cd":
        dog.cd(command[command.find(' ')+1:])
    elif command == "exit":
        del dog
        break
    elif command == "pwd":
        dog.pwd()
    elif command[:command.find(' ')] == "cat":
        dog.cat(command[command.find(' ')+1:])
