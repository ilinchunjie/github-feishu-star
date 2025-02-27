import common
import requests

class Record:
    record_id = ""
    fields = {}
    
    def __init__(self, record_id, fields):
        self.record_id = record_id
        self.fields = fields

class Table:
    node_token = ""
    app_token = ""
    table_id = ""
    page_size = 100
    records = []
    
    def __init__(self, node_token, table_id):
        self.node_token = node_token
        self.table_id = table_id
        self.app_token = common.get_obj_token(node_token)

    # https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/search?appId=cli_a73d9286913c500c
    def request_all_records(self):
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/tables/{self.table_id}/records/search?page_size={self.page_size}"
        headers = common.get_headers()
        post_data = {}
        self.records = []
        
        r = requests.post(url, headers=headers, json=post_data)
        data = r.json()
        self.insert_record(data)

        while data["code"] == 0 and data["data"]["has_more"]:
            page_token = data["data"]["page_token"]
            url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/tables/{self.table_id}/records/search?page_token={page_token}&page_size={self.page_size}"
            r = requests.post(url, headers=headers, json=post_data)
            data = r.json()
            self.insert_record(data)
        return
    
    def get_all_names_with(self, filed_name):
        names = []
        for record in self.records:
            names.append(record.fields[filed_name]["text"])
        return names
    
    def insert_record(self, data):
        if data["code"] != 0:
            return
        items = data["data"]["items"]
        for item in items:
            record_id = item["record_id"]
            fields = item["fields"]
            self.records.append(Record(record_id, fields))
        return
    
    # https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-record/create?appId=cli_a73d9286913c500c
    def add_record(self, data):
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/tables/{self.table_id}/records"
        headers = common.get_headers()
        post_data = {
            "fields": data
        }
        r = requests.post(url, headers=headers, json=post_data)
        if r.status_code != 200:
            print(r.text)
        return
    
    def add_records(self, datas):
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/tables/{self.table_id}/records/batch_create"
        headers = common.get_headers()
        post_data = {
            "records": datas
        }
        r = requests.post(url, headers=headers, json=post_data)
        print(r.text)
        return
    
    # https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-record/batch_create
    def add_records_with_limit(self, datas):
        for i in range(0, len(datas), 1000):
            self.add_records(datas[i:i+1000])
        return