thonpython
import re

class PriceCleaner:
 def clean(self, price_str: str):
 if not price_str:
 return None, None

 currency_match = re.findall(r"[€$£]|USD|EUR|GBP", price_str)
 currency = currency_match[0] if currency_match else None

 numeric = re.findall(r"[\d\.,]+", price_str)
 value = numeric[0].replace(",", "") if numeric else None

 try:
 value = float(value)
 except:
 value = None

 return value, currency