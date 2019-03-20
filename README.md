https://accounts.spotify.com/authorize?client_id={your_client_id}&response_type=code&redirect_uri={your_redirect_uri}&scope={permissions_scope}



your_client_id, your_redirect_uri:
configured in initial Spotify API request

permissions_scope:
playlist-read-private playlist-modify-public playlist-modify-private


use the code that follows your redirect uri in the address bar to get an access_token via Spotify API 'https://accounts.spotify.com/api/token'
this code is {your_authorization_code}
or SpottyWrapper.getAccessToken()
Header Fields:
Authorization: Basic ({{client_id:client_secret}}).encodeBase64()

Body Fields:
grant_type: authorization_code
redirect_uri: {your_redirect_uri}
code: {your_authorization_code}
refresh_token: {your_refresh_token}

# Note: if access_token expires, we can avoid making another call to https://accounts.spotify.com/authorize, then https://accounts.spotify.com/api/token
by using the refresh_token to request a new access_token.
make another call to 'https://accounts.spotify.com/api/token':
- change authorization_code to refresh_token
- change code: {your_authorization_code} to refresh_token: {your_refresh_token}