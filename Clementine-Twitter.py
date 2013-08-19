#!/usr/bin/env python

from dbus import Bus, DBusException
import tweepy

bus = Bus(Bus.TYPE_SESSION)

consumer_key		= "IvbTe3U1IL2QELEtH9xJQ" #your consumer key
consumer_secret		= "bFG3ZvKznVRyPmM96wG6cjtDLGV6ERZoVBBOhv8W9M" #your consumer secret
access_token		= "395428377-NMg3CEaF3on02pUyoMuIDGR3g5RFDQotdFEr93V2" #your acces token
access_token_secret	= "6RnB4nEn7J3jjHMwFBBpGd1tzh2PHPkhlVjPphFSb8" #your access token secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_clem():
  try:
    return bus.get_object('org.mpris.clementine', '/Player')
  except DBusException:
    print "\x02Either Clementine is not running or you have something wrong with your D-Bus setup."
    return None

def get_metadata():
  clem = get_clem()
  
  if clem:
    clemp = bus.get_object('org.mpris.clementine', '/Player')
    clemmd = clemp.GetMetadata()

    clem

    
    try:
      title = clemmd['title']

    except DBusException:
      print "\x02Can't extract information. File might be insufficently tagged."
      return None

    output = "#NowPlaying " + unicode(title).encode('utf-8') + " #Clementine"

    return output

api.update_status(get_metadata())
