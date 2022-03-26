from Crawler.CrawlURL import crawlURLBaseOnTopBranch
from Crawler.crawlContent import crawlContent
if __name__ == "__main__":
    links = crawlURLBaseOnTopBranch()
    contents = crawlContent(links)