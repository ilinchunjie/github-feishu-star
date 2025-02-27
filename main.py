import os
import table
import github
import common

def main():
    env_node_token = os.environ.get("FEISHU_NODE_TOKEN")
    env_table_id = os.environ.get("FEISHU_TABLE_ID")
    env_github_token = os.environ.get("TOKEN_GITHUB")
    feishu_table = table.Table(env_node_token, env_table_id)
    feishu_table.request_all_records()
    existed_names = feishu_table.get_all_names_with("Name")
    github_data = github.GitHub(env_github_token)
    starred_repos = github_data.get_starred_repos()
    records = common.get_add_records(starred_repos, existed_names)
    feishu_table.add_records_with_limit(records)
    return

main()