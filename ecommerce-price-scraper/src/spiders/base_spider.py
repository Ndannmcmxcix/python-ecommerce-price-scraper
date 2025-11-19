thonpython
import logging
from abc import ABC, abstractmethod

class BaseSpider(ABC):
 def __init__(self):
 self.logger = logging.getLogger(self.__class__.__name__)

 @abstractmethod
 def scrape(self, url: str) -> dict:
 pass