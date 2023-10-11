'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DO NOT EDIT THIS FILE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

import io
from unittest import mock, TestCase

from library import books, available_books, check_out, check_in, search_by_name, count_books, search_by_author, books_with_details



class TestLibraryFunctions(TestCase):

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_available_books(self, mock_stdout):
        available_books()

        expected = '\n'.join(books) + '\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_check_out(self, mock_stdout):
        check_out('THE PEOPLE WE KEEP')
        available_books()

        expected = '\n'.join(books) + '\n'

        self.assertEqual(expected, mock_stdout.getvalue())
        self.assertNotIn('THE PEOPLE WE KEEP', books)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_check_in(self, mock_stdout):
        check_in('DECOLONIZE WEALTH')
        available_books()

        expected = '\n'.join(books) + '\n'

        self.assertEqual(expected, mock_stdout.getvalue())
        self.assertIn('DECOLONIZE WEALTH', books)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_name(self, mock_stdout):
        search_by_name('BRAIDING SWEETGRASS')
        search_by_name('ERAGON')

        expected = 'Available\nNot Available\n'

        self.assertEqual(expected, mock_stdout.getvalue())

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_count_books(self, mock_stdout):
        self.assertEqual(len(books_with_details), count_books())

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_by_author(self, mock_stdout):
        larkin_books = search_by_author('Allison Larkin')
        harari_books = search_by_author('Yuval Noah Harari')
        mead_books = search_by_author('Richelle Mead')
        
        self.assertEqual(larkin_books, ['THE PEOPLE WE KEEP'])
        self.assertEqual(harari_books, ['HOMO DEUS: A BRIEF HISTORY OF TOMORROW'])
        self.assertEqual(mead_books, [])
        
