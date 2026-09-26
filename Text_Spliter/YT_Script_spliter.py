from langchain_text_splitters import RecursiveCharacterTextSplitter

text_spliter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)