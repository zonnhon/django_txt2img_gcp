# 時事輿論視覺化Website
## Introduction
本網站以網路爬蟲自動蒐集論壇熱門文章，透過GPT對文章及其留言統整及摘要為簡短英文敘述，並將英文摘要傳遞給AI圖像生成模型(Stable Diffusion)生成具有文章內容意象之圖像，進行趣味性呈現。\
網站以Django框架建置，透過視圖機制動態插入內容，以AJAX Request動態更新頁面內容。
## Tech Stack
• **Framework**: Django\
• **Database**: PostgreSQL\
• **Deployment**: GCP

## Preview
![zonnweb site_demo1](https://github.com/zonnhon/django_txt2img_gcp/assets/57436816/93216a8d-20e6-49da-9f45-359a39e49de9)
![zonnweb site_demo2](https://github.com/zonnhon/django_txt2img_gcp/assets/57436816/76b47743-347f-4b5f-8595-a18d2949005b)
