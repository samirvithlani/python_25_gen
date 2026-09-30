playlist=["beran","barsat","tum hi ho","perfect","sitare"]

def addSong(song):
    playlist.append(song)

def removeSong(song):
    playlist.remove(song)

def display():
    for i in playlist:
        print(i)    

def sortplaylist(mode):
    if mode=='ASC':
        playlist.sort()
    else:
        playlist.sort(reverse=True)    



while True:
    print("********************")        
    print("press 1 for add song")
    print("press 2 for remove song")
    print("press 3 for display song")
    print("press 4 for sort song")
    choice = int(input(""))
    match choice:
        case 1:
            addSong("farak")    
        case 2:
            removeSong("barsat")    
        case 3:
            display()
        case 4:
            sorted("DSC")        
        case 5:
            break    
        case _:
            print("invalid choice ")    
            break
