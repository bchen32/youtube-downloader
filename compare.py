from time import sleep

import pytube, os

directory = 'C:/Data/Python/youtube-downloader/downloads/'
playlist = pytube.Playlist('https://www.youtube.com/playlist?list=PLFITtxHy9Gk4gsWyU7uCVHK2Xp6W4pW35')

ind = 0
files = [x[2] for x in os.walk(directory)]
files[0] = [file[:-4] for file in files[0]]
titles = []
for video in playlist.videos:
	ind += 1
	title = video.streams.filter(file_extension='mp4').first().default_filename[:-4]
	titles.append(title)
	print('Traversing {} {} / {}'.format(title, ind, len(playlist.videos)))
	if title not in files[0]:
		print('\n----Not found---- {}\n'.format(video.title))
	sleep(1)
for file in files[0]:
	if file not in titles:
		print('\n----Deleted---- {}\n'.format(file))
