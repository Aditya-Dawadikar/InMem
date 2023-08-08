def kill_cache_threads(DB_REFERENCES):
    for db_ref,db  in DB_REFERENCES.items():
        # print(db)
        # print(type(db))
        cache = db["cache"]
        cache.stop_expiration_scheduler()