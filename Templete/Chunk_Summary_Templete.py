from langchain_core.prompts import PromptTemplate

chunk_summary_templete = PromptTemplate(
    template= """
You are summarizing a YouTube video transcript.

Summarize the following section clearly and concisely.

Focus on:
- Main ideas
- Important concepts
- Technical concepts
- Examples
- Important conclusions
- Skill

Do not add information that is not present in the transcript.

Chunk_Content:
{Chunk_Content}
""",
input_variables= ["chunk_Content"]
)
