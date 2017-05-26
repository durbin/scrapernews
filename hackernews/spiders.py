import scrapy
from hackernews.models import Item

class ItemsSpider(scrapy.Spider):
    name = 'items_spider'
    start_urls = ['https://news.ycombinator.com/']

    def parse(self, response):
        """
        Hackernews doesn't wrap all of the story data in one element, they are
        in different table rows, so we need to scrap data from two rows and then
        merge the data into one dictionary.
        """
        stories = []
        for thing in response.css('.athing'):
            stories.append({ 
                    'hnid': int(thing.css('::attr(id)').extract_first()),
                    'url': thing.css('.storylink').xpath('@href').extract_first(),
                    'title': thing.css('.storylink::text').extract_first() } )

        subtexts = []
        for sub in response.css('.subtext'):
            subtexts.append({ 
                    'hacker': sub.css('.hnuser::text').extract_first(),
                    'points': sub.css('.score::text').extract_first() })

        for i, story in enumerate(stories):
            z = self.merge_dicts(story, subtexts[i])
            print(z)

            obj, created = Item.objects.get_or_create(
                hnid=z['hnid'],
                defaults=z,
            )


        next_page = response.css('.morelink ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)


    def merge_dicts(self, x, y):
        z = x.copy()
        z.update(y)
        return z