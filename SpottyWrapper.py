import Constants
import SpottyUtils

def getAccessToken(code_token: str, grant_type: str, app_creds: dict, return_field: str=None) -> (dict, bool):
	url = "https://accounts.spotify.com/api/token/"
	headers = {
	Constants.HEADER_CONTENT_TYPE : Constants.HEADER_FORM,
	Constants.HEADER_AUTHORIZATION : Constants.HEADER_BASIC + app_creds.get('base64idsecret')
	}

	body = {
	Constants.BODY_GRANT_TYPE : grant_type,
	Constants.BODY_REDIRECT_URI : app_creds.get(Constants.BODY_REDIRECT_URI),
	Constants.TOKEN_TYPE.get(grant_type) : code_token
	}
	params = {}

	items, success = SpottyUtils.getItemsFromRequest(Constants.POST, url, headers, body, params, return_field)
	return items, success

def getAlbumsByArtist(artist_id: str, token: str, album_groups: str, search_limit: int, offset: int, markets: str, return_field: str) -> (dict, bool):
	url = "https://api.spotify.com/v1/artists/" + artist_id + "/albums/"
	albums = {}
	headers = {
	Constants.HEADER_ACCEPT : Constants.HEADER_JSON,
	Constants.HEADER_AUTHORIZATION : Constants.HEADER_BEARER + str(token)
	}
	body = {}
	params = {Constants.PARAM_LIMIT : str(search_limit), Constants.PARAM_OFFSET : str(offset), Constants.PARAM_INCLUDE_GROUPS : album_groups, Constants.PARAM_MARKET : markets}

	items, success = SpottyUtils.getItemsFromRequest(Constants.GET, url, headers, body, params, return_field)
	return items, success

def getTracksByArtistFromAlbum(artist_id: str, album_id: str, token: str, search_limit: int=Constants.SEARCH_LIMIT, markets: str=Constants.MARKETS, return_field: str=Constants.ITEMS) -> (dict, bool):
	url = "https://api.spotify.com/v1/albums/" + album_id + "/tracks/"
	tracks = {}

	headers = {
	Constants.HEADER_ACCEPT : Constants.HEADER_JSON,
	Constants.HEADER_AUTHORIZATION : Constants.HEADER_BEARER + token
	}
	body = {}
	params = {
	Constants.PARAM_MARKET: markets,
	Constants.PARAM_LIMIT: str(search_limit)
	}

	items, success = SpottyUtils.getItemsFromRequest(Constants.GET, url, headers, body, params, return_field)
	return items, success

def filterTracksMetadata(tracks: list, success: bool) -> (dict, bool):
	filtered = dict()
	for track in tracks:
		t_id = track.get(Constants.ID)
		t_duration = track.get(Constants.DURATION_MS)
		t_explicit = track.get(Constants.EXPLICIT)
		t_title = track.get(Constants.NAME)
		filtered[t_id] = [t_title, t_explicit, t_duration]
	return filtered, success

def filterAlbumsMetadata(albums: dict, success: bool) -> (dict, bool):
	filtered = dict()
	for album in albums:
		artists = album.get(Constants.ARTISTS) #list
		for artist in artists:
			filtered[album.get(Constants.ID)] = album.get(Constants.NAME)
	return filtered, success

def createPlaylist(user_id: str, playlist_name: str, token: str, return_field: str=Constants.ITEMS) -> (dict, bool):
	url = "https://api.spotify.com/v1/users/" + user_id + "/playlists/"
	bodyjson = '{"name":"' + playlist_name + '", "public":"false"}'
	headers = {
	Constants.HEADER_CONTENT_TYPE : Constants.HEADER_JSON,
	Constants.HEADER_AUTHORIZATION : Constants.HEADER_BEARER + token
	}
	body = bodyjson
	params = {}
	items, success = SpottyUtils.getItemsFromRequest(Constants.POST, url, headers, body, params, return_field)

	return {items.get(Constants.ID) : items.get(Constants.NAME)}, success if success else items, success

def addToPlaylist(playlist_id: str, listoftrackuris: str, token: str, return_field: str=Constants.ITEMS) -> (dict, bool):
	url = "https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks"
	headers = {
	Constants.HEADER_CONTENT_TYPE : Constants.HEADER_JSON,
	Constants.HEADER_AUTHORIZATION : Constants.HEADER_BEARER + token
	}
	body = listoftrackuris.encode('utf-8')
	params = {}

	items, success = SpottyUtils.getItemsFromRequest(Constants.POST, url, headers, body, params, return_field)
	return items, success

