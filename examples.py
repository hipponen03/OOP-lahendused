"""examples.py

See fail aitab kasutajal aru saada, kuidas programmi
kasutada näidates kasutajale paar demo.
"""

def albumiteKriipsud():
        for rida in fail:
            elemendid = rida.split("\t")
            esineja = elemendid[0]
            album = elemendid[1]
            albumid.append(album)
            aasta = elemendid[2]
            laul = elemendid[3]
            if len(albumid) > 1:
                if albumid[-2] != albumid[-1]:
                    print()
                    print("--------------------------------------------")
                    print()
            print(rida)



print("Tere, Paavo!")
mitmesDemo = int(input("Mitmendat demo soovid näha? 1/2/3: "))
if mitmesDemo == 1:
    b = "jah"
    print("Kas soovid lisada vinüülplaatide nimekirja albumit? jah/ei \033[96mjah\033[0m")


    if b == "jah":
        seis = "aktiivne"
        grupp = "Anne Veski"
        print("Sisestage esitaja nimi: \033[96mAnne Veski\033[0m")
        album = "Eesti kullafond"
        print("Sisestage albumi nimi: \033[96mEesti kullafond\033[0m")
        aasta = "2006"
        print("Sisestage aasta: \033[96m2006\033[0m")

        while seis == "aktiivne":
        
            laul = "Roosiaia kuninganna"
            print("Sisestage laulu pealkiri: \033[96mRoosiaia kuninganna\033[0m")
            laulupealkiri = grupp.title() + "\t" + album.title() + "\t" + aasta + "\t" + laul.title()
            fail = open("albumid.txt", "a", encoding="UTF-8")
            fail.write("\n" + laulupealkiri)
            print("Kas soovite veel laule lisada? jah/ei \033[96mjah\033[0m")
            laul = "Jätke võtmed väljapoole"
            print("Sisestage laulu pealkiri: \033[96mJätke võtmed väljapoole\033[0m")
            laulupealkiri = grupp.title() + "\t" + album.title() + "\t" + aasta + "\t" + laul.title()
            fail = open("albumid.txt", "a", encoding="UTF-8")
            fail.write("\n" + laulupealkiri)
            seis = "inaktiivne"
        

    else:
     pass

    y = "ei"
    print("Kas soovid näha vinüülplaatide nimekirja? jah/ei \033[96mei\033[0m")
    fail = open("albumid.txt", encoding="UTF-8")
    albumid = []


    if y == "jah":
        albumiteKriipsud()
    
    else:
        w = "jah"
        print("Kas soovid otsida laulu? jah/ei \033[96mjah\033[0m")
        if w == "jah":
            for rida in fail:
                albumid.append(rida)
    
            nimi = "Alice Cooper"
            print("Sisesta albumi või artisti nimi: \033[96mAlice Cooper\033[0m")
            x = nimi.title()

            for str in albumid:
                if x in str:
                    print(str)  
        else:
            print("Ei soovinud midagi!")
    fail.close()

elif mitmesDemo == 2:
    print("Kas soovid lisada vinüülplaatide nimekirja albumit? jah/ei \033[96mei\033[0m")
    print("Kas soovid näha vinüülplaatide nimekirja? jah/ei \033[96mjah\033[0m")

    fail = open("albumid.txt", encoding="UTF-8")
    albumid = []
    y = "jah"

    if y == "jah":
        albumiteKriipsud()
        
    fail.close()

elif mitmesDemo == 3:
    print("Kas soovid lisada vinüülplaatide nimekirja albumit? jah/ei \033[96mei\033[0m")
    print("Kas soovid näha vinüülplaatide nimekirja? jah/ei \033[96mei\033[0m")
    w = "jah"
    print("Kas soovid otsida laulu? jah/ei \033[96mjah\033[0m")
    if w == "jah":
        albumid = []
        fail = open("albumid.txt", encoding="UTF-8")
        for rida in fail:
            albumid.append(rida)
    
        nimi = "Aerosmith"
        print("Sisesta albumi või artisti nimi: \033[96mAerosmith\033[0m")
        x = nimi.title()

        for str in albumid:
            if x in str:
                print(str)
    fail.close()
