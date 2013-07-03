from session import SessionStore
from django.test import TestCase
from django.contrib.sessions.tests import SessionTestsMixin

class RiakSessionTests(SessionTestsMixin, TestCase):
    backend = SessionStore
