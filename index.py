from ablesci import ablesci

Cookie = "_identity-frontend=5dc0959958a5d1510b8b43e52513bb19cd3ee03db3707fb76decfa9a449e56cea%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22_identity-frontend%22%3Bi%3A1%3Bs%3A51%3A%22%5B325620%2C%22PT8R-8BHzS6PPzSJfeuRws99092zkG41%22%2C2592000%5D%22%3B%7D; ablesci-serial=0ebcbba32f7237dcbf5fa96443ecc6f6; advanced-frontend=08d66q9h1f802e40ikgdhbo4r7; _csrf=4a16bfbbb41e973ff70c55d80dbb238cde10c51eac410f0f0db9d0bd869c3fc9a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22SyKQnU2wkulvSNOPsX2GJiJaPBgzKgrq%22%3B%7D; Hm_lvt_21ea3daf4a17e94a98a483d3d810f41a=1706060845,1706599415,1707560383,1707565418; security_session_verify=41ee7b0eca0a584f69d940a4a2287f6d; Hm_lpvt_21ea3daf4a17e94a98a483d3d810f41a=1707566348" # 替换自己在浏览器中的Cookie

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"{Cookie}",
    "DNT": "1",
    "Referer": "https://www.ablesci.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

def main():
    ablesci(headers=headers)

if __name__ == "__main__":
    main()
