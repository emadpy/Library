from library import Library

def main():

    library = Library()

    while True:

        print("Add: 1 | Remove: 2 | Search: 3 | Show: 4 | Exit: 5")

        choice = input()

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            library.add_book(title, author)
        elif choice == "2":
            title = input("Title: ")
            library.remove_book(title)
        elif choice == "3":
            title = input("Title: ")
            library.search_book(title)
        elif choice == "4":
            library.show_books()
        elif choice == "5":
            break




if __name__ == "__main__":
    main()