from django.test import TestCase

from store.models import Book
from store.serializers import BooksSerializer


class BooksSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Test 1', price=100, author_name='Author 1', owner=None)
        book_2 = Book.objects.create(name='Test 2', price=200, author_name='Author 2', owner=None)
        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test 1',
                'price': 100,
                'author_name': 'Author 1',
                'owner': None,
            },
            {
                'id': book_2.id,
                'name': 'Test 2',
                'price': 200,
                'author_name': 'Author 2',
                'owner': None,
            }
        ]
        self.assertEqual(expected_data, data)
