from collections import OrderedDict
from threading import Lock, Thread
import threading
import schedule
import time
from datetime import datetime, timezone
from services.Time import get_timestamp

class Cache:
    def __init__(self,
                 db_name: str,
                 max_items:int=10,
                 expiration:int=10,
                 increased_expiration:int=3):
        """
            max_items `int`:
                maximum number of items that can exist in the cache
            
            expiration `int`:
                integer defining the number of seconds for which the
                item should remain in the cache
        """
        self.db_name = db_name
        self.max_items = max_items
        self.expiration = expiration
        
        # Ensure that items are retrieved in same order of insertion
        self.items = OrderedDict()
        
        # Ensure that cache write operations are thread safe
        self.lock = Lock()
        
        # Threshold for query_frequency to be considered high frequency query
        self.query_frequency_threshold = 5

        # High Frequency items must have higher expiration threshold
        self.increased_expiration_threshold = self.expiration*increased_expiration
        
        # Stopping event for Thread
        self.stop_event = threading.Event()
        
        # self.start_expiration_scheduler()
        self.scheduled_cache_eviction_thread = Thread(target=self.start_expiration_scheduler)
        self.scheduled_cache_eviction_thread.start()


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
        """
            Whenever a key from the cache is queried,
            its frequency is increased
        """
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
        """
            LRU Logic
            Pass 1: filter items that have low query_frequency
            Pass 2: filter items that are the oldest
        """
        with self.lock:
            lru_item = min(self.items.values(), key=lambda x: (x["query_frequency"], x["cached_at"]))
            del self.items[lru_item]

    def start_expiration_scheduler(self):
        """
            This function will initiate a scheduled cache
            expiration mechanism
        """
        schedule.every(self.expiration).seconds.do(self.expire_cache_items)
        
        while not self.stop_event.is_set():
            schedule.run_pending()
            time.sleep(self.expiration)
    
    def expire_cache_items(self):
        """
            This function will be called periodically to remove items
            from the cache that have surpassed their expiration time
        """
        with self.lock:
            current_time = time.time()
            expired_keys = []
            
            for key, item in self.items.items():
                cached_time = datetime.fromtimestamp(item["cached_at"], tz=timezone.utc)
                query_frequency = item["query_frequency"]

                if query_frequency > self.query_frequency_threshold:
                    # Use higher expiration time for high frequency queries
                    new_expiration = self.increased_expiration_threshold
                    if (current_time - cached_time.timestamp()) > new_expiration:
                        expired_keys.append(key)

                elif (current_time - cached_time.timestamp()) > self.expiration:
                    # Use standard expiration time for low frequency queries
                    expired_keys.append(key)
            
            for key in expired_keys:
                print(f"""Expiring cache item for "{key}" """)
                self.items.pop(key)
            
            # self.describe_cache()

    def stop_expiration_scheduler(self):
        """
            This function is used to kill the thread responsible
            for scheduled cache eviction
        """
        if hasattr(self, 'scheduled_cache_eviction_thread') and \
            self.scheduled_cache_eviction_thread.is_alive():
                # Kill the background task
                self.stop_event.set()
                self.scheduled_cache_eviction_thread.join()

    def describe_cache(self):
        print("-------------------------------")
        timestamp = time.time()
        print(f"""{self.db_name} CACHE contents at {timestamp}""")
        print("-------------------------------")
        for key,item in self.items.items():
                print(key, item)
