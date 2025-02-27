
import requests

class Repository:
    name = ""
    url = ""
    description = ""
    stars = 0
    language = ""
    topics = []

    def __init__(self, repo):
        self.name = repo["name"]
        self.url = repo["clone_url"]
        self.description = repo["description"]
        self.stars = repo["stargazers_count"]
        self.language = repo["language"]
        self.topics = repo["topics"]

class GitHub:
    access_token = ""
    page_size = 100

    def __init__(self, access_token):
        self.access_token = access_token

    def get_starred_repos(self):
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Accept": "application/vnd.github.v3+json"
        }

        page = 1
        starred_repos = []
        while True:
            url = f"https://api.github.com/user/starred?per_page={self.page_size}&page={page}"
            response = requests.get(url, headers=headers)

            if response.status_code != 200:
                break

            repos = response.json()
            if not repos:
                break

            
            for repo in repos:
                starred_repos.append(Repository(repo))

            link_header = response.headers.get("Link", "")
            if "rel=\"next\"" not in link_header:
                break

            page += 1
        
        return starred_repos