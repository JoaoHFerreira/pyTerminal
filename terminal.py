curent_folder  = "/"
tree_structure = { 
    curent_folder: {
        "folders": list(),
        "files": list(),
        "previous_folder": "/",
    }
}


while True:
    command = input("/")

    if command == "ls":
        if tree_structure[curent_folder]["files"] or tree_structure[curent_folder]["folders"]:
            print(tree_structure[curent_folder]["files"])
            print(tree_structure[curent_folder]["folders"])
        continue

    if command.split(" ")[0] == "touch":
        if len(command.split(" ")) == 2:
            tree_structure[curent_folder]["files"].append(command.split(" ")[1])
        continue
        

    if command.split(" ")[0] == "mkdir":
        if len(command.split(" ")) == 2:
            tree_structure[curent_folder]["folders"].append(curent_folder  +  command.split(" ")[1] + "/")
            tree_structure[curent_folder  +  command.split(" ")[1] + "/"] = {
                "folders": list(),
                "files": list(),
                "previous_folder": curent_folder,
                }
        continue

    if command == "pwd":
        print(curent_folder)

    if command == "cd ..":
        curent_folder = tree_structure[curent_folder]["previous_folder"]
        continue


    if command.split(" ")[0] == "cd":
        temp = command.split(" ")[1].split(" ")[0]
        curent_folder = curent_folder + temp + "/"
        continue


    if command.split(" ")[0] == "echo":
        print(command[5:])


        
    