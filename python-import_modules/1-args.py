import sys

def print_arguments():
    # Get the number of arguments
    num_args = len(sys.argv) - 1

    # Print the number of arguments
    print(f"Number of argument(s): {num_args}")

    # Print the list of arguments
    if num_args > 0:
        print(f"Argument{'s' if num_args > 1 else ''}:")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")
    else:
        print(".")
    
if __name__ == "__main__":
    print_arguments()
