thonpython
import requests
from bs4 import BeautifulSoup
from .base_spider import BaseSpider
from extractors.bs4_parser import BS4Parser
from extractors.price_cleaner import PriceCleaner

class EcommerceSpider(BaseSpider):
 def scrape(self, url: str) -> dict:
 self.logger.info(f"Fetching: {url}")
 response = requests.get(url, timeout=10)
 response.raise_for_status()

 soup = BeautifulSoup(response.text, "html.parser")

 parser = BS4Parser()
 cleaner = PriceCleaner()

 product_name = parser.extract_text(soup, ["h1", ".product-title"])
 price_raw = parser.extract_text(soup, [".price", ".product-price"])
 price, currency = cleaner.clean(price_raw)

 return {
 "product_name": product_name,
 "price": price,
 "currency": currency,
 "product_url": url,
 "availability": parser.extract_text(soup, [".availability", "#stock"]),
 "sku": parser.extract_text(soup, [".sku", "#sku"]),
 "category": parser.extract_text(soup, [".breadcrumb", ".category-path"])
 }