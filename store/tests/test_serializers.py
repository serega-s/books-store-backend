from django.test import TestCase

from store.models import Book
from store.serializers import BooksSerializer


class BooksSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Test 1', price=100)
        book_2 = Book.objects.create(name='Test 2', price=200)
        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test 1',
                'price': '100.00'
            },
            {
                'id': book_2.id,
                'name': 'Test 2',
                'price': '200.00'
            }
        ]
        self.assertEqual(expected_data, data)
