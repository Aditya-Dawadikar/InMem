import json
import hashlib
from datetime import timedelta
from services.Time import get_timestamp
from services.StringManipulation import generate_unique_string,getHash, sign_string
from config import SERVER_SECRET

class ServiceAccount:
    def __init__(self, db_name: str, validity_days: int=30):
        self.db_name = db_name
        self.created_at = get_timestamp()
        self.validity_days = validity_days
        print(type(self.created_at))
        self.expiration_date = self.created_at + self.validity_days*86400
    
    def generateCredentials(self):
        sa_timestamp = int(self.created_at)
        server_sa_account_file_name = f"{self.db_name}-{sa_timestamp}"

        account_facts = {
            "database_name": self.db_name,
            "sa_created_at": self.created_at,
            "sa_expires_on": self.expiration_date
        }

        unique_string = generate_unique_string(10)
        signed_unique_string = sign_string(SERVER_SECRET, unique_string)

        sa_key = getHash(account_facts,signed_unique_string)

        client_account_json = {
            **account_facts,
            "sa_key": sa_key,
        }
        server_account_json = {
            **client_account_json,
            "unique_string": unique_string,
            "signed_unique_string": signed_unique_string
        }

        print(client_account_json)
        print(server_account_json)

        # Save Server account json
        server_sa_json = json.dumps(server_account_json)
        with open(f"auth/service_accounts/{server_sa_account_file_name}.json", "w") as sa_file:
            sa_file.write(server_sa_json)
        
        # Return Client account json
        client_sa_json = json.dumps(client_account_json)
        return client_sa_json
    
    def is_valid(self):
        current_time = get_timestamp()
        return current_time <= self.expiration_date

    
    
        