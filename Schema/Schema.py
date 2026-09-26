from pydantic import BaseModel, Field
from typing import Annotated, List

class JD_Skill_Schema(BaseModel):
    technical_skill : Annotated[List[str], Field(description="list of skill which can be present in a resume, from the given resume content list")]
    # non_technical_skill : Annotated[List[str], Field(description="list of keyword can't be count in skill, from the given resume content list")]
    
class Chunk_Summary_Schema(BaseModel):
    summary : Annotated[str, Field(description="chunk summary of YouTube Video Scripts")]
    skill : Annotated[List[str], Field(description="list of skill or job role which is discussed in the chunk")]
    