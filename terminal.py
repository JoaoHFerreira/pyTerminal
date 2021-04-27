atu  = "/"
c = { 
    "/": {
        "f": [],
        "fi": [],
        "p": "/",
        "r": True
    }
}


while True:
    o = input("/")

    if o == "ls":
        if c[atu]["fi"] or c[atu]["f"]:
            print(c[atu]["fi"])
            print(c[atu]["f"])
        continue

    if o.split(" ")[0] == "touch":
        if len(o.split(" ")) == 2:
            c[atu]["fi"].append(o.split(" ")[1])
        continue
        

    if o.split(" ")[0] == "mkdir":
        if len(o.split(" ")) == 2:
            c[atu]["f"].append(atu  +  o.split(" ")[1] + "/")
            c[atu  +  o.split(" ")[1] + "/"] = {
                "f": [],
                "fi": [],
                "p": atu,
                "r": False
                }
        continue

    if o == "pwd":
        print(atu)

    if o == "cd ..":
        atu = c[atu]["p"]
        continue


    if o.split(" ")[0] == "cd":
        temp = o.split(" ")[1].split(" ")[0]
        atu = atu + temp + "/"
        continue


    if o.split(" ")[0] == "echo":
        print(o[5:])


        
    