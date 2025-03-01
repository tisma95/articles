
def hello():
    print("hello()::est appelée")
    return "Hello"



def hello(nom):
    print(f"hello()::est appelée avec le paramètre nom='{nom}'")
    return f"Hello {nom}"


def hello(nom):
    print(f"hello()::est appelée avec le paramètre nom='{nom}'")
    reponse = f"Hello {nom}"
    print(f"hello()::s'est exécutée avec le résultat: '{reponse}'")
    return reponse

def obtenirNom():
    print("obtenirNom()::est appelée")
    nom = input("Entrer votre nom:")
    print(f"obtenirNom()::s'est exécutée avec le résultat nom='{nom}'")
    return nom


def main():
    print("main()::est appelée")
    nom = obtenirNom()
    print(f"main()::a exécuté obtenirNom() avec le résultat nom='{nom}'")
    hello(nom)

main()