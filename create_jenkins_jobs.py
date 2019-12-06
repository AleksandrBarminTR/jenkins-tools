import os
import requests
import requests.auth
from jenkins_credentials import jenkins_host
from jenkins_credentials import jenkins_user_password
from jenkins_credentials import jenkins_user_login
from jenkins_credentials import jobs_directory_name
from jenkins_tools import check_jenkins_available
from jenkins_tools import is_job_folder
from jenkins_tools import config_file_name


jenkins_create_part = "createItem"


def process_jobs(parent_directory: str):
    for current, subdirs, files in os.walk(parent_directory):
        process_job_folder(current, files)


def process_job_folder(folder_name: str, files: []):
    if is_job_folder(files):
        create_jenkins_job(folder_name)


def create_jenkins_job(folder_name: str):
    print("Creating job from folder " + folder_name)
    headers = {
        "Content-Type": "application/xml"
    }
    data = open(folder_name + "\\" + config_file_name, "r").read()
    auth = requests.auth.HTTPBasicAuth(jenkins_user_login, jenkins_user_password)
    endpoint = get_jenkins_create_endpoint(folder_name)
    response = requests.post(endpoint, auth=auth, data=data, headers=headers)
    if response.status_code == 200:
        print("... done")
    else:
        raise Exception("Can't create a job with name " + folder_name)


def get_jenkins_create_endpoint(folder_name: str):
    folder_name = folder_name.replace(jobs_directory_name + "\\", "")
    parts = folder_name.split("\\")
    new_job_name = parts[len(parts) - 1]
    parts.remove(new_job_name)
    endpoint = jenkins_host
    if len(parts) > 0:
        endpoint += "/job/" + "/job/".join(parts)
    return endpoint + "/" + jenkins_create_part + "?name=" + new_job_name


if __name__ == '__main__':
    check_jenkins_available()
    process_jobs(jobs_directory_name)
