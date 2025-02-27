import common
import os
import requests
class Feishu:
    app_id = ""
    app_secret = ""
    access_token = ""

    def __init__(self):
        self.access_token = self.get_access_token()
        self.app_id = os.environ.get("FEISHU_APP_ID")
        self.app_secret = os.environ.get("FEISHU_APP_SECRET")
        print(self.app_id)
        return

    def get_access_token(self):
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
        post_data = {
            "app_id": self.app_id,
            "app_secret": self.app_secret
        }
        r = requests.post(url, json=post_data)
        return r.json()["tenant_access_token"]
    
feishu = Feishu()