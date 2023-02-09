#####
#
#   Import Statements
#
#   You probably need to import some python modules - you should put them here at the top
#
import sys, json, csv, time, datetime
#
#   import the command line argument parsing object
#
from mele.classes.utilities.Args import Args
#
#   import the objects needed to access user timelines from twit
#
from mele.twit.support import *
from mele.twit.Authorizer import Authorizer
from mele.twit.UserTimeline import UserTimeline
#
#   Here YOU need to add the import statements to access Mongo DB 
#




#####
#
#   CONSTANTS
#
#   Constants are just like variables - but they do not need to change, they are constant
#
#   As a convention we use ALL_CAPS_NAMES to help remember that something is a constant
#

#
#   We need some constants for to Authorize() the UserTimeline() object
#   
#   You'll need to set your own twitter user name (or handle) or this won't work
#
TWITTER_APP = "HCDE530Test01"
TWITTER_USER = "rohanpaldesign"


#
#   The name of the collection that you want to use in the Mongo DB for storing the tweets
#   This is a constant - we need to access the same collection each time.
#
COLLECTION_NAME = "senate_collection"


#
#   The name of the congressional chamber you decide to collect, either the 'senate' or the
#   'house' - you need to pick something so you can track where each person works
#
CHAMBER_HOUSE = "house"
CHAMBER_SENATE = "senate"
# 
#   You should pick one of these - just uncomment the line for the one you want to collect
#   You still need to make sure you're using the right CSV file or the data will be inconsistent
#
CONGRESSIONAL_CHAMBER = "<undefined>"
CONGRESSIONAL_CHAMBER = CHAMBER_SENATE
CONGRESSIONAL_CHAMBER = CHAMBER_HOUSE


#
#   There are congress members who do not have an official twitter account. These have 'no_official'
#   in the field for the user account (handle). They should be skipped for now. The main() for loop
#   has an if conditional check and skips people with this as the twitter handle
#
MISSING_ACCOUNT = "no_official"


#
#   The collection loop should pause or sleep, just a little, between each collection cycle.
#   This is just to be considerate of the remote servers and the free data they are providing.
#   This also makes sure you do not exceed the rate limits for the UserTimeline() request
#
TIMELINE_SLEEP_DURATION = 1.0
LOOP_SLEEP_DURATION = 5.0


#
#   The user timeline request will allow you to request a maximum of 200 tweets in each 
#   request. That is, if there are 200 tweets available it would try to return 200.
#   You should set your UserTimeline object to always request the maximum number of tweets
#   so that you make *fewer* total requests to get all of a user's timeline
#
MAX_TIMELINE_COUNT = 200


#
#   This is to make sure we don't get caught in an endless loop of timeline requests -- if
#   something goes wrong. You can only get 3200 tweets for each user, so if you request 200
#   tweets (the MAX_TIMELINE_COUNT) each time you should only need 16 requests. This is set 
#   a little higher.
#
MAX_TIMELINE_REQUESTS = 25
#
#   When testing your program you might just want to make a small number of timeline requests
#   This low number will terminate the request loop early, before you've likely gotten a
#   whole timeline. Uncomment the line to make fewer requests - for TESTING only!
#
#MAX_TIMELINE_REQUESTS = 3


#
#   Database settings should be a constant - We want to work with the same database each time
#
DATABASE_SETTINGS = {
#
#   Your database settings as a python dictionary go here  You could probably copy and paste 
#   from an example you saw in class. You may need to change some values in some fields.
#
}



#STEP 02 =====================================================================================================


#WORKING
def load_text_csv(filename=None):
    congress_members = list()
    #
    #   The list of senators or house members is in a CSV (comma separated values) file. 
    #
    #   You need to:
    #       open the CSV file
    #       read each CSV row 
    #       add the resulting information to the list of congress members
    #       close the file
    #       return the congress members
    data = open(filename, "r")
    reader = csv.DictReader(data)
    for row in reader:
        congress_members.append(row)
    return congress_members # this line should return a list of dictionaries.


#STEP 03 =======================================================================================================


def make_timeline_request(requester=None, max_id=0):
    tweets = list()
    #
    #   You need to:
    #       set the max_id of the request 
    #       make the request
    #       get the response
    #       return the response
    max_id = max_id
    
    
    #
    return tweets # this line should return a list of tweets, dictionaries, 


