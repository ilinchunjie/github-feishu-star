import requests
import feishu
import github

def get_headers():
    headers = {
        "Authorization": f"Bearer {feishu.feishu.access_token}",
        "Content-Type": "application/json; charset=utf-8",
    }
    return headers

def get_obj_token(node_token):
    url = f"https://open.feishu.cn/open-apis/wiki/v2/spaces/get_node?token={node_token}"
    headers = get_headers()
    r = requests.get(url, headers=headers)
    obj_token = r.json()["data"]["node"]["obj_token"]
    return obj_token

def get_add_records(starred_repos, existed_names):
    records = []
    for repo in starred_repos:
        if repo.name not in existed_names:
            records.append({
                "fields": {
                    "Name": repo.name,
                    "URL": {
                        "link": repo.url,
                        "text": repo.name
                    },
                    "Description": repo.description,
                    "Topics": repo.topics,
                    "Language": repo.language,
                    "Star": repo.stars,
                }
            })
    return records