#to issue a passport user must have aadhar card and zero crimnal offence and must be indian citizen

indian = True
aadharcArd = True
criminaloff = 0

if indian ==True:
    print("user is indian !")
    if aadharcArd == True:
        print("user have aadharcard")
        if criminaloff<=0:
            print("user dont have any offecnced can apply for PASSPRT")
        else:
            print("user dont have any offecnced REJECTED")
                
    else:
        print("user dont have aadhar card REJECTED")    
else:
    print("user is not indian citiz")           