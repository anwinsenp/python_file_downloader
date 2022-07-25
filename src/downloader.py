import requests


def getFilename_fromURL(url):
    return url.rsplit('/', 1)[1] if url.find('/') else None


def download(url, output_dir):
    print(f"downloading {url} ...")
    try:
        r = requests.get(url, allow_redirects=True)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    print(f"{r.status_code} HTTP response")
    if r.status_code == 200:
        filename = getFilename_fromURL(url)
        output_dir = output_dir[:-1] if output_dir[-1] == '/' else output_dir
        try:
            with open(f"{output_dir}/{filename}", 'wb') as f:
                f.write(r.content)
        except IOError as e:
            raise SystemExit(e)
