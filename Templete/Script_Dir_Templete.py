from langchain_core.prompts import PromptTemplate
from Data_Gathering.YT.URL_List import query

script_dir_templete = PromptTemplate(
    template="""
    for the provided Query, return the directory name like

    example :
    1. query = "machine learning roadmap", output = "Machine Learning"\n\n

    Query = {query}
""",
input_variables= ["query"]
)