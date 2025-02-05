import requests

LINKEDIN_BASE_URL = "https://www.linkedin.com"
API_BASE_URL = f"{LINKEDIN_BASE_URL}/voyager/api"
REQUEST_HEADERS = {
    "user-agent": " ".join(
        [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5)",
            "AppleWebKit/537.36 (KHTML, like Gecko)",
            "Chrome/83.0.4103.116 Safari/537.36",
        ]
    ),
    "accept-language": "en-AU,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "x-li-lang": "en_US",
    "x-restli-protocol-version": "2.0.0",
}

AUTH_REQUEST_HEADERS = {
    "X-Li-User-Agent": "LIAuthLibrary:0.0.3 com.linkedin.android:4.1.881 Asus_ASUS_Z01QD:android_9",
    "User-Agent": "ANDROID OS",
    "X-User-Language": "en",
    "X-User-Locale": "en_US",
    "Accept-Language": "en-us",
}

class LinkedinAuthGateway:
    def __init__(self):
        self.session = requests.session()
        self.session.proxies.update({})
        self.session.headers.update(REQUEST_HEADERS)
    
    def _request_session_cookies(self):
        """
        Return the session cookies as given by LinkedIn
        """
        res = requests.get(
            f"{LINKEDIN_BASE_URL}/uas/authenticate",
            headers=AUTH_REQUEST_HEADERS,
            proxies={},
        )

        return res.cookies
    
    def authenticate(self, username: str, password: str):
        cookies = self._request_session_cookies()

        JSESSIONID = cookies["JSESSIONID"].strip('"')

        payload = {
            "session_key": username,
            "session_password": password,
            "JSESSIONID": JSESSIONID,
        }

        new_headers = AUTH_REQUEST_HEADERS.copy()

        new_headers["csrf-token"] = JSESSIONID

        response = requests.post(
            f"{LINKEDIN_BASE_URL}/uas/authenticate",
            data=payload,
            headers=new_headers,
            cookies=cookies,
            proxies={},
        )

        data = response.json()

        if data and data["login_result"] != "PASS":
            raise Exception(data["login_result"])
        
        if response.status_code == 401:
            raise Exception("Unauthorized")
        
        if response.status_code != 200:
            raise Exception("Unknown error")
        
        return {
            'cookies': response.cookies.get_dict(),
            'csrf': response.cookies["JSESSIONID"].strip('"')
        }