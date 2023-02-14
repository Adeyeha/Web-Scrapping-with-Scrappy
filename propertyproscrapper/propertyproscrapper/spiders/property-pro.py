from gc import callbacks
import scrapy


class PropertyProSpider(scrapy.Spider):
    name = 'property_pro'
    start_urls = ['https://www.propertypro.ng/property']
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

    def parse(self,response):
        for product in response.css('div.single-room-sale.listings-property'):
            link = product.css('div.single-room-text').css('a::attr(href)')
            dt = {
                'title': product.css('h3.listings-property-title2::text').get(),
                'details_link': product.css('div.single-room-img.result-img a::attr(href)').get(),
                'image_link': product.css('div.single-room-img.result-img').css('a').css('img.listings-img::attr(src)').get(),
                'details_link_2': product.css('div.single-room-text').css('a::attr(href)').get(),
                'title_2': product.css('div.single-room-text').css('a').css('h4.listings-property-title::text').get(),
                'address' : product.css('div.single-room-text').css('h4::text')[1].get(),
                'price' : product.css('div.single-room-text').css('div.n50').css('h3.listings-price').css('span::text').getall(),
                'category' : product.css('div.single-room-text').css('div.n50').css('h4::text').get(),
                'timeline': product.css('div.single-room-text').css('h5::text').getall(),
                'id': product.css('div.single-room-text').css('h2::text').get(),
                'category_2': product.css('div.single-room-text').css('div.furnished-btn').css('a::text').get(),
                'description':  product.css('div.single-room-text').css('div.result-list-details').css('p.d-none.d-sm-block::text').get(),
                'details_link_2': product.css('div.single-room-text').css('div.result-list-details').css('p.d-none.d-sm-block').css('a::attr(href)').get(),
                'attributes':  product.css('div.single-room-text').css('div.fur-areea').css('span::text').getall(),
                'agent_link': product.css('div.single-room-text').css('div.elite-icon').css('a::attr(href)').get(),
                'phone_no' : product.css('div.single-room-text').css('div.phone-icon::text').getall()
            }
            yield response.follow(link.get(),callback=self.parse_details, meta=dt)

        next_page = f"https://www.propertypro.ng{response.css('a.page-link::attr(href)')[4].get()}"

        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)

    def parse_details(self,response):
        yield {
            'main_details' : response.meta,
            'key_features' : response.css('div.key-features-list').getall(),
            'pictures' : response.css('img.slider-nav-img::attr(src)').getall(),
            'description_details' : response.css('div.description-text').getall()
        }



class NigerianPropertySpiderSale(scrapy.Spider):
    name = 'nigerianpropertysale'
    start_urls = ['https://nigeriapropertycentre.com/for-sale']
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'


    def parse(self,response):
        for product in response.css('div.row.property-list'):
            link = product.css('div.wp-block-content.clearfix.text-xs-left.text-sm-left a::attr(href)')
            dt =  {
                'title' : product.css('div.wp-block-title.hidden-xs h3::text').getall(),
                'front_image' : product.css('img.sm-width-min-200-max-250.xs-width-min-200-max-350::attr(src)').get(),
                'details_link' : product.css('div.wp-block-content.clearfix.text-xs-left.text-sm-left a::attr(href)').get(),
                'content_title' : product.css('div.wp-block-content.clearfix.text-xs-left.text-sm-left h4.content-title::text').get(),
                'address' :  product.css('address.voffset-bottom-10 strong::text').get(),
                'description' :  product.css('div.description.hidden-xs p::text').getall(),
                'added_on' :  product.css('span.added-on::text').get(),
                'price' :  product.css('span.price::text').getall(),
                'agent' : product.css('span.marketed-by.pull-right.hidden-xs.hidden-sm.text-right::text').get(),
                'agent_no' : product.css('span.marketed-by.pull-right.hidden-xs.hidden-sm.text-right strong::text').getall(),
                'features' : product.css('ul.aux-info li span::text').getall()
            }
            yield response.follow(link.get(),callback=self.parse_details,meta=dt)
            


        next_page = f"https://nigeriapropertycentre.com/for-sale{response.css('ul.pagination li a::attr(href)').getall()[-1]}"

        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)

    def parse_details(self,response):
        yield {
            'main_details' : response.meta,
            'agent_name' : response.css('div.col-md-4 div.panel-body p a strong::text').getall(),
            'agent_dets' : response.css('div.col-md-4 div.panel-body p::text').getall(),
            'agent_website' : response.css('div.col-md-4 div.panel-body p a::attr(href)').getall(),
            'images' : response.css('div.col-sm-12.images-inner-container li img::attr(src)').getall(),
            'description' : response.css('div.tab-body p::text').getall(),
            'table' : response.css('table.table.table-bordered.table-striped td').getall()
        }


class NigerianPropertySpiderRent(scrapy.Spider):
    name = 'nigerianpropertyrent'
    start_urls = ['https://nigeriapropertycentre.com/for-rent']
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'


    def parse(self,response):
        for product in response.css('div.row.property-list'):
            link = product.css('div.wp-block-content.clearfix.text-xs-left.text-sm-left a::attr(href)')
            dt =  {
                'title' : product.css('div.wp-block-title.hidden-xs h3::text').getall(),
                'front_image' : product.css('img.sm-width-min-200-max-250.xs-width-min-200-max-350::attr(src)').get(),
                'details_link' : product.css('div.wp-block-content.clearfix.text-xs-left.text-sm-left a::attr(href)').get(),
                'content_title' : product.css('div.wp-block-content.clearfix.text-xs-left.text-sm-left h4.content-title::text').get(),
                'address' :  product.css('address.voffset-bottom-10 strong::text').get(),
                'description' :  product.css('div.description.hidden-xs p::text').getall(),
                'added_on' :  product.css('span.added-on::text').get(),
                'price' :  product.css('span.price::text').getall(),
                'agent' : product.css('span.marketed-by.pull-right.hidden-xs.hidden-sm.text-right::text').get(),
                'agent_no' : product.css('span.marketed-by.pull-right.hidden-xs.hidden-sm.text-right strong::text').getall(),
                'features' : product.css('ul.aux-info li span::text').getall()
            }
            yield response.follow(link.get(),callback=self.parse_details,meta=dt)
            
        next_page = f"https://nigeriapropertycentre.com/for-rent{response.css('ul.pagination li a::attr(href)').getall()[-1]}"

        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)

    def parse_details(self,response):
        yield {
            'main_details' : response.meta,
            'agent_name' : response.css('div.col-md-4 div.panel-body p a strong::text').getall(),
            'agent_dets' : response.css('div.col-md-4 div.panel-body p::text').getall(),
            'agent_website' : response.css('div.col-md-4 div.panel-body p a::attr(href)').getall(),
            'images' : response.css('div.col-sm-12.images-inner-container li img::attr(src)').getall(),
            'description' : response.css('div.tab-body p::text').getall(),
            'table' : response.css('table.table.table-bordered.table-striped td').getall()
        }
