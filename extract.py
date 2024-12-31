import pandas as pd
import requests
import json
#scrapping videos IDs
def getvidIDs(channelID):
    
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/channel/videos"
    querystring = {"channelId":channelID,"type":"videos","sortBy":"newest"}
    headers = {
        "x-rapidapi-key": "d07e27c2a7msh53f183883e90347p181523jsnce2644b80022",
        "x-rapidapi-host": "youtube-media-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    textTojson = json.loads(response.text)
    vidIDs = {i['id']: i['title'] for i in textTojson['items']}
    return vidIDs

#scrapping videos data
def getvidData(vidID):
    comments = []
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/comments"

    querystring = {"videoId":vidID,"sortBy":"top"}

    headers = {
        "x-rapidapi-key": "d07e27c2a7msh53f183883e90347p181523jsnce2644b80022",
        "x-rapidapi-host": "youtube-media-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    textTojson = json.loads(response.text)
    for i in textTojson['items']:
        comments.append(i['contentText'])
    return comments

#getting comments

def df_making(res):
    final_dict = {}
    for i in res.keys():
        com = getvidData(i)
        final_dict[i]=com
    rows = []
    for key, values in final_dict.items():
        for value in values:
            rows.append({'id': key, 'comment': value})

    data = pd.DataFrame.from_dict(rows)
    return data