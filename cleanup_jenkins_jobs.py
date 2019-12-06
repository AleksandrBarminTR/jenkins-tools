import os
import requests
from jenkins_tools import check_jenkins_available
from jenkins_credentials import jobs_directory_name
from jenkins_credentials import jenkins_host
from jenkins_credentials import jenkins_user_password
from jenkins_credentials import jenkins_user_login
from jenkins_tools import is_job_folder


def get_jenkins_delete_endpoint(folder_name: str):
    return jenkins_host + "/job/" + folder_name + "/doDelete"


def remove_top_level_job(folder_name: str):
    print("Removing top-level job " + folder_name)
    auth = requests.auth.HTTPBasicAuth(jenkins_user_login, jenkins_user_password)
    endpoint = get_jenkins_delete_endpoint(folder_name)
    response = requests.post(endpoint, auth=auth)
    if response.status_code == 200:
        print("... done")
    else:
        raise Exception("Can't delete a job with name " + folder_name)


def remove_top_level_jobs():
    for folder in os.listdir(jobs_directory_name):
        if is_job_folder(os.listdir(jobs_directory_name + "//" + folder)):
            remove_top_level_job(folder)


if __name__ == '__main__':
    check_jenkins_available()
    remove_top_level_jobs()
