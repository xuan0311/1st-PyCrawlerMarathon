#載入套件
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    target_urls = [
        'https://www.ptt.cc/bbs/Gossiping/M.1559788476.A.074.html',
        'https://www.ptt.cc/bbs/Gossiping/M.1557928779.A.0C1.html'
    ]
    #呼叫 CrawlerProcess 就會建立爬蟲流程
    process = CrawlerProcess(get_project_settings()) 
    #每個爬蟲都有一個全局唯一的名稱，可以直接透過這個名稱來決定要開始執行哪個爬蟲
    process.crawl('PTTCrawler', start_urls=target_urls, filename='test.json')#filename='test.json':給予自定義的其他參數
    process.start()

if __name__ == '__main__':
    main()
