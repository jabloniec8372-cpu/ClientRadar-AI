import urllib.request
import urllib.error
import ssl
import re
import http.client
from urllib.parse import urlparse, urlunparse


def get_page_title(html):
    title_match = re.search(
        r"<title>(.*?)</title>",
        html,
        re.IGNORECASE | re.DOTALL
    )

    if title_match:
        return clean_title(title_match.group(1).strip())

    return "No title found"


def clean_title(title):
    blocked_phrases = [
        "your request has been blocked",
        "access denied",
        "request blocked",
        "bot detection",
    ]

    title_lower = title.lower()

    for phrase in blocked_phrases:
        if phrase in title_lower:
            return "Website protected or blocked"

    return title


def build_result(online, status, title):
    return {
        "website_online": online,
        "website_status": status,
        "website_title": title,
        "online": online,
        "status": status,
        "title": title,
    }


def build_headers():
    return {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/126.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "close",
    }


def get_url_options(url):
    parsed_url = urlparse(url)
    urls = [url]

    if parsed_url.netloc and not parsed_url.netloc.startswith("www."):
        www_url = urlunparse(parsed_url._replace(netloc=f"www.{parsed_url.netloc}"))
        urls.append(www_url)

    return urls


def open_website(url, method, context=None):
    request = urllib.request.Request(
        url,
        headers=build_headers(),
        method=method
    )

    return urllib.request.urlopen(request, timeout=5, context=context)


def check_with_http_client(url):
    parsed_url = urlparse(url)
    path = parsed_url.path or "/"

    if parsed_url.query:
        path = f"{path}?{parsed_url.query}"

    if parsed_url.scheme == "https":
        connection = http.client.HTTPSConnection(parsed_url.netloc, timeout=5)
    else:
        connection = http.client.HTTPConnection(parsed_url.netloc, timeout=5)

    try:
        connection.request("HEAD", path, headers=build_headers())
        response = connection.getresponse()

        return build_result(True, response.status, "No title found")

    except Exception:
        return build_result(False, None, "Unavailable")

    finally:
        connection.close()


def check_one_url(url, context=None):
    try:
        response = open_website(url, "GET", context)

        html = response.read(50000).decode("utf-8", errors="ignore")
        title = get_page_title(html)

        return build_result(True, response.status, title)

    except urllib.error.HTTPError as error:
        html = error.read(50000).decode("utf-8", errors="ignore")
        title = get_page_title(html) if html else "Unavailable"

        return build_result(True, error.code, title)

    except ssl.SSLError:
        raise

    except Exception:
        try:
            response = open_website(url, "HEAD", context)

            return build_result(True, response.status, "No title found")

        except urllib.error.HTTPError as error:
            return build_result(True, error.code, "Unavailable")

        except ssl.SSLError:
            raise

        except Exception:
            return build_result(False, None, "Unavailable")


def check_website(url):
    for url_option in get_url_options(url):
        result = check_one_url(url_option)

        if result["website_online"]:
            return result

        result = check_with_http_client(url_option)

        if result["website_online"]:
            return result

        try:
            context = ssl._create_unverified_context()
            result = check_one_url(url_option, context)

            if result["website_online"]:
                return result

        except ssl.SSLError:
            pass

    return build_result(False, None, "Unavailable")
