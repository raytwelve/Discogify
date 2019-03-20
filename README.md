# Step 1:

First, you will need to hit Spotify API to obtain an authorization_code:

https://accounts.spotify.com/authorize?client_id={your_client_id}&response_type=code&redirect_uri={your_redirect_uri}&scope={permissions_scope}


### Details:
{your_client_id} was given in initial app registration with Spotify
{your_redirect_uri}  was configured in initial app registration with Spotify
{permissions_scope} is how much permissions you will allow for this token-holder to interact with your Spotify account

Ex.
playlist-read-private playlist-modify-public playlist-modify-private


use the code that follows your redirect uri in the address bar to get an access_token via Spotify API 'https://accounts.spotify.com/api/token'
this code is {your_authorization_code}
or SpottyWrapper.getAccessToken()
### Header Fields:
- Authorization: Basic ({{client_id:client_secret}}).encodeBase64()
	- {your_client_id}:{your_client_secret} in base64

### Body Fields:
- grant_type: authorization_code
- redirect_uri: {your_redirect_uri}
- code: {your_authorization_code}
- refresh_token: {your_refresh_token}

### Note: if access_token expires, we can avoid making another call to 
1. https://accounts.spotify.com/authorize, and then 
2. https://accounts.spotify.com/api/token

by using the refresh_token to request a new access_token.
#### make another call to 'https://accounts.spotify.com/api/token':
- change authorization_code to refresh_token
- change code: {your_authorization_code} to refresh_token: {your_refresh_token}