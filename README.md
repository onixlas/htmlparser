# htmlparser

## Usage
```console
# Build image
docker build -t onixlas/htmlparser:latest .

# Run instance
docker run --restart unless-stopped -d -p 0.0.0.0:8000:8000 onixlas/htmlparser:latest
```

## Commentary
This app was optimized for parsing news sites (but not only them). Ex.:
* [sport.ru](https://www.sport.ru/football/fenerbahche-obyyavil-o-naznachenii-mourinyu-na-post-glavnogo-trenera/article585530/)
* [forbes.ru](https://www.forbes.ru/investicii/504686-blokcejn-platforma-terraform-labs-podala-zaavlenie-o-bankrotstve)
* [ria.ru](https://ria.ru/20240530/biolog-1949309238.html)
* [wikipedia](https://ru.wikipedia.org/wiki/OpenAI)
* [rudn.ru](https://www.rudn.ru/media/news/admission/priemnaya-kampaniya-2024-v-rudn-polezno-uznat)
