import Helper;

##data = [3, '0100']

def main():
    print("Hello from the main function!")
    ##Helper.appendTime("john", data)

    #currently only works on classic
    print(Helper.record_Runtime(Helper.a,Helper.b)) 
    print(Helper.record_Runtime(Helper.c,Helper.d))

if __name__ == "__main__":
    main()