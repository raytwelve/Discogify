import SpottyWrapper;
import Constants;

def jsonifyList(li: list) -> str:
	stringer = '{"uris":['
	for ea in li:
		stringer += '"' + ea + '",'
	stringer = stringer[:len(stringer)-1] + ']}'
	return stringer

def addAllTracksToPlaylist(tracks: list, playlist_id: str, token: str):
	size = len(tracks)
	hundos = size//Constants.QUERY_LIMIT
	extras = 0 if size%Constants.QUERY_LIMIT == 0 else 1

	for i in range(hundos + extras):
		offset = i*Constants.QUERY_LIMIT
		hundredtracks = tracks[offset:offset+Constants.QUERY_LIMIT]

		alist = jsonifyList(hundredtracks)
		re, success = SpottyWrapper.addToPlaylist(playlist_id, alist, token)
		if(not success):
			break
			
		print("added "+ repr(len(hundredtracks)) +" tracks to playlist.")

# wrapper function for getAlbumsByArtist(), use this function if number of albums is expected to exceed 50
def getAllAlbumsFromArtist(artist_id: str, offset: int, token: str, album_groups: str):
	albums = dict()
	off = offset
	resp_size = Constants.RESPONSE_MAX_SIZE
	while(resp_size == Constants.RESPONSE_MAX_SIZE):
		items = dict()
		success = False
		items, success = SpottyWrapper.getAlbumsByArtist(artist_id, token, album_groups, Constants.RESPONSE_MAX_SIZE, off, Constants.MARKETS, Constants.ITEMS)
		if(not success):
			return items, success
		for item in items:
			albums[item.get(Constants.ID)] = item.get(Constants.NAME)
		resp_size = len(items)
		off += Constants.RESPONSE_MAX_SIZE
	return albums, success

# implement as needed
def getAllTracksByArtistFromAlbums(artist_id: str, albums: dict, token: str):
	tracks = {}

	# key=(album_id, album_name, is_explicit)
	# value=dict()
	# 	key=track_id
	# 	value=track_metadata
	success=True
	for album_id in album_ids.keys():
		album_tracks, success = SpottyWrapper.getTracksByArtistFromAlbum(artist_id, album_id, token)
		if(not success):
			return album_tracks, success
		tracks.update(album_tracks)
	return tracks, success



