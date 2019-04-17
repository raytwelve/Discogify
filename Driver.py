import SpottyUtils, SpottyCollect, SpottyWrapper, Constants

def full_run():
	album_groups = Constants.ALBUM_GROUPS
	search_limit = Constants.SEARCH_LIMIT
	offset = Constants.OFFSET
	markets= Constants.MARKETS
	return_field= Constants.ITEMS
	token = SpottyUtils.loadString('in/access_token.txt')
	artist_id = ''
	playlistName = ''

	albums, success = SpottyCollect.getAllAlbumsFromArtist(artist_id, offset, token, album_groups)

	# save for later use; dont have to make API calls
	SpottyUtils.sortFormatSaveAlbums('out/albums.txt', albums)
	print("Saved the albums.")


	a_tracks = dict()
	for album_id, album_title in albums.items():
		tracks, success = SpottyWrapper.getTracksByArtistFromAlbum(artist_id, album_id, token, Constants.SEARCH_LIMIT, Constants.MARKETS, return_field)
		t_filtered, success = SpottyWrapper.filterTracksMetadata(artist_id, tracks, success)
		a_tracks.update(t_filtered)

		# save for later use; dont have to make API calls
		album_title = album_title.replace("/", "_").replace(":", "_")
		outfilename = 'out/album_tracks/' + album_title + '__' + album_id + '.txt'
		SpottyUtils.saveJson(outfilename, t_filtered)

	SpottyUtils.saveJson('out/album_tracks/__album_tracks.txt', a_tracks)


	output_filename = "out/tracks.txt"
	list_of_songs = SpottyUtils.sortFormatSaveTracks(output_filename, a_tracks)
	input("Saved the tracks.")

	return list_of_songs


def loadAllTracksFromFile(filename):
	return SpottyUtils.sortFormatSaveTracks(None, SpottyUtils.loadJson(filename))



def groupByTitles(tracks):
	titlegroups = list()

	first = ""
	for i in range(len(tracks)):
		track = tracks[i]
		track_id = track[0]
		track_meta = track[1]
		title = track_meta[0]
		if not SpottyUtils.titleMatch(first, title):
			first = title
			titlegroups.append(dict())
		titlegroups[-1][track_id] = track_meta
	return titlegroups



def main():
	filename = "out/album_tracks/__album_tracks.txt"
	start_from_scratch  = False
	list_of_songs = None

	if start_from_scratch:
		list_of_songs = full_run()
	else:
		list_of_songs = loadAllTracksFromFile(filename)


	grouped = groupByTitles(list_of_songs)
	print("grouped songs by title.")

	for i in range(len(grouped)):
		same_songs = grouped[i]
		title = list(same_songs.values())[0][0]
		title = title.replace("/", "_").replace(":", "_")
		contents = SpottyUtils.jsonifyTracks(same_songs)
		filename = 'out/duplicate_tracks/' + title + '.txt'
		SpottyUtils.saveString(filename, contents)

main()

























