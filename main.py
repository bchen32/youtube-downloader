import pytube

import converter
import downloader

directory = 'C:/Data/Python/youtube-downloader/downloads/'
playlist = pytube.Playlist('https://www.youtube.com/playlist?list=PLFITtxHy9Gk4gsWyU7uCVHK2Xp6W4pW35')
start_ind = 651
downloader.download(playlist, directory, start_ind)
converter.convert_normalize(directory)