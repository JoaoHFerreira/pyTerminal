# A variável atu é responsável por indicar o "Atual diretório"
# por isso o nome de atu, é uma abreviação para atual diretório
atu  = "/"

# Na linha abaixo estão setadas as configurações da árvore de elementos,
# ela será incrementada por mais elementos ao longo do percurso

# Cada elemento (path ou folder) contém como chaves:
# * Uma lista de folder, representado pela letra 'f'
# * Uma lista de files, representado pela letra 'fi'
# * Um path anterior representado pela letra 'p'
c = { "/": {"f": [],"fi": [],"p": "/",}}


# Este é um loop infinito, roda para sempre porque é um terminal
while True:

    # Na letra 'o' é recebida uma entrada, se espera uma entrada dupla, no caso, o comando mais um nome.
    # exceto para pwd e para ls
    o = input("/")

    # Verifica se o que foi escrito é ls, se for printa o que existe no path atual (atu)
    if o == "ls":
        if c[atu]["fi"] or c[atu]["f"]:
            print(c[atu]["fi"])
            print(c[atu]["f"])
        continue

    # Verifica se o que foi escrito é touch, splita para pegar o primeiro elemnento
    # o segundo elemento é utilizado para fazer a criação do arquivo
    if o.split(" ")[0] == "touch":
        if len(o.split(" ")) == 2:
            c[atu]["fi"].append(o.split(" ")[1])
        continue
        

    # Verifica se o que foi escrito é mkdir, splita para pegar o primeiro elemnento
    # o segundo elemento é utilizado para fazer a criação do folder
    if o.split(" ")[0] == "mkdir":
        if len(o.split(" ")) == 2:
            c[atu]["f"].append(atu  +  o.split(" ")[1] + "/")
            c[atu  +  o.split(" ")[1] + "/"] = {"f": [],"fi": [],"p": atu,}
        continue

    # Simplesmente verifica se o que foi digitado é pwd, caso sim, print resultado do path atual
    if o == "pwd":
        print(atu)
        continue

    # Volta para o folder anterior e registra seu novo path, como o path anterior que era
    if o == "cd ..":
        atu = c[atu]["p"]
        continue

    # Entra em determinado path, pode se usar o ls para determinar quais são os paths acessíveis
    if o.split(" ")[0] == "cd":
        temp = o.split(" ")[1].split(" ")[0]
        atu = atu + temp + "/"
        continue

    # Printa alguma coisa na tela, 
    if o.split(" ")[0] == "echo":
        print(o[5:])
        continue
