#Final ptroject practice

# Book Class
# This class defines a Book object with attributes like title, author, genre, status, and rating.
class Book:
    def __init__(self, title, author, genre, status='unread', rating=None):
        self.title = title  # Stores the title of the book
        self.author = author  # Stores the author of the book
        self.genre = genre  # Stores the genre of the book
        self.status = status  # Stores the reading status: 'read' or 'unread'
        self.rating = rating  # Stores the optional rating for the book
        self.next = None  # Points to the next book in the linked list


# Linked List
# This class manages a list of books, allowing books to be added, deleted, or displayed.
class LinkedList:
    def __init__(self):
        self.head = None  # Stores the start of the linked list (initially empty)

    # Adds a book to the end of the linked list
    def add(self, book):
        if not self.head:
            self.head = book  # Sets the new book as the head if the list is empty
        else:
            current = self.head
            while current.next:  # Traverses to the end of the list
                current = current.next
            current.next = book  # Sets the new book at the end of the list

    # Deletes a book by title from the linked list
    def delete(self, title):
        current = self.head
        previous = None
        while current:
            if current.title == title:  # Finds the book with the matching title
                if previous:  # If it's not the head, adjusts the pointers
                    previous.next = current.next
                else:  # If it's the head, updates the head pointer
                    self.head = current.next
                return f"Book '{title}' deleted."
            previous = current  # Moves to the next node
            current = current.next
        return f"Book '{title}' not found."  # Indicates that the book was not found

    # Displays all books in the linked list as a list
    def display(self):
        books = []
        current = self.head
        while current:
            books.append(current)  # Collects each book in the list
            current = current.next
        return books


# Library Management System
# This class manages the entire library, using a dictionary of linked lists to organize books by genre.
class Library:
    def __init__(self):
        self.genres = {}  # Stores genres as keys and linked lists as values

    # Adds a book to the library under the appropriate genre
    def add_book(self, title, author, genre, status='unread', rating=None):
        book = Book(title, author, genre, status, rating)  # Creates a new Book object
        if genre not in self.genres:  # Checks if the genre exists; if not, creates a new linked list
            self.genres[genre] = LinkedList()
        self.genres[genre].add(book)  # Adds the book to the linked list for the genre
        return f"Book '{title}' added to genre '{genre}'."

    # Deletes a book from the library by searching across all genres
    def delete_book(self, title):
        for genre, linked_list in self.genres.items():  # Iterates through all genres
            result = linked_list.delete(title)  # Tries to delete the book from the current genre
            if "deleted" in result:  # Checks if the deletion was successful
                return result
        return f"Book '{title}' not found."  # Indicates that the book was not found in any genre

    # Searches for books by keyword (matches title or author)
    def search_books(self, keyword):
        results = []
        for genre, linked_list in self.genres.items():  # Iterates through all genres
            current = linked_list.head
            while current:
                # Checks if the keyword matches the book's title or author
                if keyword.lower() in current.title.lower() or keyword.lower() in current.author.lower():
                    results.append(current)  # Adds matching books to the results
                current = current.next  # Moves to the next book
        return results

    # Counts the number of unread books using recursion
    def count_unread_books(self):
        def recursive_count(node):
            if not node:  # Base case: if the node is None, returns 0
                return 0
            # Adds 1 if the book is unread, then recursively counts the rest
            return (1 if node.status == 'unread' else 0) + recursive_count(node.next)

        total = 0
        for linked_list in self.genres.values():  # Counts unread books for each genre
            total += recursive_count(linked_list.head)
        return total

    # Displays all books in the library, organized by genre
    def display_library(self):
        for genre, linked_list in self.genres.items():  # Iterates through all genres
            print(f"\nGenre: {genre}")
            for book in linked_list.display():  # Displays all books in the genre
                print(f" - {book.title} by {book.author} [{book.status}]")


# Main Function
# This is the entry point for the program and provides a menu-driven interface for the user.
def main():
    library = Library()  # Creates a Library object
    while True:
        # Displays the main menu
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Search Books")
        print("4. Count Unread Books")
        print("5. Display Library")
        print("6. Exit")
        choice = input("Enter your choice: ")

        # Performs actions based on the user's choice
        if choice == '1':
            # Adds a new book
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            genre = input("Enter genre: ")
            status = input("Enter status (read/unread): ")
            rating = input("Enter rating (optional): ")
            print(library.add_book(title, author, genre, status, rating))

        elif choice == '2':
            # Deletes a book
            title = input("Enter book title to delete: ")
            print(library.delete_book(title))

        elif choice == '3':
            # Searches for books
            keyword = input("Enter search keyword: ")
            results = library.search_books(keyword)
            if results:
                for book in results:
                    print(f" - {book.title} by {book.author} [{book.status}]")
            else:
                print("No books found.")

        elif choice == '4':
            # Counts unread books
            print(f"Unread books: {library.count_unread_books()}")

        elif choice == '5':
            # Displays all books in the library
            library.display_library()

        elif choice == '6':
            # Exits the program
            print("Goodbye!")
            break

        else:
            # Handles invalid input
            print("Invalid choice. Please try again.")


# Directly calls the main function to start the program
main()
