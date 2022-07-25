import requests
from clint.textui import progress


def getFilename_fromURL(url):
    return url.rsplit('/', 1)[1] if url.find('/') else None


def download(url, output_dir):
    print(f"downloading {url}")
    try:
        r = requests.get(url, stream=True)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    print(f"{r.status_code} HTTP response")
    if r.status_code == 200:
        filename = getFilename_fromURL(url)
        output_dir = output_dir[:-1] if output_dir[-1] == '/' else output_dir
        try:
            with open(f"{output_dir}/{filename}", 'wb') as f:
                total_length = int(r.headers.get('content-length'))
                for chunk in progress.bar(
                        r.iter_content(chunk_size=1024),
                        expected_size=(total_length/1024) + 1):
                    if chunk:
                        f.write(chunk)
                        f.flush()
        except IOError as e:
            raise SystemExit(e)
