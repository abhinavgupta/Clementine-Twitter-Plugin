from dbus import Bus, DBusException
import tweepy

bus = Bus(Bus.TYPE_SESSION)

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

    try:
      artist = clemmd['artist']
    except KeyError:
    	artist = ''
    
    try:
      album = clemmd['album']
    except KeyError:
    	album = ''
    	
    try:
      title = clemmd['title']
    except KeyError:
    	title = ''
    	
    if all(attributes is '' for attributes in [artist,album,title]):
    	return "#NowPlaying A song with no metadata. Whatae Joke"

    output = "#NowPlaying " + unicode(title).encode('utf-8') + " - " + unicode(artist).encode('utf-8') + " #Clementine"

    return output



