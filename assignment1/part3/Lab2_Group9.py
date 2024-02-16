# Dorghaam Haidar, Abdullah Lambada
# February 14, 2024
# INFT 1207
# Description: Prompts user to either add book, list books, or search for a book within a csv file




# Importing csv to make a csv file
import csv 

# Naming the csv file "books.csv" as stated in assignment
filename = "books.csv"  

# Creating a function for when the user wants to enter a book, must be in following order (title, authorm year)
def import_book(book_title, author_name, year_of_publication):
    # Opening and appending whatever the user inputs as an addition to the book
    with open(filename, 'a', newline='') as csvfile:
        # Writer is what puts the csv file into a writer mode and appends whatever user inputs
        writer = csv.writer(csvfile)  
        #Writerrow is what appaends the input into a row fashion onto csv excel
        writer.writerow([book_title, author_name, year_of_publication])
    # Print statement for success of adding the book
    print("Your book has now been added successfully!")

# Creating a function for listing the books in the csv file
def list_of_books():
    # Opening the file in read mode to list books that have been added
    with open(filename, 'r') as csvfile:
        # Reader is how the csv file is opened into read mode 
        reader = csv.reader(csvfile)
        # For loop for ever book that has been added, it must be printed
        for row in reader:
            # Its it printed in this order, book title, author name, and year of publication
            print(f"Book Title: {row[0]}, Author Name: {row[1]}, Year Of Publication: {row[2]}")


# Function for searching a book in  the csv file
def search_book(title):
    # Again opening up the file in read mode so nothing is appeneded
    with open(filename, 'r') as csvfile:
        # Reader is to open up csv file in reader mode
        reader = csv.reader(csvfile)
        # FOund variable is boolean value to see if input has been found, if it is false
        found = False
        # Then use this for loop to go through list of books in csv file 
        for row in reader:
            # If the title is found throughout the rows
            if title.upper() in row[0].upper():
                # Print it out in this order
                print(f"Title: {row[0]}, Author: {row[1]}, Year: {row[2]}")
                found = True

        # If the book is not found
        if not found:
            # Print statement that book has not been found
            print("Book not found.")

# While loop for list of options to continuously repeat
while True:
    
    # Try and except for proper invalid statements to be printed
    try:
            
            # Print options for user to input
            print("\nReading List Menu:")
            print("1. Add a book")
            print("2. List all books")
            print("3. Search for a book")
            print("4. Exit")

            # USer must input which option he wants to put
            choice = input("Enter your choice: ")
            
            # If chosen one, user must add book title, author, and year
            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter author's name: ")
                year = input("Enter year of publication: ")
                # Then it uses the import book function to append book into csv file
                import_book(title, author, year)

            # If option is 2, list all the books
            elif choice == "2":
                # USes list_of_books function to show all books in csv file
                list_of_books()

            # if option 3, then user can search for a book in the csv file
            elif choice == "3":
                # Asks user to input book title to search
                title = input("Enter book title to search: ")
                # Then uses the search book function to for loop and search for the book
                search_book(title)

            # If the choice is 4, it exits the program
            elif choice == "4":
                print("Exiting the program.")
                # Breaks while loop
                break
            # Else statement for any invalid choices
            else:
                print("Invalid choice. Please choose again.")

    except:
            # Anything invalid, invalid print statement comes up and repeats while loop
            print("Invalid, please type a valid input!")

