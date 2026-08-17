def windows(*args):
    print("windows called...")
    print(args)

def mac(*args):
    print("mac called...")    
    print(args)



def os(func,*args):
    print("os called...")
    print(args)
    func(args)

os(windows,"a","b")   
os(mac,"a","b","c") 