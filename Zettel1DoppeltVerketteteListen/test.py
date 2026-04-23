#heir ist das Demo programm um unser modul zutesten. die datei __init__.py hat keine inhalt, sie muss aber im dem ornder sein, damit python den ordner als einbindbares modul erkennt und man es in anderen programm verwenden kann


from main import * #Alles aus main in diesen namespace kippen


def main():
    print("Test startett....");

    liste = DoppeltVerketteteListe();

    liste.append(10)
    liste.append(20)
    liste.append(30)

    print("Nach erstem Test:")
    liste.drucken()

    print("Tsste Iterator Funktion:")
    for d in liste:  #testet ob das objekt wirkciah als iterator aufgefasst wird
        print(d)

    print("Länge:", len(liste)) #Da wir __len eingeaut haben

if __name__ == '__main__':
    main();
