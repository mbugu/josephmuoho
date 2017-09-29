import re
import urllib 
from HTMLParser import HTMLParser  
from urlparse import urlparse
import scrapy


def HREFParser(HTMLParser):  
    """
    Parser that extracts hrefs
    """
    hrefs = set()
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            dict_attrs = dict(attrs)
            if dict_attrs.get('href'):
                self.hrefs.add(dict_attrs['href'])

def get_links(html):
 url_regex=re.compile("http://www.strathmore.edu/")
 return page_regex.findall(html)

def crawl(seed_page, max_depth=3):
    tocrawl = [seed_url]
    crawled = []
    index = {}
    next_depth = []
    depth = 0
    while to_crawl and depth <= max_depth:
          current_crawl = tocrawl.pop()
          if current_crawl not in crawled:
             content = get_html(current_crawl)
             links, index = get_all_links(content, current_crawl)
             union(next_depth, links)
             crawled.append(current_crawl)
          if not to_crawl:
             tocrawl, next_depth = next_depth, []
             depth = depth + 1
    return url
