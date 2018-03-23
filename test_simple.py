import requests

'''
测试接口：获取图书信息	GET	/v2/book/:id
测试URL：https://api.douban.com/v2/book/:id
测试数据: 2230208
预期结果：
{"rating":{"max":10,"numRaters":22156,"average":"7.9","min":0},"subtitle":"","author":["亦舒"],"pubdate":"2007-8","tags":[{"count":9937,"name":"亦舒","title":"亦舒"},{"count":5652,"name":"我的前半生","title":"我的前半生"},{"count":4044,"name":"小说","title":"小说"},{"count":2802,"name":"女性","title":"女性"},{"count":2089,"name":"爱情","title":"爱情"},{"count":1305,"name":"香港","title":"香港"},{"count":1144,"name":"言情","title":"言情"},{"count":798,"name":"中国文学","title":"中国文学"}],"origin_title":"","image":"https://img1.doubanio.com\/mpic\/s2720819.jpg","binding":"平装","translator":[],"catalog":"","pages":"271","images":{"small":"https://img1.doubanio.com\/spic\/s2720819.jpg","large":"https://img1.doubanio.com\/lpic\/s2720819.jpg","medium":"https://img1.doubanio.com\/mpic\/s2720819.jpg"},"alt":"https:\/\/book.douban.com\/subject\/2230208\/","id":"2230208","publisher":"新世界出版社","isbn10":"7802283930","isbn13":"9787802283930","title":"我的前半生","url":"https:\/\/api.douban.com\/v2\/book\/2230208","alt_title":"","author_intro":"亦舒，言情文学作家。原名倪亦舒，兄长是香港作家倪匡。亦舒1946年生于上海，祖籍浙江镇海，五岁时定居香港。中学毕业后，曾在《明报》任职记者，及担任电影杂志采访和编辑等。1973年，亦舒赴英国修读酒店食物管理课程，三年后回港，任职富丽华酒店公关部，后进入政府新闻处担任新闻官，也曾当过电视台编剧。现为专业作家，并已移居加拿大。","summary":"一个三十几岁的美丽女人子君，在家做全职家庭主妇。却被一个平凡女人夺走丈夫，一段婚姻的失败，让女主角不得不坚强，变得更美丽，有了事业，最终遇见一个更值得爱的男人……","series":{"id":"5782","title":"亦舒新经典"},"price":"22.00元"}
'''
def test_get_book_id():
    id = '2230208'
    response = requests.get("https://api.douban.com/v2/book/" + id, verify=True)
    print(response.url)
    assert response.status_code == 200
    