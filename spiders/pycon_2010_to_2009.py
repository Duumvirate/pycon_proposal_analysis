import scrapy


class QuotesSpider(scrapy.Spider):
    name = "proposal_analysis"
    start_urls = [
        'http://pyvideo.org/events/pycon-us-2010.html',
        #'http://pyvideo.org/events/pycon-us-2009.html',
    ]

    def parse(self, response):
        
        for talk in response.css('article.list_item'):
            raw_title = talk.css("div").css("a::attr(title)").extract()[0]
            title = raw_title.lstrip("Permalink to ")
            yield {
                "title": title,
                "authors": talk.css("footer").css("address").css("a::text").extract()
            }
        """
        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        """
