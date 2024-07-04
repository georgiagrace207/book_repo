import pandas as pd

# TASK 1


class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        if book_list is None:
            self.book_list = pd.DataFrame({'book_name': [], 'book_rating': []})
        else:
            self.book_list = book_list

# Method 1:
    def add_book(self, book_name, rating):
        if any(self.book_list['book_name'] == book_name):
            print(f"'{book_name}' already exists in list")
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
            print(f"'{book_name}' (rating: {rating}) successfully added to list")

# Method 2:
    def has_read(self, book_name):
        if any(self.book_list['book_name'] == book_name):
            return True
        else:
            return False

# Method 3:
    def num_books_read(self):
        return self.num_books

# Method 4:
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]

# Testing with the examples given:
if __name__ == "__main__":
    test_object = BookLover("Alice", "alice@example.com", "fantasy")

    test_object.add_book("Jane Eyre", 4)
    test_object.add_book("Fight Club", 3)
    test_object.add_book("The Divine Comedy", 5)
    test_object.add_book("The Popol Vuh", 5)

    test_object.add_book("Jane Eyre", 4)

    print(f"Has Alice read 'Jane Eyre'? {test_object.has_read('Jane Eyre')}")
    print(f"Has Alice read '1984'? {test_object.has_read('1984')}")

    print(f"Number of books Alice has read: {test_object.num_books_read()}")

    print("\nAlice's favorite books:")
    print(test_object.fav_books())


# TASK 2







# TASK 3















