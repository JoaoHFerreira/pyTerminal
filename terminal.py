from IPython import embed

# A variável current_folder é responsável por indicar o "Atual diretório"
curent_folder  = "/"

# Na linha abaixo estão setadas as configurações da árvore de elementos,
# ela será incrementada por mais elementos ao longo do percurso

# Cada elemento (path ou folder) contém como chaves:
# * Uma lista de folder, representado pela letra 'folders'
# * Uma lista de files, representado pela letra 'files'
# * Um path anterior representado pela letra 'previous_folder'
tree_structure = { 
    curent_folder: {
        "folders": list(),
        "files": list(),
        "previous_folder": "/",
    }
}

# Este é um loop infinito, roda para sempre porque é um terminal
while True:

    # Na variável command é recebida uma entrada, se espera uma entrada dupla, no caso, o comando mais um nome.
    # exceto para pwd e para ls
    # Nesse split são coletados o commando e o arguemento
    init_command = input("/").split(" ")

    # Caso seja echo vai coletar primeiro elemnto echo
    # e o segundo vai juntar as strings para formar o print
    if len(init_command) == 1:
        command = init_command[0]
    elif init_command[0] == "echo":
        command = init_command[0]
        argument = " ".join(init_command[1:])
        print(argument)
        continue
    else:
        # caso não apenas desempacota o comando coletado
        command, argument = init_command

    # Verifica se o command foi ls, caso sim, printa a estrutura do diretório corrente
    if command == "ls":
        if tree_structure[curent_folder]["files"] or tree_structure[curent_folder]["folders"]:
            print(tree_structure[curent_folder]["files"])
            print(tree_structure[curent_folder]["folders"])
        continue

    # Verifica se o command foi touch, caso sim, cria arquivo
    if command == "touch":
        tree_structure[curent_folder]["files"].append(argument)
        continue
        
    # Verifica se o command foi mkdir, caso sim, cria folder
    if command == "mkdir":
        dir_name = f"{curent_folder}{argument}/"
        tree_structure[curent_folder]["folders"].append(dir_name)
        tree_structure[dir_name] = {"folders": list(),"files": list(),"previous_folder": curent_folder,}
        continue

    # Verifica se o command foi pwd, caso sim, printa o diretório corrente
    if command == "pwd":
        print(curent_folder)

    # Volta para o folder anterior e registra seu novo path, como o path anterior que era
    if command == "cd" and argument == "..":
        curent_folder = tree_structure[curent_folder]["previous_folder"]
        continue

    # Entra em determinado path, pode se usar o ls para determinar quais são os paths acessíveis
    if command == "cd":
        real_path_name = argument.split(" ")[0]
        curent_folder = f"{curent_folder}{real_path_name}/"
        continue

    