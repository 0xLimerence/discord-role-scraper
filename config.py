#!/usr/bin/env python3

VERSION_NUMBER = '1.3'

SCRAPE_GUILD_INFO = True

GUILD_INFO_TO_SCRAPE = [
    'id', 
    'name', 
    'description', 
    'owner_id', 
    'region', 
    'mfa_level', 
    'vanity_url_code', 
    'premium_tier', 
    'premium_subscription_count', 
    'nsfw',
]

# Make sure to keep the formatting
# DO NOT change any of the values
PERMISSIONS_TO_CHECK = {
    'Name': True,
    'Position': True,
    'ID': True,
    'Mentionable': True,
    'Administrator': 0x0000000000000008,
    'Mention All': 0x0000000000020000,
    'Manage Guild': 0x0000000000000020,
    'Manage Roles': 0x0000000010000000,
    'Manage Channels': 0x0000000000000010,
    # 'Manage Events': 0x0000000200000000,
    # 'Manage Nicknames': 0x0000000008000000,
    # 'Kick Members': 0x0000000000000002,
    # 'Ban Members': 0x0000000000000004,
    'Webhooks': 0x0000000020000000,
    # 'App Commands': 0x0000000080000000,
    'Tags': True,
}