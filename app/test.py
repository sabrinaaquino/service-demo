import tweepy
import twitter_config as tc

# authorize the API Key
authentication = tweepy.OAuthHandler(tc.api_key, tc.api_secret_key)

# authorization to user's access token and access token secret
authentication.set_access_token(tc.access_token, tc.access_token_secret)

# call the api
api = tweepy.API(authentication)

try:
    user = api.verify_credentials()
    print("Authentication successful. Your account name is: ", user.name)
except tweepy.TweepyException as e:
    print("Authentication failed. Please check your API keys. Error:", e)
