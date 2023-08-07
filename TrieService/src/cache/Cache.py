from collections import OrderedDict
from threading import Lock
import threading
import schedule
import time
from datetime import datetime, timezone
from services.Time import get_timestamp

class Cache:
    def __init__(self,
                 max_items:int=10,
                 expiration:int=10):
        """
            max_items `int`:
                maximum number of items that can exist in the cache
            
            expiration `int`:
                integer defining the number of seconds for which the
                item should remain in the cache
        """
        self.max_items = max_items
        self.expiration = expiration
        self.items = OrderedDict()
        self.lock = Lock()
        
        self.start_expiration_scheduler()

    def set_cache_item(self, key:str, value):
        with self.lock:
            if len(self.items) >= self.max_items-1:
                # If Cache is Full, then remove least recently used item
                self.remove_least_recently_used()

            if self.items.get(key) is None:
                # Item does not exist
                # Add new Item
                print(f"""Setting Cache for key "{key}" """)
                self.items[key] = {
                       "cached_at": get_timestamp(),
                        "data": value,
                        "query_frequency": 1
                }
            else:
                # Item already exists
                # Increment query_frequency
                self.increment_query_frequency(key)

    def increment_query_frequency(self,key:str):
        if self.items.get(key) is not None:
            print(f"""Query Frequency incremented for key "{key}" """)
            self.items[key]["query_frequency"] = 1+self.items[key]["query_frequency"]

    def get_cache_item(self, key:str):
        if self.items.get(key) is not None:
            print(f"""Cache HIT for key "{key}" """)
            return self.items.get(key).get("data")
        
        
        print(f"""Cache MISS for key "{key}" """)
        return None

    def update_cache_item(self, key:str, value):
        with self.lock:
            if self.items.get(key) is not None:
                self.items[key]["data"] = value
                return True
            return False

    def delete_cache_item(self, key: str):
        with self.lock:
            if self.items.get(key) is not None:
                print(f"""Deleted Cache item for key "{key}" """)
                self.items.pop(key)
                return True
            return False

    def clear_cache(self):
        with self.lock:
            self.items = OrderedDict()
            return True

    def cache_metrics(self):
        return {
            "hit_rate": None,
            "miss_rate": None,
            "cached_items_count": None
        }

    def remove_least_recently_used(self):
        with self.lock:
            lru_item = min(self.items.values(), key=lambda x: (x["query_frequency"], x["cached_at"]))
            del self.items[lru_item]

    def start_expiration_scheduler(self):
        schedule.every(self.expiration).seconds.do(self.expire_cache_items)
    
    # TODO: This has to be implemented correctly
    def expire_cache_items(self):
        with self.lock:
            # current_time = time.time()
            # expired_keys = []
            
            # for key, item in self.items.items():
            #     cached_time = datetime.fromtimestamp(item["cached_at"], tz=timezone.utc)
            #     if (current_time - cached_time).total_seconds() > self.expiration:
            #         expired_keys.append(key)
            
            # for key in expired_keys:
            #     print(f"""Expiring cache item for "{key}" """)
            #     self.items.pop(key)
            pass
