# First attempts at creating a python backend for Follo app
# Initial API calls to all necessary endpoints
# Stashed into dicts with names that are relevant to each call


from urllib import urlopen # keepin it lightweight for now
#from collections import OrderedDict
import json

insta_api = 'https://api.instagram.com/v1/'
# Will need to replace with Oauth functionality later
access_token = 'access_token=2774536779.2eed6a9.b924cdf64bde4b5b928e802e6dabbbf7'
#======Users=======#
self_endpt = 'users/self/?'
user_endpt = 'users/%r/?'
self_recent_endpt = 'users/self/media/recent/?' # needs parameters to be included later (count, min_id, max_id)
user_recent_endpt = 'users/%r/media/recent/?'
self_liked_endpt = 'users/self/media/liked?' #needs params TBI (count, max_like_id)
# users_search
#==Relationships===#
following_endpt = 'users/self/follows?'
followers_endpt = 'users/self/followed-by?'
requested_by_endpt = 'users/self/requested-by?'
relationship_endpt = 'users/%r/relationship/?'
#======Media=======#
media_endpt = 'media/%r?'
shortcode_endpt = 'media/shortcode/%r/?'
# media_search
#=====Comments=====#
comments_endpt = 'media/%r/comments/?'


#======Likes=======#
likes_endpt = 'media/%r/likes?'


#=======Tags=======#
tags_endpt = 'tags/%s/?'
recent_tags_endpt = 'tags/%s/media/recent?'
# tag_search
#=====Locations====#
#location_ids will need to be looked up separately
locs_endpt = 'locations/%r?'
recent_locs_endpt = 'locations/%r/media/recent?'
# location_search
#------------------#


def get_simple(endpoint):
    response = json.loads(urlopen(insta_api + endpoint
                                  + access_token).read())
        # creates dict containing API response
    return response

def get_user(endpoint, user_id=None):
    followers = get_simple(followers_endpt)['data']
    followers_raw = {}
    for i in range(len(followers)):
        followers_raw["%s" % followers[i]['username']] = followers[i]['id']
    
    
    response = json.loads(urlopen(insta_api
                                  + endpoint % user_ids[0]
                                  + access_token).read())



silf = get_simple(followers_endpt)['data']
print silf
#i = 0
#while i < 2:
#    print silf[i]['id']
#    i += 1
followers_raw = {}
rilf = get_simple(self_recent_endpt)['data']
recent = {}
for i in range(len(rilf)):
    rilfa = rilf[i]['id']
    rilfb = {"thumbnail_url": rilf[i]['images']['thumbnail']['url']}
    recent["%s" % rilfa] = rilfb
for i in range(len(silf)):
    silfa = silf[i]['id']
    silfb = {"name": silf[i]['full_name']}
    silfb["user"] = silf[i]['username']
    silfb["pic"] = silf[i]['profile_picture']
    followers_raw["%s" % silfa] = silfb
print followers_raw
print recent
