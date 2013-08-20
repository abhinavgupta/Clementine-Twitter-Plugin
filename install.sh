echo "Installing ClemTweet App...."
echo "Make sure you have entered your consumer and access tokens in the ClemTweetScript file under the Scripts folder"
sudo mkdir /usr/share/icons/ClemTweet
sudo cp twitter_music.jpg /usr/share/icons/ClemTweet
pip install -r requirements.txt --no-index --find-links file:///tmp/packages
sudo python setup.py install

