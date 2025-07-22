import time
from zoho_api import ZohoMailAPI
from namecheap_api import NamecheapAPI
from utils import load_config


def setup_email_for_domain(domain_config, zoho_api, namecheap_api):
    domain = domain_config['domain']
    users = domain_config.get('users', [])

    print(f"[INFO] Starting setup for domain: {domain}")

    # Step 1: Add domain to Zoho
    domain_id = zoho_api.add_domain(domain)
    print(f"[INFO] Domain added to Zoho: {domain_id}")

    # Step 2: Fetch DNS records from Zoho
    dns_records = zoho_api.get_dns_records(domain)
    print(f"[INFO] Retrieved DNS records from Zoho")

    # Step 3: Update Namecheap DNS
    namecheap_api.update_dns_records(domain, dns_records)
    print(f"[INFO] DNS records pushed to Namecheap")

    # Step 4: Trigger verification in Zoho
    zoho_api.verify_domain(domain)
    print(f"[INFO] Domain verification triggered")

    # Step 5: Create mailboxes
    for user in users:
        zoho_api.create_mailbox(domain, user['name'], user['email'])
        print(f"[INFO] Created mailbox: {user['email']}")

    print(f"[SUCCESS] Setup complete for domain: {domain}\n")


if __name__ == "__main__":
    config = load_config("config.json")

    zoho_api = ZohoMailAPI(config['zoho'])
    namecheap_api = NamecheapAPI(config['namecheap'])

    for domain_cfg in config['domains']:
        try:
            setup_email_for_domain(domain_cfg, zoho_api, namecheap_api)
            time.sleep(2)  # Throttle requests
        except Exception as e:
            print(f"[ERROR] Failed for domain {domain_cfg['domain']}: {str(e)}")
