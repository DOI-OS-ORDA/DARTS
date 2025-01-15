from django.test import TestCase

from search.structs.search_result import SearchResultStruct

class SearchResultStructTest(TestCase):

    def setUp(self):
        self.data = {
            'id': 1,
            'title': 'Document title',
            'highlight': 'This is a <span class="highlight">search term</span>.',
        }
        self.subject = SearchResultStruct(self.data)

    def test_responds_to_given_attributes(self):
        self.assertEqual(self.data['id'], self.subject.id)
        self.assertEqual(self.data['title'], self.subject.title)
        self.assertEqual(self.data['highlight'], self.subject.highlight)
