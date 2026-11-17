from urllib.parse import urlencode

from django.core.exceptions import RequestDataTooBig
from django.test import SimpleTestCase, override_settings
from rest_framework.test import APIRequestFactory

from .views import CustomAuthToken


@override_settings(DATA_UPLOAD_MAX_MEMORY_SIZE=64)
class LoginRequestSizeTests(SimpleTestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CustomAuthToken.as_view()

    def test_oversized_json_and_form_bodies_are_rejected(self):
        payload = {"username": "x" * 256}
        requests = (
            self.factory.post("/api/accounts/login/", payload, format="json"),
            self.factory.generic(
                "POST",
                "/api/accounts/login/",
                data=urlencode(payload),
                content_type="application/x-www-form-urlencoded",
            ),
        )

        for request in requests:
            with self.subTest(content_type=request.META["CONTENT_TYPE"]):
                with self.assertRaises(RequestDataTooBig):
                    self.view(request)

    def test_small_json_body_reaches_normal_validation(self):
        request = self.factory.post(
            "/api/accounts/login/", {"username": "example"}, format="json"
        )

        response = self.view(request)

        self.assertEqual(response.status_code, 400)
        self.assertIn("password", response.data)
