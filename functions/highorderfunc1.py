def tobecalled():
    print("to be called.. call !!")



def test(a):
    print(a)
    a() #->to be called..

# test(12)    
# test(False)    
# test("")
# test([])        
test(tobecalled)