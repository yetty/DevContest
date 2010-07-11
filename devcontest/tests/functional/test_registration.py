from devcontest.tests import *

class TestRegistrationController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='registration', action='index'))
        # Test response...
