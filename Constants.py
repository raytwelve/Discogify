# Field Names
GET  = 'get'
POST = 'post'
ID = 'id'
NAME = 'name'
EXPLICIT = 'explicit'
DISC_NUMBER = 'disc_number'
DURATION_MS = 'duration_ms'
TRACK_NUMBER = 'track_number'
IS_PLAYABLE = 'is_playable'
URI = 'uri'
ITEMS = 'items'
ARTISTS = 'artists'


# get_token
AUTHORIZATION_CODE = 'authorization_code'

#step 2
ACCESS_TOKEN = 'access_token'
REFRESH_TOKEN = 'refresh_token'

CODE = 'code'


HEADER_CONTENT_TYPE = 'Content-Type'
HEADER_AUTHORIZATION = 'Authorization'
HEADER_ACCEPT = 'Accept'
HEADER_JSON = 'application/json'
HEADER_FORM = 'application/x-www-form-urlencoded'
HEADER_BASIC = 'Basic '
HEADER_BEARER = 'Bearer '

BODY_GRANT_TYPE = 'grant_type'
BODY_REDIRECT_URI = 'redirect_uri'

PARAM_MARKET = 'market'
PARAM_LIMIT = 'limit'
PARAM_OFFSET = 'offset'
PARAM_INCLUDE_GROUPS = 'include_groups'


# Defaul Values
TIMEOUT = 5
QUERY_LIMIT = 100
SEARCH_LIMIT = 50
OFFSET = 0
TOKEN_TYPE = {AUTHORIZATION_CODE: CODE, REFRESH_TOKEN: REFRESH_TOKEN}
SUCCESS_CODES = [200, 201]
RESPONSE_MAX_SIZE = 50


MARKETS = 'US'
ALBUM_GROUPS = 'album,single,appears_on,compilation'
# ALBUM_GROUPS = 'appears_on,compilation'
SCOPE = 'playlist-read-public playlist-read-private playlist-modify-public playlist-modify-private'