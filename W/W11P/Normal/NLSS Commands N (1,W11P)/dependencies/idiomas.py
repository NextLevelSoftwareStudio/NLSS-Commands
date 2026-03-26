def idiomasAceites():
    inglês = ["English"]
    português = ["Inglês"]
    return inglês + português

def buscador(idioma: str):
    if idioma == "Inglês":
        return ["English"]
    else:
        print("A programming error occurred.")
