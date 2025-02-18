from django.test import TestCase

from search.structs.struct import Struct

class StructTest(TestCase):
    def setUp(self):
        self.data = {
            'id': 1,
            'title': 'Document title',
            'highlight': 'This is a <span class="highlight">search term</span>.',
        }
        self.subject = Struct(self.data)

    def test_responds_to_given_attributes(self):
        self.assertEqual(self.data['id'], self.subject.id)
        self.assertEqual(self.data['title'], self.subject.title)
        self.assertEqual(self.data['highlight'], self.subject.highlight)

