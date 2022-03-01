import pytube

import converter
import downloader

directory = 'C:/Data/Python/youtube-downloader/downloads/'
playlist = pytube.Playlist('https://www.youtube.com/playlist?list=PLFITtxHy9Gk4gsWyU7uCVHK2Xp6W4pW35')
downloader.download(playlist, directory, 726)
converter.convert_normalize(directory)