import requests
from jenkins_credentials import jenkins_host
from jenkins_credentials import jenkins_user_password
from jenkins_credentials import jenkins_user_login


jenkins_api_endpoint = jenkins_host + "/api/"
config_file_name = "config.xml"


def get_jenkins_xml_endpoint():
    return jenkins_api_endpoint + "xml"


def check_jenkins_available():
    print("Checking if Jenkins available")
    auth = requests.auth.HTTPBasicAuth(jenkins_user_login, jenkins_user_password)
    response = requests.get(get_jenkins_xml_endpoint(), auth=auth)
    if response.status_code != 200:
        raise Exception("Jenkins is not available")
    else:
        print("... Checked, Jenkins works")


def is_job_folder(files: []):
    return config_file_name in files
