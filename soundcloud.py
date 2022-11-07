#---------------------------------
# Soundcloud
# soundcloud.py
#
# @ start date          04 11 2022
# @ last update         07 11 2022
#---------------------------------

#---------------------------------
# Imports
#---------------------------------
import requests, re
from bs4 import BeautifulSoup

from typing import List

#---------------------------------
# Function: soundcloud_playlist
#---------------------------------
def soundcloud_playlist(url: str) -> List[str]:
    '''
    Returns a list of all the songs in the playlist.
    '''
    html = requests.get(url)
    if html.status_code != 200:
        raise ValueError('Couldn\'t retrieve that soundcloud playlist.')
    
    # Parse the response to find all 'script' tags
    soup = BeautifulSoup(html.text, 'html.parser')
    scripts = soup.find_all('script')

    # Locate and extract playlist info from the scripts
    data_json_pattern = re.compile(r"\"tracks\":\[(.*?)\],\".*\":")
    song_idx_pattern = re.compile(r'"id":([^,]+),"kind":"track"')
    
    for script in scripts:
        m = re.search(data_json_pattern, str(script))
        if m:
            break
        
    if not m:
        raise ValueError('Couldn\'t find the playlist info.')

    # Convert each song id into a streamable url for that song
    urls = []
    for idx in re.finditer(song_idx_pattern, m.group(1)): 
        urls.append(f'https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/{idx.group(1)}')

    return urls

#---------------------------------
# Execute
#---------------------------------
if __name__ == '__main__':
    urls = soundcloud_playlist('https://soundcloud.com/erasojajao/sets/orbital-mix-best-of-1')
    for url in urls:
        print(url)
