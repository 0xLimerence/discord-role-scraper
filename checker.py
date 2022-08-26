#!/usr/bin/env python3

import requests, os, json, base64, re, sys
from random import choice
from colorama import Fore
from tabulate import tabulate

def fetch_info():
    locales = ["af", "af-NA", "af-ZA", "agq", "agq-CM", "ak", "ak-GH", "am", "am-ET", "ar", "ar-001", "ar-AE", "ar-BH", "ar-DJ", "ar-DZ", "ar-EG", "ar-EH", "ar-ER", "ar-IL", "ar-IQ", "ar-JO", "ar-KM", "ar-KW", "ar-LB", "ar-LY", "ar-MA", "ar-MR", "ar-OM", "ar-PS", "ar-QA", "ar-SA", "ar-SD", "ar-SO", "ar-SS", "ar-SY", "ar-TD", "ar-TN", "ar-YE", "as", "as-IN", "asa", "asa-TZ", "ast", "ast-ES", "az", "az-Cyrl", "az-Cyrl-AZ", "az-Latn", "az-Latn-AZ", "bas", "bas-CM", "be", "be-BY", "bem", "bem-ZM", "bez", "bez-TZ", "bg", "bg-BG", "bm", "bm-ML", "bn", "bn-BD", "bn-IN", "bo", "bo-CN", "bo-IN", "br", "br-FR", "brx", "brx-IN", "bs", "bs-Cyrl", "bs-Cyrl-BA", "bs-Latn", "bs-Latn-BA", "ca", "ca-AD", "ca-ES", "ca-FR", "ca-IT", "ccp", "ccp-BD", "ccp-IN", "ce", "ce-RU", "cgg", "cgg-UG", "chr", "chr-US", "ckb", "ckb-IQ", "ckb-IR", "cs", "cs-CZ", "cy", "cy-GB", "da", "da-DK", "da-GL", "dav", "dav-KE", "de", "de-AT", "de-BE", "de-CH", "de-DE", "de-IT", "de-LI", "de-LU", "dje", "dje-NE", "dsb", "dsb-DE", "dua", "dua-CM", "dyo", "dyo-SN", "dz", "dz-BT", "ebu", "ebu-KE", "ee", "ee-GH", "ee-TG", "el", "el-CY", "el-GR", "en", "en-001", "en-150", "en-AG", "en-AI", "en-AS", "en-AT", "en-AU", "en-BB", "en-BE", "en-BI", "en-BM", "en-BS", "en-BW", "en-BZ", "en-CA", "en-CC", "en-CH", "en-CK", "en-CM", "en-CX", "en-CY", "en-DE", "en-DG", "en-DK", "en-DM", "en-ER", "en-FI", "en-FJ", "en-FK", "en-FM", "en-GB", "en-GD", "en-GG", "en-GH", "en-GI", "en-GM", "en-GU", "en-GY", "en-HK", "en-IE", "en-IL", "en-IM", "en-IN", "en-IO", "en-JE", "en-JM", "en-KE", "en-KI", "en-KN", "en-KY", "en-LC", "en-LR", "en-LS", "en-MG", "en-MH", "en-MO", "en-MP", "en-MS", "en-MT", "en-MU", "en-MW", "en-MY", "en-NA", "en-NF", "en-NG", "en-NL", "en-NR", "en-NU", "en-NZ", "en-PG", "en-PH", "en-PK", "en-PN", "en-PR", "en-PW", "en-RW", "en-SB", "en-SC", "en-SD", "en-SE", "en-SG", "en-SH", "en-SI", "en-SL", "en-SS", "en-SX", "en-SZ", "en-TC", "en-TK", "en-TO", "en-TT", "en-TV", "en-TZ", "en-UG", "en-UM", "en-US", "en-US-POSIX", "en-VC", "en-VG", "en-VI", "en-VU", "en-WS", "en-ZA", "en-ZM", "en-ZW", "eo", "es", "es-419", "es-AR", "es-BO", "es-BR", "es-BZ", "es-CL", "es-CO", "es-CR", "es-CU", "es-DO", "es-EA", "es-EC", "es-ES", "es-GQ", "es-GT", "es-HN", "es-IC", "es-MX", "es-NI", "es-PA", "es-PE", "es-PH", "es-PR", "es-PY", "es-SV", "es-US", "es-UY", "es-VE", "et", "et-EE", "eu", "eu-ES", "ewo", "ewo-CM", "fa", "fa-AF", "fa-IR", "ff", "ff-CM", "ff-GN", "ff-MR", "ff-SN", "fi", "fi-FI", "fil", "fil-PH", "fo", "fo-DK", "fo-FO", "fr", "fr-BE", "fr-BF", "fr-BI", "fr-BJ", "fr-BL", "fr-CA", "fr-CD", "fr-CF", "fr-CG", "fr-CH", "fr-CI", "fr-CM", "fr-DJ", "fr-DZ", "fr-FR", "fr-GA", "fr-GF", "fr-GN", "fr-GP", "fr-GQ", "fr-HT", "fr-KM", "fr-LU", "fr-MA", "fr-MC", "fr-MF", "fr-MG", "fr-ML", "fr-MQ", "fr-MR", "fr-MU", "fr-NC", "fr-NE", "fr-PF", "fr-PM", "fr-RE", "fr-RW", "fr-SC", "fr-SN", "fr-SY", "fr-TD", "fr-TG", "fr-TN", "fr-VU", "fr-WF", "fr-YT", "fur", "fur-IT", "fy", "fy-NL", "ga", "ga-IE", "gd", "gd-GB", "gl", "gl-ES", "gsw", "gsw-CH", "gsw-FR", "gsw-LI", "gu", "gu-IN", "guz", "guz-KE", "gv", "gv-IM", "ha", "ha-GH", "ha-NE", "ha-NG", "haw", "haw-US", "he", "he-IL", "hi", "hi-IN", "hr", "hr-BA", "hr-HR", "hsb", "hsb-DE", "hu", "hu-HU", "hy", "hy-AM", "id", "id-ID", "ig", "ig-NG", "ii", "ii-CN", "is", "is-IS", "it", "it-CH", "it-IT", "it-SM", "it-VA", "ja", "ja-JP", "jgo", "jgo-CM", "jmc", "jmc-TZ", "ka", "ka-GE", "kab", "kab-DZ", "kam", "kam-KE", "kde", "kde-TZ", "kea", "kea-CV", "khq", "khq-ML", "ki", "ki-KE", "kk", "kk-KZ", "kkj", "kkj-CM", "kl", "kl-GL", "kln", "kln-KE", "km", "km-KH", "kn", "kn-IN", "ko", "ko-KP", "ko-KR", "kok", "kok-IN", "ks", "ks-IN", "ksb", "ksb-TZ", "ksf", "ksf-CM", "ksh", "ksh-DE", "kw", "kw-GB", "ky", "ky-KG", "lag", "lag-TZ", "lb", "lb-LU", "lg", "lg-UG", "lkt", "lkt-US", "ln", "ln-AO", "ln-CD", "ln-CF", "ln-CG", "lo", "lo-LA", "lrc", "lrc-IQ", "lrc-IR", "lt", "lt-LT", "lu", "lu-CD", "luo", "luo-KE", "luy", "luy-KE", "lv", "lv-LV", "mas", "mas-KE", "mas-TZ", "mer", "mer-KE", "mfe", "mfe-MU", "mg", "mg-MG", "mgh", "mgh-MZ", "mgo", "mgo-CM", "mk", "mk-MK", "ml", "ml-IN", "mn", "mn-MN", "mr", "mr-IN", "ms", "ms-BN", "ms-MY", "ms-SG", "mt", "mt-MT", "mua", "mua-CM", "my", "my-MM", "mzn", "mzn-IR", "naq", "naq-NA", "nb", "nb-NO", "nb-SJ", "nd", "nd-ZW", "nds", "nds-DE", "nds-NL", "ne", "ne-IN", "ne-NP", "nl", "nl-AW", "nl-BE", "nl-BQ", "nl-CW", "nl-NL", "nl-SR", "nl-SX", "nmg", "nmg-CM", "nn", "nn-NO", "nnh", "nnh-CM", "nus", "nus-SS", "nyn", "nyn-UG", "om", "om-ET", "om-KE", "or", "or-IN", "os", "os-GE", "os-RU", "pa", "pa-Arab", "pa-Arab-PK", "pa-Guru", "pa-Guru-IN", "pl", "pl-PL", "ps", "ps-AF", "pt", "pt-AO", "pt-BR", "pt-CH", "pt-CV", "pt-GQ", "pt-GW", "pt-LU", "pt-MO", "pt-MZ", "pt-PT", "pt-ST", "pt-TL", "qu", "qu-BO", "qu-EC", "qu-PE", "rm", "rm-CH", "rn", "rn-BI", "ro", "ro-MD", "ro-RO", "rof", "rof-TZ", "ru", "ru-BY", "ru-KG", "ru-KZ", "ru-MD", "ru-RU", "ru-UA", "rw", "rw-RW", "rwk", "rwk-TZ", "sah", "sah-RU", "saq", "saq-KE", "sbp", "sbp-TZ", "se", "se-FI", "se-NO", "se-SE", "seh", "seh-MZ", "ses", "ses-ML", "sg", "sg-CF", "shi", "shi-Latn", "shi-Latn-MA", "shi-Tfng", "shi-Tfng-MA", "si", "si-LK", "sk", "sk-SK", "sl", "sl-SI", "smn", "smn-FI", "sn", "sn-ZW", "so", "so-DJ", "so-ET", "so-KE", "so-SO", "sq", "sq-AL", "sq-MK", "sq-XK", "sr", "sr-Cyrl", "sr-Cyrl-BA", "sr-Cyrl-ME", "sr-Cyrl-RS", "sr-Cyrl-XK", "sr-Latn", "sr-Latn-BA", "sr-Latn-ME", "sr-Latn-RS", "sr-Latn-XK", "sv", "sv-AX", "sv-FI", "sv-SE", "sw", "sw-CD", "sw-KE", "sw-TZ", "sw-UG", "ta", "ta-IN", "ta-LK", "ta-MY", "ta-SG", "te", "te-IN", "teo", "teo-KE", "teo-UG", "tg", "tg-TJ", "th", "th-TH", "ti", "ti-ER", "ti-ET", "to", "to-TO", "tr", "tr-CY", "tr-TR", "tt", "tt-RU", "twq", "twq-NE", "tzm", "tzm-MA", "ug", "ug-CN", "uk", "uk-UA", "ur", "ur-IN", "ur-PK", "uz", "uz-Arab", "uz-Arab-AF", "uz-Cyrl", "uz-Cyrl-UZ", "uz-Latn", "uz-Latn-UZ", "vai", "vai-Latn", "vai-Latn-LR", "vai-Vaii", "vai-Vaii-LR", "vi", "vi-VN", "vun", "vun-TZ", "wae", "wae-CH", "wo", "wo-SN", "xog", "xog-UG", "yav", "yav-CM", "yi", "yi-001", "yo", "yo-BJ", "yo-NG", "yue", "yue-Hans", "yue-Hans-CN", "yue-Hant", "yue-Hant-HK", "zgh", "zgh-MA", "zh", "zh-Hans", "zh-Hans-CN", "zh-Hans-HK", "zh-Hans-MO", "zh-Hans-SG", "zh-Hant", "zh-Hant-HK", "zh-Hant-MO", "zh-Hant-TW", "zu", "zu-ZA"]
    response = requests.get("https://discord-user-api.cf/api/v1/properties/web").json()
    xsuper = {"os":"Windows","browser":"Chrome","device":"","system_locale":f"{choice(locales)}","browser_user_agent":f"{response['chrome_user_agent']}","browser_version":f"{response['chrome_version']}","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":response['client_build_number'],"client_event_source":"null"}
    fixed = json.dumps(xsuper, separators=(',', ':')).encode("utf-8")
    encoded = base64.b64encode(fixed).decode("utf-8")
    return encoded

headers = {
	'accept': "*/*",
	'accept-language': 'en-US,en;q=0.9',
	'origin': 'https://discord.com',
	'referer': 'https://discord.com/channels/@me',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
	'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjkwNzA0NzgxNTA5MDQyNTkyNiIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5NjA3NTIyOTUxNzg1MzkwMzAiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
	'x-super-properties': fetch_info()
}

ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", flags=re.UNICODE)

def request_cookie():
	response1 = requests.get("https://discord.com")
	cookie = response1.cookies.get_dict()
	return cookie

def scrape_roles(token, server_id):
    try:
        headers["authorization"] = token
        cookie = request_cookie()
        response = requests.get(f"https://discord.com/api/v9/guilds/{server_id}/roles", headers=headers, cookies=cookie)
        roles = sorted(response.json(), key=lambda x: x['position'], reverse=True)

        print(response.json())

        data = []
        # Comment out what you dont want, except 'Tags'
        tab_headers = [
            'Pos', 
            'Role Name', 
            'Role ID',
            'Mentionable',
            'Administrator',
            # 'Manage Guild',
            'Manage Roles',
            'Manage Channels',
            # 'Manage Events',
            # 'Manage Nicknames',
            # 'Kick Members',
            # 'Ban Members',
            'Mention All',
            'Webhooks',
            'App Commands',
            'Tags', # Dont comment this one out, im not fixing that logical horror
        ]
        for role in roles:
            role_info = []
            role_info.append(role['position'] if 'Pos' in tab_headers else None)
            role_info.append(emoji_pattern.sub(r'', role['name']).encode('ascii', 'ignore').decode('utf-8') if 'Role Name' in tab_headers else None)
            role_info.append(role['id'] if 'Role ID' in tab_headers else None)
            role_info.append(f'{Fore.GREEN}Yes{Fore.RESET}' if role['mentionable'] == True and 'Mentionable' in tab_headers else f'{Fore.RED}No{Fore.RESET}' if 'Mentionable' in tab_headers else None) # Mentionable

            # https://discord.com/developers/docs/topics/permissions
            role_info.append(f'{Fore.GREEN}Yes{Fore.RESET}' if int(role['permissions']) & 0x0000000000000008 != 0 and 'Administrator'    in tab_headers else f'{Fore.RED}No{Fore.RESET}' if 'Administrator'    in tab_headers else None) # Admin
            role_info.append(f'{Fore.GREEN}Yes{Fore.RESET}' if int(role['permissions']) & 0x0000000000000020 != 0 and 'Manage Guild'     in tab_headers else f'{Fore.RED}No{Fore.RESET}' if 'Manage Guild'     in tab_headers else None) # Manage guild
            role_info.append(f'{Fore.GREEN}Yes{Fore.RESET}' if int(role['permissions']) & 0x0000000010000000 != 0 and 'Manage Roles'     in tab_headers else f'{Fore.RED}No{Fore.RESET}' if 'Manage Roles'     in tab_headers else None) # Manage roles
            role_info.append(f'{Fore.GREEN}Yes{Fore.RESET}' if int(role['permissions']) & 0x0000000000000010 != 0 and 'Manage Channels'  in tab_headers else f'{Fore.RED}No{Fore.RESET}' if 'Manage Channels'  in tab_headers else None) # Manage channels
            role_info.append(f'{Fore.GREEN}Yes{Fore.RESET}' if int(role['permissions']) & 0x0000000200000000 != 0 and 'Manage Events'    in tab_headers else f'{Fore.RED}No{Fore.RESET}' if 'Manage Events'    in tab_headers else None) # Manage events
            role_info.append(f'{Fore.GREEN}Yes{Fore.RESET}' if int(role['permissions']) & 0x0000000008000000 != 0 and 'Manage Nicknames' in tab_headers else f'{Fore.RED}No{Fore.RESET}' if 'Manage Nicknames' in tab_headers else None) # Manage nicknames
            role_info.append(f'{Fore.GREEN}Yes{Fore.RESET}' if int(role['permissions']) & 0x0000000000000002 != 0 and 'Kick Members'     in tab_headers else f'{Fore.RED}No{Fore.RESET}' if 'Kick Members'     in tab_headers else None) # Kick Members
            role_info.append(f'{Fore.GREEN}Yes{Fore.RESET}' if int(role['permissions']) & 0x0000000000000004 != 0 and 'Ban Members'      in tab_headers else f'{Fore.RED}No{Fore.RESET}' if 'Ban Members'      in tab_headers else None) # Ban Members
            role_info.append(f'{Fore.GREEN}Yes{Fore.RESET}' if int(role['permissions']) & 0x0000000000020000 != 0 and 'Mention All'      in tab_headers else f'{Fore.RED}No{Fore.RESET}' if 'Mention All'      in tab_headers else None) # Mention All
            role_info.append(f'{Fore.GREEN}Yes{Fore.RESET}' if int(role['permissions']) & 0x0000000020000000 != 0 and 'Webhooks'         in tab_headers else f'{Fore.RED}No{Fore.RESET}' if 'Webhooks'         in tab_headers else None) # Webhooks
            role_info.append(f'{Fore.GREEN}Yes{Fore.RESET}' if int(role['permissions']) & 0x0000000080000000 != 0 and 'App Commands'     in tab_headers else f'{Fore.RED}No{Fore.RESET}' if 'App Commands'     in tab_headers else None) # Application commands
            role_info.append('' + \
                (f'{Fore.BLUE}Bot{Fore.RESET}' if 'tags' in role and 'bot_id' in role['tags'] else \
                 f'{Fore.LIGHTMAGENTA_EX}Booster{Fore.RESET}' if 'tags' in role and 'premium_subscriber' in role['tags'] else \
                 f'{Fore.CYAN}Premium{Fore.RESET}' if 'tags' in role and 'available_for_purchase' in role['tags'] else \
                 ''
                )
            ) # Handle tags
     
            role_info = [x for x in role_info if x is not None]
            data.append(role_info)

        tab_data = tabulate(data, headers=tab_headers, tablefmt='github')
        print(f'\n{tab_data}' )

        with open(f'./export/{server_id}_roles.txt', 'w', encoding='utf-8') as handle:
            handle.write(ansi_escape.sub(r'', tab_data))

    except Exception as err:
        print(f'{Fore.YELLOW} [!] {token} retrying.. {Fore.RESET}({Fore.LIGHTBLACK_EX}{err}{Fore.RESET})')
        pass

    print(f'\n{Fore.YELLOW}[!] Completed{Fore.RESET}')
    scrape_again = input(f'{Fore.LIGHTBLUE_EX}[!] Scrape another server? (Y/N): {Fore.RESET}')

    if 'n' in scrape_again.lower():
        return sys.exit()

    main()

def main():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print(f'{Fore.RED}Discord Role Scraper v1.1 | Fantasy{Fore.RESET}\n')

    token = input(f'{Fore.RED}Token: {Fore.RESET}').strip('\'\"')
    server_id = input(f'{Fore.RED}Server ID: {Fore.RESET}')

    scrape_roles(token, server_id)

if __name__ == '__main__':
    main()