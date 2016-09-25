import scrapy


class pycon_2015_Spider(scrapy.Spider):
    name = 'proposal_analysis'

    start_urls = ['https://us.pycon.org/2015/schedule/talks/list/']

    def parse(self, response):
        # follow links to talk pages
        for href in response.css('div.row>div>h3>a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href),
                                 callback=self.parse_talk)

    def parse_talk(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            'name': extract_with_css('.box-content>h2::text'),
        }
