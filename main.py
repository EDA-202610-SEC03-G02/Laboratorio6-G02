from App import view as view
import tracemalloc

# Main function
def main():
    view.main()


# Main function call to run the program
if __name__ == '__main__':
    tracemalloc.start()
    main()
