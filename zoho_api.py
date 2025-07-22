import requests

class ZohoMailAPI:
    def __init__(self, config):
        self.auth_token = config['auth_token']
        self.org_id = config['org_id']
        self.base_url = "https://api.zoho.com/mail"

    def add_domain(self, domain):
        # Stubbed
        return "domain_id_" + domain

    def get_dns_records(self, domain):
        # Stubbed
        return [
            {"type": "MX", "host": "@", "value": "mx.zoho.com", "priority": 10},
            {"type": "TXT", "host": "@", "value": "v=spf1 include:zoho.com ~all"},
        ]

    def verify_domain(self, domain):
        # Stubbed
        return True

    def create_mailbox(self, domain, name, email):
        # Stubbed
        return True
