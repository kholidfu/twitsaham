from twython import Twython
import pandasaham as pshm
import time
import datetime

now_time = datetime.datetime.fromtimestamp(time.mktime(time.gmtime((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() + 25200))).strftime('%Y-%m-%d %H:%M:%S')

# url
# https://twython.readthedocs.org/en/latest/usage/advanced_usage.html

cons_key = 'wjK82GEwfXhD7mQep76p8Q'
cons_secret = 'wr5bymR0jt8N7Kl5CUw22g2cngmMLFsaZnt7AWE8'
acc_token = '14355401-A71yN2Ik9tZEroe1neT2P2v9LBOgIpAhBWGrTLYbp'
acc_token_sec = 'MA1950ket722UktcCfO3zGFMkRKxFEngShWeqgaQY'

t = Twython(app_key=cons_key,
            app_secret=cons_secret,
            oauth_token=acc_token,
            oauth_token_secret=acc_token_sec)

# update no media
# t.update_status(status='hello from twython!')


# download and analyze it
pshm.dl()
# update twitter _with_media
photo = open('ihsg.png', 'rb')
t.update_status_with_media(status='[Autotwit] Grafik Pergerakan IHSG 3 bulan terakhir dgn Analisis MACD ' + now_time + ' #saham #ihsg #jci #idx', media=photo)
