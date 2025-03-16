from typing import List
import os

# Function to print a message with a line break
def print_with_break(message: str = ""):
    print(f"{message}\n")

# BookDetails class to represent information about a book
class BookDetails:
    def __init__(self, title: str, author: str, publication_year: int, genre: str, read_status: bool):
        # Initialize the attributes of the book
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.read_status = read_status

    # String representation of the book for easy display
    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Genre: {self.genre}, Read: {'Yes' if self.read_status else 'No'}"

    # Convert the book details to a string format suitable for saving to a file
    def to_file_format(self):
        return f"{self.title},{self.author},{self.publication_year},{self.genre},{self.read_status}"

    # Class method to convert a file line into a BookDetails object
    @classmethod
    def from_file_format(cls, line: str):
        title, author, year, genre, read_status = line.strip().split(',')
        return cls(title, author, int(year), genre, read_status.lower() == 'true')

# Library class to manage a collection of books
class Library:
    def __init__(self):
        # Initialize an empty list to store books
        self.books: List[BookDetails] = []
        self.load_library()    # Load books from the file if it exists

    # Add a book to the library
    def add_book(self, book: BookDetails):
        self.books.append(book)

    # Remove a book from the library by title
    def remove_book(self, title: str):
        self.books = [book for book in self.books if book.title != title]

    # Search for books by title (case-insensitive)
    def search_book(self, title: str):
        return [book for book in self.books if title.lower() in book.title.lower()]

    # Display all books in the library
    def display_books(self):
        if self.books:
            for index, book in enumerate(self.books, start=1):
                # Check read status and display it
                read_status = "Read" if book.read_status else "Unread"
                print(f"{index}. {book.title} by {book.author} ({book.publication_year}) - {book.genre} - {read_status}")
            
            # Add a line break only if it's the last book
            if index == len(self.books):
                print()
        else:
            print_with_break("No books available.")

    # Display statistics about the library
    def display_statistics(self):
        total_books = len(self.books)
        read_books = sum(1 for book in self.books if book.read_status)
        unread_books = total_books - read_books

        # Print statistics: total books, read books, unread books, and percentage read
        print_with_break(f"Total Books: {total_books}\nBooks Read: {read_books}\nBooks Unread: {unread_books}\nPercentage Read: {read_books / total_books * 100 if total_books else 0:.2f}%")

    # Save all books to a file
    def save_library(self):
        with open("library.txt", "w") as file:
            for book in self.books:
                file.write(book.to_file_format() + "\n")

    # Load books from the file (if it exists)
    def load_library(self):
        if os.path.exists("library.txt"):
            with open("library.txt", "r") as file:
                for line in file:
                    # Add each book from the file to the library
                    self.books.append(BookDetails.from_file_format(line))

# Menu function to handle user interaction
def menu():
    library = Library()  # Create a Library instance

    while True:
        # List of menu options
        options = [
            "Welcome to your Personal Library Manager!",
            "1. Add a book",
            "2. Remove a book",
            "3. Search for a book",
            "4. Display all books",
            "5. Display statistics",
            "6. Exit"
        ]
        # Print the menu options
        print_with_break("\n".join(options))

        # Prompt the user for their choice
        choice = input("Select an option (1-6): ")

        # Option to add a book
        if choice == '1' or choice.lower() == "add a book":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            publication_year = int(input("Enter publication year: "))
            genre = input("Enter genre: ")
            read_status = input("Have you read this book? (y/n): ").lower() == 'y'

            # Create a BookDetails object and add it to the library
            book = BookDetails(title, author, publication_year, genre, read_status)
            library.add_book(book)
            print_with_break(f"Book '{title}' added.")

        # Option to remove a book
        elif choice == '2' or choice.lower() == "remove a book":
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)
            print_with_break(f"Book '{title}' removed.")

        # Option to search for a book by title
        elif choice == '3' or choice.lower() == "search for a book":
            title = input("Enter the title to search for: ")
            found_books = library.search_book(title)
            if found_books:
                for index, book in enumerate(found_books, start=1):
                    # Display each found book with read status
                    read_status = "Read" if book.read_status else "Unread"
                    print(f"{index}. {book.title} by {book.author} ({book.publication_year}) - {book.genre} - {read_status}")
                    # Add a line break only if it's the last book
                    if index == len(found_books):
                        print()
            else:
                print_with_break(f"No books found for '{title}'.")

        # Option to display all books
        elif choice == '4' or choice.lower() == "display all books":
            print("Your Library:")
            library.display_books()

        # Option to display library statistics
        elif choice == '5' or choice.lower() == "display statistics":
            print("Current statistics:")
            library.display_statistics()

        # Option to exit and save library data
        elif choice == '6' or choice.lower() == "exit":
            library.save_library()  # Save library data to a file
            print_with_break("Library saved to file. Goodbye!")
            break  # Exit the loop

        # Handle invalid input
        else:
            print_with_break("Invalid choice. Please select a valid option.")

# Main entry point to run the program
if __name__ == "__main__":
    menu()
