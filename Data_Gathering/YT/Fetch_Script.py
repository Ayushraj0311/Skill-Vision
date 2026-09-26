"""
STEP : 3
"""

from .LanguageProblemSolved import AutoEnglishTranscript
from youtube_transcript_api import YouTubeTranscriptApi
from Templete import Other_To_English_Templete
from .combine_info import Combine_INFO
from LLMs_Model import model
import os
import re

def Create_Transcript(query):

    if __name__ == "Data_Gathering.YT.Fetch_Script":

        print("pwd : ",os.getcwd())
        
        print("""----------------------------------
        Entered : Data_Gather.YT.Fetch_Script.py
        --------------------------------------""")

        count = 0
        urls_data = Combine_INFO(query)
        # print("urls data 3: ", urls_data)
        # url_data = ["https://www.youtube.com/watch?v=8WzSEikpHk8", ]

        ytt_api = YouTubeTranscriptApi()

        print("Status -> Invoking the model ")
        # folder_name = model.BaseModel.invoke(query)

        folder_name = "ML"
        folder_path = "D:\\deployed Project\\RAG SKILL GAP\\Data_Gathering\\YT\\Chunked_Transcript_Text"

        dir_list = [item for item in os.listdir(folder_path)]

        print("Status -> checking Field Folder exit or not")
        if folder_name in dir_list:
            print("field folder already exit \n\n")
            return

        print("creating field folder  \n\n")

        folder = os.path.join(folder_path, folder_name)
        os.mkdir(folder)

        running_count = 1
        Alphabet_series = 65

        for url in urls_data:

            print("url : ", url, "\n")

            if running_count > 11:
                break

            count += 1
            print("working on file : ", count)

            video_id = re.sub(r"\S+?v=", "", url["video_url"]).split("&")[0]

            # Language problem solve

            # FetchedTranscript = AutoEnglishTranscript(video_id)

            try:
                print("url inside try: ", url )
                FetchedTranscript = ytt_api.fetch(
                        video_id = video_id,
                        languages = ["en", "hi"]
                    )

                if FetchedTranscript:

                    print("\n-----------------------------\n\nFetched Transcript data : ", FetchedTranscript,"\n\n-----------------------------")

                    current_path = os.path.join(folder_path, folder_name)

                    file_name = f'{count}_{chr(Alphabet_series)}'
                    
                    current_path = os.path.join(current_path, file_name)
                    
                    transcriptData = "".join(snippet.text for snippet in FetchedTranscript)

                    try:
                        print("\n inside writting : TRY")
                        with open(current_path, "w", encoding="utf-8") as file:
                            file.write(str(transcriptData))
                            print("file created successfully")
                    except Exception as e:
                        print("\n inside writting except")
                        print(f"{count} faild to write the transcript in file : ", e)

                    running_count += 1
                    Alphabet_series += 1

                else:
                    print("\n\nFeteched Transcript is empty \n\n")
                
            except Exception as e:
                # raise Exception("Transcript Language is not supported")
                print("--------------------excuted except ------------------------------")
                print(f"Faild {count}", e)
            
            # current_path = os.getcwd() + "\\Data_Gathering\\YT\\Transcript_Text"
            
            

        
        print("""----------------------------------
        Exit : Data_Gather.YT.Fetch_Script.py
        --------------------------------------""")

        return

    else:
        print("Execute -> main.py not this file")