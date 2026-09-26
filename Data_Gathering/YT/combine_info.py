"""
STEP : 2
"""

# Creating the list of URL, Title, channel
from .URL_List import URLS_LIST
import requests



def Combine_INFO(query):

    if __name__ == "Data_Gathering.YT.combine_info":
    
        print("""----------------------------------
        Entered : Data_Gather.YT.combine_info.py
        --------------------------------------""")

        video_urls = URLS_LIST(query)

        urls_data = []

        for url in video_urls:

            yt_data = requests.get(f"https://www.youtube.com/oembed?url={url}&format=json").json()

            video_url = url
            video_title = yt_data["title"]
            video_channel = yt_data["author_name"]

            urls_data.append({"video_url":url, "video_title":video_title, "channel":video_channel})

        print("Printing Data : ")

        for i in urls_data:
            print(i)

        
        print("""----------------------------------
        Exit : Data_Gather.YT.combine_info.py
        --------------------------------------""")
        
        return urls_data

    else:
        print("Execute -> main.py not this file")