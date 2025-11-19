thonpython
import json
import logging

class Exporter:
 def __init__(self):
 self.logger = logging.getLogger("Exporter")

 def to_json(self, data, filepath):
 try:
 with open(filepath, "w", encoding="utf-8") as f:
 json.dump(data, f, indent=4)
 except Exception as e:
 self.logger.error(f"Failed to write JSON: {e}")