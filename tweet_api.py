import tweepy

class get_twitter_api:

    _CONSUMER_KEY    = 'xxxxx'
    _CONSUMER_SECRET = 'xxxxx'
    _ACCESS_TOKEN    = 'xxxxx'
    _ACCESS_SECRET   = 'xxxxx'

    try:
        f = open('token.txt')
        token = f.readlines()
        f.close()

        _CONSUMER_KEY    = token[0].rstrip('\r\n')
        _CONSUMER_SECRET = token[1].rstrip('\r\n')
        _ACCESS_TOKEN    = token[2].rstrip('\r\n')
        _ACCESS_SECRET   = token[3].rstrip('\r\n')

    except:
        print('Consumer Key等が設定されていないようです')
        print('詳細はこちら -> '
              'http://statsbeginner.hatenablog.com/'
              'entry/2015/10/21/131717')

        _CONSUMER_KEY    = input('Consumer Keyを入力してください :')
        _CONSUMER_SECRET = input('Consumer Secretを入力してださい :')
        _ACCESS_TOKEN    = input('Access Tokenを入力してください :')
        _ACCESS_SECRET   = input('Access Token Secretを入力してください :')

    _auth = tweepy.OAuthHandler(_CONSUMER_KEY, _CONSUMER_SECRET)
    _auth.set_access_token(_ACCESS_TOKEN, _ACCESS_SECRET)

    _api = tweepy.API(_auth)

    def get_tl(self):
        try:
            return self._api.home_timeline()[0].text

        except Exception as err:
            #return ('Error:Something happened(なにかがおきました)')
            return ('エラー:{0}'.format(err.args[0][0]['message']))

    def post(self,tweet):
        self._api.update_status(tweet)
