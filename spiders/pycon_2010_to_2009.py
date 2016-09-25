import scrapy


class QuotesSpider(scrapy.Spider):
    name = "proposal_analysis"
    start_urls = [
        'http://pyvideo.org/events/pycon-us-2010.html',
        #'http://pyvideo.org/events/pycon-us-2009.html',
    ]

    def parse(self, response):
        for quote in response.css('article.list_item.div'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
