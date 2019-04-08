import SpottyUtils, SpottyCollect, SpottyWrapper, Constants

def main():
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
	print("Saved the tracks.")

	exit()

	# filter duplicates, keep explicit version over clean version

	# create new playlist
	# add filtered collection of track_ids to playlist



main()