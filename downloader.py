from time import sleep

import pytube

def download(playlist, directory, start_ind=1, end_ind=None):
	downloaded = []
	ind = 0
	for video in playlist.videos:
		ind += 1
		if ind >= start_ind:
			print('Downloading {} {} / {}'.format(video.title, ind, len(playlist.videos)))
			downloaded.appen(video.title)
			video.streams.filter(file_extension='mp4').first().download(directory)
			sleep(1)
		if end_ind and ind >= end_ind:
			break
	with open('current.txt', 'a', encoding='utf-8') as f:
		for title in downloaded:
			f.write(title + '\n')
