from django.test import TestCase

def say_hello(is_hello=True):
    if is_hello:
        return 'hello'

class SayHelloTestCase(TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello(), 'hello')

    def test_say_hi(self):
        self.assertNotEqual(say_hello(False), 'hello')

    def test_say_empty(self):
        self.assertEqual(say_hello(False), None)