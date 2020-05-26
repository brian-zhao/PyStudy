import threading
import requests
import sys
import time

# Top 100 popular site.
urls = [
  'http://www.youtube.com',
  'http://www.facebook.com',
  'http://www.baidu.com',
  'http://www.yahoo.com',
  'http://www.amazon.com',
  'http://www.wikipedia.org',
  'http://www.qq.com',
  'http://www.google.co.in',
  'http://www.twitter.com',
  'http://www.live.com',
  'http://www.taobao.com',
  'http://www.bing.com',
  'http://www.instagram.com',
  'http://www.weibo.com',
  'http://www.sina.com.cn',
  'http://www.linkedin.com',
  'http://www.yahoo.co.jp',
  'http://www.msn.com',
  'http://www.vk.com',
  'http://www.google.de',
  'http://www.yandex.ru',
  'http://www.hao123.com',
  'http://www.google.co.uk',
  'http://www.reddit.com',
  'http://www.ebay.com',
  'http://www.google.fr',
  'http://www.t.co',
  'http://www.tmall.com',
  'http://www.google.com.br',
  'http://www.360.cn',
  'http://www.sohu.com',
  'http://www.amazon.co.jp',
  'http://www.pinterest.com',
  'http://www.netflix.com',
  'http://www.google.it',
  'http://www.google.ru',
  'http://www.microsoft.com',
  'http://www.google.es',
  'http://www.wordpress.com',
  'http://www.gmw.cn',
  'http://www.tumblr.com',
  'http://www.paypal.com',
  'http://www.blogspot.com',
  'http://www.imgur.com',
  'http://www.stackoverflow.com',
  'http://www.aliexpress.com',
  'http://www.naver.com',
  'http://www.ok.ru',
  'http://www.apple.com',
  'http://www.github.com',
  'http://www.chinadaily.com.cn',
  'http://www.imdb.com',
  'http://www.google.co.kr',
  'http://www.fc2.com',
  'http://www.jd.com',
  'http://www.blogger.com',
  'http://www.163.com',
  'http://www.google.ca',
  'http://www.whatsapp.com',
  'http://www.amazon.in',
  'http://www.office.com',
  'http://www.tianya.cn',
  'http://www.google.co.id',
  'http://www.youku.com',
  'http://www.rakuten.co.jp',
  'http://www.craigslist.org',
  'http://www.amazon.de',
  'http://www.nicovideo.jp',
  'http://www.google.pl',
  'http://www.soso.com',
  'http://www.bilibili.com',
  'http://www.dropbox.com',
  'http://www.xinhuanet.com',
  'http://www.outbrain.com',
  'http://www.pixnet.net',
  'http://www.alibaba.com',
  'http://www.alipay.com',
  'http://www.microsoftonline.com',
  'http://www.booking.com',
  'http://www.googleusercontent.com',
  'http://www.google.com.au',
  'http://www.popads.net',
  'http://www.cntv.cn',
  'http://www.zhihu.com',
  'http://www.amazon.co.uk',
  'http://www.diply.com',
  'http://www.coccoc.com',
  'http://www.cnn.com',
  'http://www.bbc.co.uk',
  'http://www.twitch.tv',
  'http://www.wikia.com',
  'http://www.google.co.th',
  'http://www.go.com',
  'http://www.google.com.ph',
  'http://www.doubleclick.net',
  'http://www.onet.pl',
  'http://www.googleadservices.com',
  'http://www.accuweather.com',
  'http://www.googleweblight.com',
  'http://www.answers.yahoo.com',
]

def worker():
    while True:
        try:
            url = urls.pop()
        except IndexError:
            break  # Done.

        requests.get(url)
        sys.stdout.write('Fetched url %s\n' % url)

start = time.time()
threads = []
for _ in range(100):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print('%.2f seconds' % (time.time() - start))