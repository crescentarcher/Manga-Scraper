from stringHelpers import get_url  # Importing get_url from stringHelpers.py
import requests
import shutil
import os

def send_request(url, binary=False):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        request = requests.get(url, stream=binary, headers=headers)
        
        # If the request is blocked (status code 403), print the response body
        if request.status_code == 403:
            print(f"Request blocked! Response: {request.text}")
            exit()
    except Exception as e:
        print(f"Error during the HTTP request: {e}")
        exit()

    return request

def not_released_yet(seriesName, chpNum):
    manga_url = get_url(seriesName, chpNum)  # Now this is recognized
    html = send_request(manga_url).text

    return NOT_RELEASED_MSG in html

def download_img(url, download_path, pgNum):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    img_name = add_zeros(str(pgNum)) + FILE_EXT
    img_path = download_path + img_name

    request = send_request(url, True)

    with open(img_path, 'wb') as file_path:
        request.raw.decode_content = True
        shutil.copyfileobj(request.raw, file_path)

    print(DOWNLOADING_MSG + str(pgNum))
