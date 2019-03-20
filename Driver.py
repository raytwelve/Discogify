import SpottyWrapper
import Constants
import SpottyUtils

def main():
	album_groups = Constants.ALBUM_GROUPS
	search_limit = Constants.SEARCH_LIMIT
	offset = Constants.OFFSET
	markets= Constants.MARKETS
	return_field= Constants.ITEMS
	token = SpottyUtils.loadString('in/access_token.txt')
	artist_id = ''

	albums, success = SpottyWrapper.getAlbumsByArtist(artist_id, token, album_groups, search_limit, offset, markets, return_field)
	a_filtered, success = SpottyWrapper.filterAlbumsMetadata(albums, success)
	SpottyUtils.saveJson('out/albums.txt', a_filtered)

	for a_id, a_title in a_filtered.items():
		tracks, success = SpottyWrapper.getTracksByArtistFromAlbum(artist_id, a_id, token, Constants.SEARCH_LIMIT, Constants.MARKETS, return_field)
		t_filtered, success = SpottyWrapper.filterTracksMetadata(tracks, success)
		a_title = a_title.replace("/", "_").replace(":", "_")
		outfilename = 'out/album_tracks/' + a_title + '__' + a_id + '.txt'
		SpottyUtils.saveJson(outfilename, t_filtered)

	# load all tracks into one collection
	# filter duplicates, keep explicit version over clean version

	# create new playlist
	# add filtered collection of track_ids to playlist



main()