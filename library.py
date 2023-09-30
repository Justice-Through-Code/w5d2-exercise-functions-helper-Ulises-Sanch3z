
# You are working on a library management system, here are the list books at the library

books = [
    'MY OWN WORDS', 'THE BODY KEEPS THE SCORE', 'STAMPED FROM THE BEGINNING', 'JUST MERCY', 'BORN A CRIME', 'ON TYRANNY', 'HOMO DEUS: A BRIEF HISTORY OF TOMORROW',
    'THE WARMTH OF OTHER SUNS', 'THE NEW JIM CROW', 'THE POWER OF MOMENTS', 'BRAIDING SWEETGRASS', 'MY GRANDMOTHER\'S HANDS', 'THE PEOPLE WE KEEP'
]

# 1.1 TODO: Create a function named 'available_books' to print the books list -- one book title on each line
# Parameters: Not needed for this function
# Return: Not needed for this function

def available_books():
    for book in books:
        print(book)

# 1.2 TODO: Run the 'available_books' function

available_books()

print('-----------------------')
# 1.3 TODO: Create a function named 'check_out' that removes a book from the books list
# Parameters: book_title (string)
# Return: Not needed for this function

def check_out(book_title: str) -> str:
    books.remove(book_title)

# 1.4 TODO: Check out 'THE POWER OF MOMENTS' using the check_out function

check_out("THE POWER OF MOMENTS")

# 1.5 TODO: Run the 'available_books' function again to see if the book was checked out

available_books()

print('-----------------------')
# 1.6 TODO: Create a function 'check_in' that adds a book to the end of the books list
# Parameters: book_title (string)
# Return: Not needed for this function

def check_in(book_title: str) -> str:
    books.append(book_title)

# 1.7 TODO: Check in 'THE POWER OF MOMENTS' using the check_in function

check_in("THE POWER OF MOMENTS")

# 1.8 TODO: Run the 'available_books' function to see if the book was checked in

available_books()

print('-----------------------')
# 1.9 TODO: Create a function 'search_by_name' that prints 'Available' if exists in books list, 'Not Available' if it doesn't.
# Parameters: book_title (string)
# Return: Not needed for this function

def search_by_name(book_title: str) -> str:

    if book_title in books:
        print("Available")
    else:
        print("Not Available")


# 1.10 TODO: Search for the book 'JUST MERCY'

search_by_name("JUST MERCY")

# 1.11 TODO: Search for the book '4000 WEEKS'

search_by_name("4000 WEEKS")

# Here's the same list of books, with additional details

books_with_details = [
    {
        'title': 'MY OWN WORDS',
        'author': 'Ruth Bader Ginsburg with Mary Hartnett and Wendy W Williams',
        'description': 'A collection of articles and speeches by the Supreme Court justice.'
    },
    {
        'title': 'THE BODY KEEPS THE SCORE',
        'author': 'Bessel van der Kolk',
        'description': 'How trauma affects the body and mind, and innovative treatments for recovery.'
    },
    {
        'title': 'STAMPED FROM THE BEGINNING',
        'author': 'Ibram X Kendi',
        'description': 'Winner of the 2016 National Book Award for nonfiction. A look at anti-Black racist ideas and their effect on the course of American history.'
    },
    {
        'title': 'JUST MERCY',
        'author': 'Bryan Stevenson',
        'description': 'A civil rights lawyer and MacArthur grant recipient\'s memoir of his decades of work to free innocent people condemned to death.'
    },
    {
        'title': 'BORN A CRIME',
        'author': 'Trevor Noah',
        'description': 'A memoir about growing up biracial in apartheid South Africa by the host of “The Daily Show.”'
    },

    {
        'title': 'ON TYRANNY',
        'author': 'Timothy Snyder',
        'description': 'Twenty lessons from the 20th century about the course of tyranny.'
    },
    {
        'title': 'HOMO DEUS: A BRIEF HISTORY OF TOMORROW',
        'author': 'Yuval Noah Harari',
        'description': 'Following the success of Sapiens, Yuval Noah Harari looks to the future to see where we\'re headed.',
    },
    {
        'title': 'THE WARMTH OF OTHER SUNS',
        'author': 'Isabel Wilkerson',
        'description': 'An account of the Great Migration of 1915-70, in which six million African-Americans abandoned the South.'
    },
    {
        'title': 'THE NEW JIM CROW',
        'author': 'Michelle Alexander',
        'description': 'A law professor on the “war on drugs” and its role in the disproportionate incarceration of Black men.'
    },
    {
        'title': 'THE PEOPLE WE KEEP',
        'author': 'Allison Larkin',
        'description': 'First-person narrative follows the life of April Sawicki as she navigates coming of age.'
    },
    {
        'title': 'BRAIDING SWEETGRASS',
        'author': 'Robin Wall Kimmerer',
        'description': 'A botanist and member of the Citizen Potawatomi Nation espouses having an understanding and appreciation of plants and animals.'
    },
    {
        'title': 'MY GRANDMOTHER\'S HANDS',
        'author': 'Resmaa Menakem',
        'description': 'A therapist who specializes in trauma, body-centered psychotherapy and violence prevention explains racism\'s effect on the body.'
    },
    {
        'title': 'THE ROAD TO UNFREEDOM',
        'author': 'Timothy Snyder',
        'description': 'Snyder explores Russian attempts to influence Western democracies and the influence of philosopher Ivan Ilyin on Russian President Vladimir Putin and the Russian Federation in general.'
    }
]


# 2.0 TODO: In a comment, describe the structure of the data in books_with_details.
# What types of data are nested within others? How do you know?

# The structure is a List of dictionaries. Its a list because it begins with "[" and ends with "]" then inside the list
# we have dictionaries whish are enclosed in  '{}'. Each dictionary consists of three key:value pairs. 

# 2.1 TODO: Create a function called 'count_books' that returns the number of books in the books_with_details list
# Parameters: Not needed for this function
# Return: number of books (integer)

def count_books():
    book_count = len(books_with_details)
    return book_count

# 2.2 TODO: Check the number of books available in the books list using the `count_books` function
# HINT: Does `return` print anything out? NO

# print(count_books())

# 2.3 TODO: Create a function 'search_by_author' that returns the titles of books by an author
# Parameters - author (string)
# Return - author's books (list of strings)
# Hint - You will need a for loop, if statement, and .append() for this solution!

def search_by_author(author: str) -> str:

    book = []
    for books in books_with_details:
        if books["author"] == author:
            book.append(books["title"])
    return book
    
# 2.4 TODO: Search for book titles by the author 'Yuval Noah Harari' using the search_by_author function
# HINT: Remember again-- return doesn't print anything out. How can we print the output of the function?
# print(search_by_author("Yuval Noah Harari"))