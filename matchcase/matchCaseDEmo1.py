season = "w"

match season:
    case "winter" | "WINTER" | "w" |"W":
        print("this is winter season !!")
    case "summer":
        print("welcome to ahmedabad !!")    
    case "monsoon":
        print("Ambalal is here !!")    
    case _:
        print("invalid choice !!")        
        
        