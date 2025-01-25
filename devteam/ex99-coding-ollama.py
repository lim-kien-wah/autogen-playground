import asyncio
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.teams.magentic_one import MagenticOne
from autogen_agentchat.ui import Console
from autogen_agentchat.teams import MagenticOneGroupChat
from autogen_ext.agents.web_surfer import MultimodalWebSurfer
from autogen_ext.agents.magentic_one import MagenticOneCoderAgent

def get_coder_model_client() -> OpenAIChatCompletionClient:  # type: ignore
    "Mimic OpenAI API using Local LLM Server."
    return OpenAIChatCompletionClient(
        # model="llama3.2:1b",
        model="ollama/deepseek-coder-v2:latest",
        api_key="NotRequiredSinceWeAreLocal",
        base_url="http://0.0.0.0:4000",
        model_info={
            "json_output": False,
            "vision": False,
            "function_calling": True,
        },
    )

def get_llm_model_client() -> OpenAIChatCompletionClient:  # type: ignore
    return OpenAIChatCompletionClient(model="gpt-4o-mini")


async def main():

    surfer = MultimodalWebSurfer(
        "WebSurfer",
        model_client=get_llm_model_client()
    )

    coder = MagenticOneCoderAgent(
        "Coder",
        model_client=get_coder_model_client()
    )
    team = MagenticOneGroupChat([surfer, coder], model_client=get_llm_model_client())
    task = "Write a Java Hello World program."
    result = await Console(team.run_stream(task=task))
    print(result)

if __name__ == "__main__":
    asyncio.run(main())