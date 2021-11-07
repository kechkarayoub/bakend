from django.test import TestCase
from .utils import date_from_string, send_email, get_static_logo_url, get_img_as_base64
from django.core import mail
from django.conf import settings
import datetime
import base64
import requests


class UtilsTest(TestCase):

    def setUp(self):
        pass

    def test_date_from_string(self):
        date_obj = date_from_string('01/01/2021')
        self.assertEqual(date_obj, datetime.datetime(2021, 1, 1, 0, 0))
        date_obj = date_from_string('25/01/2021')
        self.assertEqual(date_obj, datetime.datetime(2021, 1, 25, 0, 0))
        date_obj = date_from_string('25/001/2021')
        self.assertEqual(date_obj, None)
        date_obj = date_from_string('2021/01/21')
        self.assertEqual(date_obj, None)

    def test_send_email(self):
        send_email("subject", "message_txt", ['edxkls2019@gmail.com'], html_message=None)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "subject")
        self.assertIn("message_txt", mail.outbox[0].body)

    def test_get_static_logo_url(self):
        self.assertEqual(settings.BACKEND_URL + "/static/images/logo.jpg", get_static_logo_url())

    # def test_get_img_as_base64(self):
    #     base64_to_compare = base64.b64encode(requests.get(get_static_logo_url()).content).decode('ascii')
    #     # self.assertEqual(base64_to_compare, get_img_as_base64(get_static_logo_url()))

