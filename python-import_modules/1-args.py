import sys

def print_arguments():
 
    num_args = len(sys.argv) - 1

    
    if num_args > 0:
        print("{} argument{}:".format(num_args, 's' if num_args > 1 else ''))
        # print("Argument{}:".format('s' if num_args > 1 else ''))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
    else:
        print("0 arguments.")
    
if __name__ == "__main__":
    print_arguments()
