import pytube
from time import sleep

playlist = pytube.Playlist('https://www.youtube.com/playlist?list=PLFITtxHy9Gk4gsWyU7uCVHK2Xp6W4pW35')
ind = 0
start_ind = 1
for video in playlist.videos:
	ind += 1
	if ind >= start_ind:
		print('Downloading {} {} / {}'.format(video.title, ind, len(playlist.videos)))
		video.streams.filter(file_extension='mp4').first().download('C:/Data/Python/Youtube-Downloader/Downloads/')
		sleep(1)