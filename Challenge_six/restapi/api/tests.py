import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django

django.setup()
from django.test import TestCase


class TestChallenge10(TestCase):
    def test_0(self):
        response = self.client.post('/lambda/', {"question": [2, 3, 2, 4, 5, 12, 2, 3]},
                                    content_type='application/json')
        assert isinstance(response.data, dict)
        self.assertEqual(response.status_code, 200)

    def test_01(self):
        response = self.client.post('/lambda/', {"question": [2, 3, 2, 4, 5, 12, 2, 3]},
                                    content_type='application/json')
        assert len(response.data['solution']) == 8
        self.assertEqual(response.status_code, 200)

    # def test_post_empty_data(self):
    #     response = self.client.post('/lambda/', {}, content_type='application/json')
    #     self.assertEqual(response.status_code, 400)
    #
    # def test_post_invalid_data(self):
    #     response = self.client.post('/lambda/', {"question": [2, "abc", {}, 12, 2, 3]},
    #                                 content_type='application/json')
    #     self.assertEqual(response.status_code, 400)
    #
    # def test_solution_empty_list_sort(self):
    #     res = _solution_list_sort([])
    #     self.assertSequenceEqual([], res)
