from langchain_core.prompts import ChatPromptTemplate

# all chunk summarization
reduce_prompt = ChatPromptTemplate.from_template(
    """
    You are creating the final summary of a YouTube video.

    Below are summaries generated from different sections of the same video.

    Combine them into one coherent summary.

    Requirements:
    - Remove repetition
    - Preserve important technical concepts
    - Maintain the logical flow of the video
    - Do not introduce information that wasn't present
    - Make the summary easy to understand

    Section summaries:

    {summaries}
    """
)
