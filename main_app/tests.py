from django.test import TestCase


# Create your tests here.
class S3TestCase(TestCase):
    def download_exe(self):
        res = self.client.get(
            "/download_exe/", data={"object_key": "EXECUTOR_OBJECT_KEY"}
        )
        self.assertEqual(res.status_code, 200)

    def lastest_version(self):
        res = self.client.get("/lastest_version/")
        self.assertEqual(res.status_code, 200)
        print(res.content)
