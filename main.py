from Data_Gathering.YT.URL_List import URLS_LIST
from Data_Gathering.YT.combine_info import Combine_INFO
from Data_Gathering.YT.Fetch_Script import Create_Transcript


if __name__ == "__main__":
    query = "machine learning roadmap"

    Create_Transcript(query=query)

    