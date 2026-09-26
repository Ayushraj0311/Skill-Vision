"""
Step : 4
"""

from youtube_transcript_api import YouTubeTranscriptApi
from Templete import Other_To_English_Templete
from LLMs_Model import model


def AutoEnglishTranscript(video_id):

    language = ["en", "hi"]

    ytt_api = YouTubeTranscriptApi()

    for lang in language:
        try:
            FetchedTranscript = ytt_api.fetch(
                video_id = video_id,
                languages = [lang]
            )

            script_paragraph = [paragraph for paragraph in FetchedTranscript.split('.')]

            if lang is not "en":

                for paragraph in script_paragraph:
                    TranslatePrompt = Other_To_English_Templete.invoke({paragraph})
                    en_translated = model.BaseModel.invoke(TranslatePrompt)

                
            return FetchedTranscript
        
        except:
            print("Transcript not found for Language : ", lang, "\n")
