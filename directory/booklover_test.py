import unittest
from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        book_test = BookLover("Alice", "alice@example.com", "fantasy")
        book_test.add_book("Jane Eyre", 4)
        self.assertIn("Jane Eyre", book_test.book_list['book_name'].tolist())

    def test_2_add_book(self):
        book_test = BookLover("Bob", "bob@example.com", "science fiction")
        book_test.add_book("Dune", 5)
        book_test.add_book("Dune", 5)
        self.assertEqual(len(book_test.book_list[book_test.book_list['book_name'] == 'Dune']), 1)

    def test_3_has_read(self):
        book_test = BookLover("Charlie", "charlie@example.com", "mystery")
        book_test.add_book("Sherlock Holmes", 5)
        self.assertTrue(book_test.has_read("Sherlock Holmes"))

    def test_4_has_not_read(self):  # Rename to ensure uniqueness
        book_test = BookLover("David", "david@example.com", "thriller")
        book_test.add_book("Gone Girl", 4)
        self.assertFalse(book_test.has_read("The Girl with the Dragon Tattoo"))

    def test_5_num_books_read(self):
        book_test = BookLover("Emma", "emma@example.com", "historical fiction")
        book_test.add_book("Pride and Prejudice", 5)
        book_test.add_book("Sense and Sensibility", 4)
        book_test.add_book("Emma", 5)
        self.assertEqual(book_test.num_books_read(), 3)

    def test_6_fav_books(self):
        book_test = BookLover("Frank", "frank@example.com", "fiction")
        book_test.add_book("The Great Gatsby", 5)
        book_test.add_book("To Kill a Mockingbird", 4)
        book_test.add_book("1984", 3)
        fav_books = book_test.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))

if __name__ == '__main__':
    unittest.main(verbosity=2)


