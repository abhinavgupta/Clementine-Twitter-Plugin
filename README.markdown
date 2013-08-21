# Clementine Twitter Plugin

A Simple Python Script to tweet your current playing song as a #NowPlaying tweet


## Requirements

	1. python-tweepy
	2. python-dbus
	3. python-setuptools
	4. pip
	
## License
	Apache License V2

## Installation

	Make sure you have "curl" and "pip" package. To install pip:

		$ curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
		$ [sudo] python get-pip.py	
	
	Before installing the application, make sure you get your consumer and access tokens and secret.
	To do that, you need to register you application on https://dev.twitter.com/apps/new
	After getting the 4 tokens, put them in the ClemTweetScript file placed in the Script folder.
	They are mentioned by the comment #consumer_token etc.

	ONLY AFTER FOLLOWING THE STEP ABOVE PROCEED TO INSTALL THE APPLICATION

	To install all the dependencies and the application itself, do this:
	
		$ sudo install.sh
	
	This will install the application and you can see the application icon in the folder.


## Script Usage
	
	To use this application from the command line:
		
		$ ClemTweetScript

## Using the package

	To use it in a python script, it will give only metadata, you need to work on the Tweeting script:

		from ClemTweet import get_metadata
		tweet = get_metadata()

	Then you can use your own script to tweet it accordingly

## Using the Desktop Application
	
	Okay, it sucks. But everytime you feel like tweeting your current song, just click on the icon. 
	It will tweet your current playing song.
	

## TODO
	1. Add more tags from metadata
	2. Handle exceptions for metadeta absence
	3. Create Firefox/Ubuntu Plugin
	4. Integrate with Clementine 
	5. More features


