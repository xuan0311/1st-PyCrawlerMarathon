#載入套件
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    target_board = ['Gossiping', 'Stock']
    #呼叫 CrawlerProcess 就會建立爬蟲流程
    process = CrawlerProcess(get_project_settings()) 
    for board in target_board:
        process.crawl('PTTCrawler', board=board)
    
    # process.start() 要放在 for 迴圈的外面
    process.start()# start() 只可以被呼叫一次，這裡只會產生一個.json檔，包含兩個版的內容

if __name__ == '__main__':
    main()
