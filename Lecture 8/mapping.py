{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import time\n",
    "import json\n",
    "from tweepy.streaming import StreamListener\n",
    "from tweepy import OAuthHandler\n",
    "from tweepy import Stream\n",
    "\n",
    "C_KEY = 'XXXXXXX'\n",
    "C_SECRET = 'XXXXXXX'\n",
    "A_TOKEN_KEY = 'XXXXXX'\n",
    "A_TOKEN_SECRET = 'XXXXXXX'\n",
    "\n",
    "bbox = [22,49,-119,-64]    # bounding box for United States\n",
    "lats = []\n",
    "lons = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "41.66900774 , -73.98039447\n",
      "41.77842988 , -81.13553257\n",
      "39.9457731 , -86.1477107\n",
      "42.37356418 , -71.12133731\n",
      "28.19478932 , -82.50367058\n",
      "38.90024882 , -76.99998949\n",
      "40.7207559 , -74.0007613\n",
      "40.82786913 , -73.50245575\n",
      "39.9622783 , -75.1412627\n",
      "33.13755119 , -97.734375\n",
      "33.00137556 , -96.70438528\n",
      "32.9167085 , -96.7678438\n",
      "41.59233747 , -93.60351563\n",
      "29.7629 , -95.3832\n",
      "40.747214 , -73.954733\n",
      "33.13755119 , -97.734375\n",
      "40.74225526 , -73.95587537\n",
      "45.00123 , -93.26664\n",
      "42.09593024 , -72.58681881\n",
      "41.66900774 , -73.98039447\n",
      "29.7629 , -95.3832\n",
      "30.26851 , -97.72559\n",
      "33.9632999 , -118.00067\n",
      "29.57709615 , -95.64366817\n",
      "29.685 , -95.411\n",
      "42.36415316 , -71.10178308\n",
      "30.428101 , -81.663811\n",
      "29.68472222 , -95.41083333\n",
      "35.3524676 , -80.68549036\n",
      "40.86086 , -73.42157\n",
      "25.683611 , -100.288056\n",
      "38.8991 , -77.029\n",
      "38.8991 , -77.029\n",
      "38.8991 , -77.029\n",
      "38.8991 , -77.029\n",
      "40.0 , -100.0\n",
      "39.0131121 , -78.77551672\n",
      "29.7811 , -95.5395\n",
      "40.4203 , -3.7058\n",
      "42.709549 , -89.0111008\n",
      "29.75502565 , -95.3663275\n",
      "35.22583333 , -80.85277778\n",
      "41.852653 , -87.624387\n",
      "29.64555556 , -95.27888889\n",
      "29.7629 , -95.3832\n",
      "33.14865754 , -96.86310404\n",
      "35.5740236 , -78.74957853\n",
      "29.7629 , -95.3832\n",
      "29.75507615 , -95.36634843\n",
      "43.07360928 , -70.77941937\n",
      "43.067 , -70.7728\n",
      "33.4931 , -111.926\n",
      "33.4931 , -111.926\n",
      "25.6770299 , -100.29\n",
      "37.0872 , -76.473\n",
      "33.64049111 , -84.43493499\n",
      "40.7142 , -74.0064\n",
      "39.9567104 , -104.9843203\n"
     ]
    }
   ],
   "source": [
    "class MyListener(StreamListener):\n",
    "    def __init__(self, time_limit=30):\n",
    "        self.start_time = time.time()\n",
    "        self.limit = time_limit\n",
    "        super(MyListener, self).__init__()\n",
    "    \n",
    "    def on_data(self, data):\n",
    "        if (time.time() - self.start_time) < self.limit:\n",
    "            data = json.loads(data)\n",
    "            if 'coordinates' in data and data['coordinates']:\n",
    "                longitude, latitude = data['coordinates']['coordinates']\n",
    "                if latitude > bbox[0] and latitude < bbox[1] and longitude > bbox[2] and longitude < -bbox[3]:\n",
    "                    lons.append(longitude)\n",
    "                    lats.append(latitude)\n",
    "#                    print latitude, \",\", longitude\n",
    "            return True\n",
    "        else:\n",
    "            return False\n",
    "\n",
    "    def on_error(self, status):\n",
    "        print(status)\n",
    "        \n",
    "auth = OAuthHandler(C_KEY,C_SECRET)\n",
    "auth.set_access_token(A_TOKEN_KEY,A_TOKEN_SECRET)\n",
    "myStream = Stream(auth, MyListener(time_limit=600))\n",
    "myStream.filter(track=[ 'superbowl', 'super bowl', 'football'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\nQmCC\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0xa131240>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from mpl_toolkits.basemap import Basemap\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "\n",
    "map = Basemap(llcrnrlon=bbox[2], llcrnrlat=bbox[0], urcrnrlon=bbox[3],urcrnrlat=bbox[1], \n",
    "              projection='lcc', lat_1=33, lon_0=-95, resolution='i', area_thresh=10000)             \n",
    "map.drawcoastlines()\n",
    "map.drawcountries()\n",
    "#map.drawstates()\n",
    "(x,y) = map(lons,lats)       \n",
    "map.scatter(x, y, marker='D',color='r')   # plot the points\n",
    "plt.draw()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [default]",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
