# github-feishu-star

使用飞书多维表格和 Github Actions 同步和管理你的 Github Star.

## 功能

支持使用 Github Actions 定时同步增量的 Star 到飞书

## 使用

- 创建飞书应用，[参考文档](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/Attendance/Development_Guide?lang=zh-CN)
- Fork 当前仓库
- 在仓库的设置页面添加环境变量
  - `FEISHU_APP_ID` 创建的飞书应用的 App ID
  - `FEISHU_APP_SECRET` 创建的飞书应用的 App Secret
  - `FEISHU_NODE_TOKEN` 飞书多维表格 App 的唯一标识，[获取方式](https://open.feishu.cn/document/server-docs/docs/bitable-v1/bitable-overview#-752212c)
  - `FEISHU_TABLE_ID` 飞书多维表格数据表的唯一标识
    ![image](https://github.com/user-attachments/assets/81e9da53-ef06-480b-af63-9663566692b8)
  - `TOKEN_GITHUB` Github 的用户 Token，用于获取当前用户的 API，[获取方式](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)

# 参考

https://github.com/lcjnil/github-notion-star
