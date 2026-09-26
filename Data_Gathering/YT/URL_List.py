"""
STEP : 1
"""

# gather list of URLs

import yt_dlp

def URLS_LIST(query):

    if __name__ == "Data_Gathering.YT.URL_List":

        print("""----------------------------------
        Entered : Data_Gather.YT.URL_List.py
        --------------------------------------""")
        # query = "machine learning roadmap"

        options = {
            "quiet": True,
            "extract_flat": True,
            "skip_download": True,
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            results = ydl.extract_info(
                f"ytsearch10:{query}",
                download=False
            )

        video_urls = [
            f"https://www.youtube.com/watch?v={entry['id']}"
            for entry in results["entries"]
            if entry.get("id")
        ]

        print("Printing Data : ")

        for i in video_urls:
            print(i)

        
        print("""----------------------------------
        Exiting : Data_Gather.YT.URL_List.py
        --------------------------------------""")

        return video_urls

    else:
        print("Execute -> main.py not this file")


