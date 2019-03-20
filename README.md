## Step 1:
First, you will need to hit Spotify API to obtain an __{authorization_code}__:

https://accounts.spotify.com/authorize?client_id={your_client_id}&response_type=code&redirect_uri={your_redirect_uri}&scope={permissions_scope}

### Details:
#### Request parameters:
__{your_client_id}__ was given in initial app registration with Spotify

__{your_redirect_uri}__  was configured in initial app registration with Spotify

__{permissions_scope}__ is how much permissions you will allow for this token-holder to interact with your Spotify account

Ex.
playlist-read-private playlist-modify-public playlist-modify-private


## Step 2:
use the __{code}__ that follows your redirect uri in the address bar to get an access_token via Spotify API 

https://accounts.spotify.com/api/token

This __{code}__ is __{your_authorization_code}__.

Alternatively, you can use the SpottyWrapper.getAccessToken function

### Details
#### Header Fields:
- Authorization: Basic __{client_id_secret_base_64}__
	- '{your_client_id}:{your_client_secret}' in base64
}

#### Body Fields:
- grant_type: authorization_code
- redirect_uri: __{your_redirect_uri}__
- code: __{your_authorization_code}__
- refresh_token: __{your_refresh_token}__

### Note: 
if access_token expires, we can repeat step 1 and 2:
1. https://accounts.spotify.com/authorize, and then 
2. https://accounts.spotify.com/api/token

Or make one call to https://accounts.spotify.com/api/token
by using the __{refresh_token}__ to request a new __{access_token}__.

Make another call to https://accounts.spotify.com/api/token:
- change code: __{your_authorization_code}__ to refresh_token: __{your_refresh_token}__


## Step 3:
copy __{your_authorization_code}__ in to __"./in/access_token.txt"__ and run Driver.py
1. Navigate to the root directory of repository
2. Run python Driver.py {directory.of.access.token.fiile} {sportify.artist.id} {sportify.playlist.name}