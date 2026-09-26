from langchain_ollama import ChatOllama
from Schema.Schema import JD_Skill_Schema, Chunk_Summary_Schema

BaseModel = ChatOllama(
    model="qwen3:8b"
)

embeding_model = ChatOllama(
    model="qwen3-embedding:4b"
)

skill_structured_model = BaseModel.with_structured_output(schema=JD_Skill_Schema)

chunk_summary_structured_model = BaseModel.with_structured_output(schema=Chunk_Summary_Schema)