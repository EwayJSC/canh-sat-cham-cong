# Cảnh sát chấm công

Environment: python3.5, pip

Tool được phát triển bởi đội devs của EWAY - ứng phó nhanh với việc làm remote 
trong đại dịch Covid-19.

## Mô hình

Slack --> This server --> AirTable

1. Nhân sự vào group dự án của mình, báo cáo đầu giờ sáng, có `[Daily]` theo mẫu:

```
[Daily]
Hôm qua làm gì:
    - uống cafe
    - xem netflix
Hôm nay làm gì:
    - cắt móng tay cho mèo
Khó khăn gặp phải:
    - mạng chậm
```

2. Kết quả

Trên AirTable có kết quả như này, có thể group by theo các field khác nhau để
ra report khác:

![Kết quả](https://i.imgur.com/LjcbJyi.png)


## Cách tích hợp:

### Tạo AirTable

1. Đăng ký tài khoản AirTable tại https://airtable.com
2. Tạo workspace cho team bạn
3. Vào copy template này: Bấm nút `Copy Base` https://airtable.com/shrInimCTGmlwoENx
4. Lấy Base ID và API Key 

### Deploy

- Deploy code lên một server bất kỳ (có thể work luôn với Heroku)
- Edit config:

```
AIRTABLE_TOKEN=<your_airtable_api_key>
AIRTABLE_BASE=<your_airtable_base_id>
SLACK_BOT_TOKEN=<cái này update sau>
```

- Deploy --> Expose URL

### Vào Slack tạo bot

Vì Slack chỉ share được bot app khi mà dùng chung server với nhau nên các team
khác nhau nên tự tạo bot cho privacy.

- Vào https://api.slack.com/apps --> Create New App
- Ở OAuth & Permissions: Phần Scopes --> Bot Token Scopes
Thêm quyền như sau:

![Image](https://i.imgur.com/UN6PxAS.png)

- Ở App Home: Điền display name, avatar cho bot của bạn trong phần 
`How Your App Displays`
- Install App --> Copy Bot OAuth Token --> Add vào config SLACK_BOT_TOKEN của 
server
- Ở Event Subscriptions --> Enable Events
    - Request URL: http://<your.server.url>/slackbot
    ![Image](https://i.imgur.com/L8vwKxn.png)
    - Subscribe to bot events:
    ![Image](https://i.imgur.com/JVIENFD.png)
- Save Config
- Re-install your app

### Sử dụng

- Vào channel nào mà team dùng để daily report
- Add bot vào group
- Báo cáo hàng ngày với `[Daily]` ở đầu

## Authors:

1. dungnd@eway.vn
2. tienhm@eway.vn
