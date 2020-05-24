print("Tere, Paavo!")
y = input("Kas soovid näha vinüülplaatide nimekirja? jah/ei ")

fail = open("albumid.txt", encoding="UTF-8")

albumid = []

def Albumite_kriipsud():
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

if y == "jah":
        
    Albumite_kriipsud()
    
else:
    w = input("Kas soovid otsida laulu? jah/ei ")
    if w == "jah":

        for rida in fail:
            albumid.append(rida)
    

        nimi = input("Sisesta albumi või artisti nimi: ")
        x = nimi.title()

        for str in albumid:
            if x in str:
                print(str)
                
    else:
        print("Ei soovinud midagi!")
        
fail.close()