import scrapy
from scrapy.crawler import CrawlerProcess


class AgodaSpider(scrapy.Spider):
    name = 'agoda'
    start_urls = [
        'https://www.agoda.com/NewSite/th-th/Review/HotelReviews'
    ]

    def start_requests(self):
        headers = {
            'origin': 'https://www.agoda.com',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
            'content-type': 'application/json; charset=UTF-8',
            'accept': 'application/json',
            'referer': 'www.agoda.com',
            'authority': 'www.agoda.com',
            'x-requested-with': 'XMLHttpRequest',
            'dnt': '1',
        }

        data = {
            'hotelId': '1280163',
            'demographicId': '0',
            'page': '1',
            'pageSize': '20',
            'sorting': '1',
            'isReviewPage': 'false',
            'isCrawlablePage': 'true',
            'filters': {'language': [], 'room': []},
            'searchKeyword': '',
        }
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            body=str(data),
            headers=headers,
            method='POST',
        )

    def parse(self, response):
        print('----[ PARSE ]----', response.body)


process = CrawlerProcess()

process.crawl(AgodaSpider)
process.start(stop_after_crawl=True)  # the script will block here until the crawling is finished

# curl --data - binary '{"hotelId":1280163,"hotelProviderId":332,"demographicId":0,"pageNo":1,"pageSize":20,"sorting":1,"reviewProviderIds":[332,3038,27901,28999],"isReviewPage":false,"isCrawlablePage":true,"paginationSize":5}'

a = {'RecommendedPropertyHeader': {'Header': 'เปรียบเทียบกับที่พักแนะนำที่คล้ายกัน', 'RoomRate': 'ราคาเริ่มต้นต่อคืน',
                                   'GuessRating': 'คะแนนจากผู้เข้าพัก', 'Neighborhood': 'ย่าน',
                                   'Breakfast': 'อาหารเช้า', 'WiFi': 'Wi-Fi', 'OtherSuppliers': None},
     'RecommendedProperties': [{'PropertyId': 96329, 'IsFavorite': False, 'HotelName': 'โรงแรมโรมเพลส',
                                'ImageUrl': '//pix6.agoda.net/hotelImages/963/96329/96329_14062610360020042777.jpg?s=208x117&ar=16x9',
                                'StarRating': 'star-3', 'ReviewCount': 338, 'ReviewScoreText': 'ดี', 'ReviewScore': 6.8,
                                'Price': 362.5, 'Currency': '฿',
                                'HotelUrl': '/th-th/rome-place-hotel/hotel/phuket-th.html?preq=1cf1f7ea-6005-4cf6-9700-e148ee0071ae&ri=1',
                                'ReviewRating': {'Score': 6.8, 'ScoreText': 'ดี', 'Scale': 0.0, 'FormattedScore': '6.8',
                                                 'FormattedScale': '0.0', 'Percentage': 0.0, 'RecommendationScore': 0},
                                'StarRatingInfo': {'FontIcon': 'ficon-star-3',
                                                   'Tooltip': 'ที่พักเป็นผู้กำหนดระดับดาวเพื่อเป็นแนวทางให้ผู้เข้าพักทราบถึงความสะดวกสบายและสิ่งอำนวยความสะดวกที่คาดว่าน่าจะได้รับ ณ ที่พัก',
                                                   'Color': 'orange-yellow', 'Value': 3.0},
                                'ReviewCountText': '(338 รีวิว)', 'CrossedOutRate': 550.0,
                                'Neighborhood': 'ภูเก็ตทาว์น',
                                'Benefit': {'Title': 'บริการอาหารเช้า', 'Symbol': 'ficon-breakfast', 'Available': True},
                                'HighlightFacility': {'Title': 'ฟรี WiFi', 'Symbol': 'ficon-wifi', 'Available': True},
                                'Channel': None, 'IsCurrentProperty': False, 'CheapestRoomUid': None,
                                'ReviewLocationScore': 7.0, 'ValueForMoneyScore': 7.4, 'TotalDiscountPercent': 0,
                                'ReviewFormattedLocationScore': '7.0', 'ReviewLocationText': 'ทำเลที่ตั้ง',
                                'Culture': 'th-th', 'SupplierName': None, 'SupplierList': None, 'Latitude': 0.0,
                                'Longitude': 0.0},
                               {'PropertyId': 159084, 'IsFavorite': False, 'HotelName': 'ภูเก็ต เซ็นเตอร์ อพาร์ทเมนท์',
                                'ImageUrl': '//pix6.agoda.net/hotelImages/159/159084/159084_14080715090020893393.jpg?s=208x117&ar=16x9',
                                'StarRating': 'star-3', 'ReviewCount': 751, 'ReviewScoreText': 'ดีมาก',
                                'ReviewScore': 7.8, 'Price': 552.1, 'Currency': '฿',
                                'HotelUrl': '/th-th/phuket-center-apartment/hotel/phuket-th.html?preq=1cf1f7ea-6005-4cf6-9700-e148ee0071ae&ri=2',
                                'ReviewRating': {'Score': 7.8, 'ScoreText': 'ดีมาก', 'Scale': 0.0,
                                                 'FormattedScore': '7.8', 'FormattedScale': '0.0', 'Percentage': 0.0,
                                                 'RecommendationScore': 0},
                                'StarRatingInfo': {'FontIcon': 'ficon-star-3',
                                                   'Tooltip': 'ระดับดาวของที่พักประเภทนี้พิจารณาจากสิ่งอำนวยความสะดวก คะแนนจากผู้เข้าพัก ขนาดห้องพัก และปัจจัยอื่นๆ',
                                                   'Color': 'pink', 'Value': 3.0}, 'ReviewCountText': '(751 รีวิว)',
                                'CrossedOutRate': 0.0, 'Neighborhood': 'ภูเก็ตทาว์น',
                                'Benefit': {'Title': 'บริการอาหารเช้า', 'Symbol': 'ficon-breakfast',
                                            'Available': False},
                                'HighlightFacility': {'Title': 'ฟรี WiFi', 'Symbol': 'ficon-wifi', 'Available': True},
                                'Channel': {'Description': 'ราคาสำหรับคนในประเทศ', 'Symbol': 'ficon-domestic-rates'},
                                'IsCurrentProperty': False, 'CheapestRoomUid': None, 'ReviewLocationScore': 8.4,
                                'ValueForMoneyScore': 8.2, 'TotalDiscountPercent': 0,
                                'ReviewFormattedLocationScore': '8.4', 'ReviewLocationText': 'ทำเลที่ตั้ง',
                                'Culture': 'th-th', 'SupplierName': None, 'SupplierList': None, 'Latitude': 0.0,
                                'Longitude': 0.0},
                               {'PropertyId': 569304, 'IsFavorite': False, 'HotelName': 'สลีป แอท ภูเก็ต',
                                'ImageUrl': '//pix6.agoda.net/hotelImages/569/569304/569304_16083009100045905215.jpg?s=208x117&ar=16x9',
                                'StarRating': 'star-25', 'ReviewCount': 196, 'ReviewScoreText': 'ดีมาก',
                                'ReviewScore': 7.9, 'Price': 378.79, 'Currency': '฿',
                                'HotelUrl': '/th-th/sleep-at-phuket/hotel/phuket-th.html?preq=1cf1f7ea-6005-4cf6-9700-e148ee0071ae&ri=3',
                                'ReviewRating': {'Score': 7.9, 'ScoreText': 'ดีมาก', 'Scale': 0.0,
                                                 'FormattedScore': '7.9', 'FormattedScale': '0.0', 'Percentage': 0.0,
                                                 'RecommendationScore': 0},
                                'StarRatingInfo': {'FontIcon': 'ficon-star-25',
                                                   'Tooltip': 'ที่พักเป็นผู้กำหนดระดับดาวเพื่อเป็นแนวทางให้ผู้เข้าพักทราบถึงความสะดวกสบายและสิ่งอำนวยความสะดวกที่คาดว่าน่าจะได้รับ ณ ที่พัก',
                                                   'Color': 'orange-yellow', 'Value': 2.5},
                                'ReviewCountText': '(196 รีวิว)', 'CrossedOutRate': 600.0,
                                'Neighborhood': 'ภูเก็ตทาว์น',
                                'Benefit': {'Title': 'บริการอาหารเช้า', 'Symbol': 'ficon-breakfast',
                                            'Available': False},
                                'HighlightFacility': {'Title': 'ฟรี WiFi', 'Symbol': 'ficon-wifi', 'Available': True},
                                'Channel': {'Description': 'ราคาสำหรับคนในประเทศ', 'Symbol': 'ficon-domestic-rates'},
                                'IsCurrentProperty': False, 'CheapestRoomUid': None, 'ReviewLocationScore': 8.3,
                                'ValueForMoneyScore': 8.4, 'TotalDiscountPercent': 0,
                                'ReviewFormattedLocationScore': '8.3', 'ReviewLocationText': 'ทำเลที่ตั้ง',
                                'Culture': 'th-th', 'SupplierName': None, 'SupplierList': None, 'Latitude': 0.0,
                                'Longitude': 0.0},
                               {'PropertyId': 626362, 'IsFavorite': False, 'HotelName': 'บีทู ภูเก็ต โฮเต็ล',
                                'ImageUrl': '//pix6.agoda.net/hotelImages/626/626362/626362_16082214490045682715.jpg?s=208x117&ar=16x9',
                                'StarRating': 'star-3', 'ReviewCount': 874, 'ReviewScoreText': 'ดีมาก',
                                'ReviewScore': 7.6, 'Price': 496.63, 'Currency': '฿',
                                'HotelUrl': '/th-th/b2-phuket-hotel/hotel/phuket-th.html?preq=1cf1f7ea-6005-4cf6-9700-e148ee0071ae&ri=4',
                                'ReviewRating': {'Score': 7.6, 'ScoreText': 'ดีมาก', 'Scale': 0.0,
                                                 'FormattedScore': '7.6', 'FormattedScale': '0.0', 'Percentage': 0.0,
                                                 'RecommendationScore': 0},
                                'StarRatingInfo': {'FontIcon': 'ficon-star-3',
                                                   'Tooltip': 'ที่พักเป็นผู้กำหนดระดับดาวเพื่อเป็นแนวทางให้ผู้เข้าพักทราบถึงความสะดวกสบายและสิ่งอำนวยความสะดวกที่คาดว่าน่าจะได้รับ ณ ที่พัก',
                                                   'Color': 'orange-yellow', 'Value': 3.0},
                                'ReviewCountText': '(874 รีวิว)', 'CrossedOutRate': 1500.0,
                                'Neighborhood': 'ภูเก็ตทาว์น',
                                'Benefit': {'Title': 'บริการอาหารเช้า', 'Symbol': 'ficon-breakfast',
                                            'Available': False},
                                'HighlightFacility': {'Title': 'ฟรี WiFi', 'Symbol': 'ficon-wifi', 'Available': True},
                                'Channel': None, 'IsCurrentProperty': False, 'CheapestRoomUid': None,
                                'ReviewLocationScore': 7.8, 'ValueForMoneyScore': 8.4, 'TotalDiscountPercent': 0,
                                'ReviewFormattedLocationScore': '7.8', 'ReviewLocationText': 'ทำเลที่ตั้ง',
                                'Culture': 'th-th', 'SupplierName': None, 'SupplierList': None, 'Latitude': 0.0,
                                'Longitude': 0.0},
                               {'PropertyId': 285389, 'IsFavorite': False, 'HotelName': 'โรงแรมซิโนอินน์',
                                'ImageUrl': '//pix6.agoda.net/hotelImages/285/285389/285389_15012117060024742046.jpg?s=208x117&ar=16x9',
                                'StarRating': 'star-3', 'ReviewCount': 791, 'ReviewScoreText': 'ดีเยี่ยม',
                                'ReviewScore': 8.1, 'Price': 595.68, 'Currency': '฿',
                                'HotelUrl': '/th-th/sino-inn-hotel/hotel/phuket-th.html?preq=1cf1f7ea-6005-4cf6-9700-e148ee0071ae&ri=5',
                                'ReviewRating': {'Score': 8.1, 'ScoreText': 'ดีเยี่ยม', 'Scale': 0.0,
                                                 'FormattedScore': '8.1', 'FormattedScale': '0.0', 'Percentage': 0.0,
                                                 'RecommendationScore': 0},
                                'StarRatingInfo': {'FontIcon': 'ficon-star-3',
                                                   'Tooltip': 'ที่พักเป็นผู้กำหนดระดับดาวเพื่อเป็นแนวทางให้ผู้เข้าพักทราบถึงความสะดวกสบายและสิ่งอำนวยความสะดวกที่คาดว่าน่าจะได้รับ ณ ที่พัก',
                                                   'Color': 'orange-yellow', 'Value': 3.0},
                                'ReviewCountText': '(791 รีวิว)', 'CrossedOutRate': 2000.0,
                                'Neighborhood': 'ภูเก็ตทาว์น',
                                'Benefit': {'Title': 'บริการอาหารเช้า', 'Symbol': 'ficon-breakfast',
                                            'Available': False},
                                'HighlightFacility': {'Title': 'ฟรี WiFi', 'Symbol': 'ficon-wifi', 'Available': True},
                                'Channel': {'Description': 'ราคาสำหรับคนในประเทศ', 'Symbol': 'ficon-domestic-rates'},
                                'IsCurrentProperty': False, 'CheapestRoomUid': None, 'ReviewLocationScore': 7.9,
                                'ValueForMoneyScore': 8.6, 'TotalDiscountPercent': 0,
                                'ReviewFormattedLocationScore': '7.9', 'ReviewLocationText': 'ทำเลที่ตั้ง',
                                'Culture': 'th-th', 'SupplierName': None, 'SupplierList': None, 'Latitude': 0.0,
                                'Longitude': 0.0},
                               {'PropertyId': 1622405, 'IsFavorite': False, 'HotelName': 'ฮ็อป อินน์ ภูเก็ต',
                                'ImageUrl': '//pix6.agoda.net/hotelImages/162/1622405/1622405_17032716530051915827.jpg?s=208x117&ar=16x9',
                                'StarRating': 'star-2', 'ReviewCount': 428, 'ReviewScoreText': 'ดีเยี่ยม',
                                'ReviewScore': 8.3, 'Price': 476.21, 'Currency': '฿',
                                'HotelUrl': '/th-th/hop-inn-phuket/hotel/phuket-th.html?preq=1cf1f7ea-6005-4cf6-9700-e148ee0071ae&ri=6',
                                'ReviewRating': {'Score': 8.3, 'ScoreText': 'ดีเยี่ยม', 'Scale': 0.0,
                                                 'FormattedScore': '8.3', 'FormattedScale': '0.0', 'Percentage': 0.0,
                                                 'RecommendationScore': 0},
                                'StarRatingInfo': {'FontIcon': 'ficon-star-2',
                                                   'Tooltip': 'ที่พักเป็นผู้กำหนดระดับดาวเพื่อเป็นแนวทางให้ผู้เข้าพักทราบถึงความสะดวกสบายและสิ่งอำนวยความสะดวกที่คาดว่าน่าจะได้รับ ณ ที่พัก',
                                                   'Color': 'orange-yellow', 'Value': 2.0},
                                'ReviewCountText': '(428 รีวิว)', 'CrossedOutRate': 1300.0,
                                'Neighborhood': 'ภูเก็ตทาว์น',
                                'Benefit': {'Title': 'บริการอาหารเช้า', 'Symbol': 'ficon-breakfast',
                                            'Available': False},
                                'HighlightFacility': {'Title': 'ฟรี WiFi', 'Symbol': 'ficon-wifi', 'Available': True},
                                'Channel': None, 'IsCurrentProperty': False, 'CheapestRoomUid': None,
                                'ReviewLocationScore': 8.3, 'ValueForMoneyScore': 8.9, 'TotalDiscountPercent': 0,
                                'ReviewFormattedLocationScore': '8.3', 'ReviewLocationText': 'ทำเลที่ตั้ง',
                                'Culture': 'th-th', 'SupplierName': None, 'SupplierList': None, 'Latitude': 0.0,
                                'Longitude': 0.0}], 'CurrentProperty': None, 'HasOnlyCurrentProperty': False,
     'MissingImageURL': 'https://cdn6.agoda.net/images/MIN-8037/default/agoda-default-images-l@2x.png',
     'HasSearchCriteria': True}
