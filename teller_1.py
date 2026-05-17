total_kilometraje = 0
toltal_galones = 0
mejor_kilometraje = 0
mejor_galon = 0
tanqueos = 0
extra = 0
octanaje_superior = 0
galones = float(input())

if galones == 0 :
    print("no data provided")

else:
    while galones !=0:
        total_galones =+ galones
        
        if galones > mejor_galon :
            mejor_galon = galones
        kilometros = float(input())
        
        if kilometros > mejor_kilometraje:
            mejor_kilometraje = kilometros
        total_kilometraje  =+ kilometros
        octanaje = int(input())
        
        if octanaje >=90: 
            octanaje_superior =+1
        
        while octanaje <81 or octanaje>=98 :
            print("OCTANAJE INVALIDO")
            octanaje = int(input())
        tanqueos =+1 
        galones = float(input())

    AVG = total_kilometraje / total_galones
    extra = (octanaje_superior * tanqueos) / 100
    print(f"AVG:{AVG:.2f}")
    print(f"BEST:{mejor_kilometraje:.2f}/{mejor_galon:.2f}")
    print(f"extra:{extra:.2f}%")