import json

import scrapy

from yingdi.items import YingdiItem

def get_start_url(id="",web="1",seed="2",system="web"):
    base_url="http://www.iyingdi.cn/feed/list/seed?"
    return  base_url+"id="+id+"&wed="+web+"&seed="+seed+"&system="+system

class mySp(scrapy.Spider):
    name = 'iyingdi'
    allowed_domains = ["iyingdi.cn"]
    start_urls = ["http://www.iyingdi.cn/feed/list/seed?&web=1&seed=2&system=web",]

    def parse(self, response):
        response=json.loads(response.text)
        id=140000
        sourceID=0

        for feed_ in response["feeds"]:
            item=YingdiItem()

            item["author"]=feed_["feed"]["author"]
            item["id"]=feed_["feed"]["id"]
            item["pageview"]=feed_["feed"]["pageview"]
            item["reply"]=feed_["feed"]["reply"]
            item["seed"]=feed_["feed"]["seed"]
            item["seedTime"]=feed_["feed"]["seedTime"]
            item["sourceID"]=feed_["feed"]["sourceID"]
            item["title"]=feed_["feed"]["title"]

            id=feed_["feed"]["id"]
            sourceID=feed_["feed"]["sourceID"]


            yield item

        if(int(sourceID)>40000):
            url=get_start_url(id=str(id))
            yield scrapy.Request(url,callback=self.parse)






