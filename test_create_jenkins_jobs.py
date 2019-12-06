from unittest import TestCase
from create_jenkins_jobs import is_job_folder


class TestCreateJenkinsJobs(TestCase):
    def test_is_job_folder_empty_should_not_be(self):
        files = []
        self.assertFalse(is_job_folder(files))

    def test_is_job_folder_should_not_be(self):
        files = ["file.xml"]
        self.assertFalse(is_job_folder(files))

    def test_is_job_folder_shod_be(self):
        files = ["config.xml"]
        self.assertTrue(is_job_folder(files))


if __name__ == '__main__':
    TestCreateJenkinsJobs.main()
