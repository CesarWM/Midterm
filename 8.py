def is_valid_url(url):
    if not (url.startswith("http://") or url.startswith("https://")):
        return False
    scheme_end_index = url.find("://") + 3
    path_start_index = url.find("/", scheme_end_index)
    if path_start_index == -1:
        domain_part = url[scheme_end_index:]
    else:
        domain_part = url[scheme_end_index:path_start_index]
    if "." not in domain_part or " " in domain_part:
        return False
    return True