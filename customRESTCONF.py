import requests

def customRESTCONF(action, host, endpoint, username, password, strData=None):
    requests.packages.urllib3.disable_warnings()
    baseUrl = f'https://{host}/restconf/data/'
    endpoint = endpoint
    headers = {
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json'
    }
    if action == 'get':
        with requests.get(
            url=baseUrl + endpoint,
            headers=headers,
            auth=(
                username,
                password
            ),
            verify=False
        ) as res:
            return res.text
    elif action == 'post':
        with requests.post(
            url=baseUrl + endpoint,
            headers=headers,
            auth=(
                username,
                password
            ),
            data=strData,
            verify=False
        ) as res:
            return res.status_code
    elif action == 'put':
        with requests.put(
            url=baseUrl + endpoint,
            headers=headers,
            auth=(
                username,
                password
            ),
            data=strData,
            verify=False
        ) as res:
            return res.status_code
    elif action == 'patch':
        with requests.patch(
            url=baseUrl + endpoint,
            headers=headers,
            auth=(
                username,
                password
            ),
            data=strData,
            verify=False
        ) as res:
            return res.status_code
    elif action == 'delete':
        with requests.delete(
            url=baseUrl + endpoint,
            headers=headers,
            auth=(
                username,
                password
            ),
            verify=False
        ) as res:
            return res.status_code
