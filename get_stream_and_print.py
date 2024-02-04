import time
import requests

def stream_api(url):
    response = requests.get(url, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        for chunk in response.iter_content(chunk_size=1):
            # Decode chunk and end='', to avoid newlines added by print
            print(chunk.decode('utf-8'), end='', flush=True)

    else:
        print(f"Failed to connect to the API, status code: {response.status_code}")

    print("\n")

def progress_bar(total):
    for i in range(total):
        #print('#', end='', flush=True)
        print('#', end='') # no flush, only print after the whole line is done.
        time.sleep(0.02)
    print('\n')


api_url = 'https://www.jodfun.com/stream_api/get-stream'
#api_url = 'http://0.0.0.0:3009/stream_api/get-stream'

stream_api(api_url)
#fetch_and_print_stream(stream_url)
#progress_bar(50)

