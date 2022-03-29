import pytube

directory = 'C:/Data/Python/youtube-downloader/downloads/'
playlist = pytube.Playlist('https://www.youtube.com/playlist?list=PLFITtxHy9Gk4gsWyU7uCVHK2Xp6W4pW35')

with open('current.txt', 'r', encoding='utf-8') as f:
	current = f.read().splitlines()

ind = 0
titles = []
not_found = []
deleted = []
for video in playlist.videos:
	ind += 1
	title = video.title
	titles.append(title)
	print('Traversing {} {} / {}'.format(title, ind, len(playlist.videos)))
	if title not in current:
		not_found.append([video.title, ind])

for curr_title in current:
	if curr_title not in titles:
		deleted.append(curr_title)

for vid in not_found:
	print('\n----Not found---- {} {}\n'.format(vid[0], vid[1]))
for title in deleted:
	print('\n----Deleted---- {}\n'.format(title))