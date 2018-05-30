#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
from collections import Counter


api = InstagramAPI("Cthulzilla", "Drama8Bank@Disability")
# if (api.login()):
#     api.getSelfUserFeed()  # get self user feed
#     print(api.LastJson)  # print last response JSON
#     print("Login success!")
# else:
#     print("Can't login!")

allPostLikers = []
uniqueLikers  = []
postsToLike = []

if (api.login()):
    api.getSelfUserFeed()
    myPosts = api.LastJson
    for postNum in range(len(myPosts['items'])):
        api.getMediaLikers(myPosts['items'][postNum]['pk'])
        myPostLikers = api.LastJson
        for likerNum in range(len(myPostLikers['users'])):
            allPostLikers.append(myPostLikers['users'][likerNum]['pk'])
    uniqueLikers = Counter(allPostLikers).most_common()
    for aLiker in uniqueLikers:
        api.getUserFeed(aLiker[0])
        numLiked = aLiker[1]
        userPosts = api.LastJson
        while numLiked > 0:
            if "items" in userPosts:
                numLiked -= 1
                if len(userPosts['items']) > 0:
                    postsToLike.append(userPosts['items'].pop(0)['pk'])
            else:
                break
    # postsToLike

else:
    print("Can't login!")


