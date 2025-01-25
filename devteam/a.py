import asyncio
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import MagenticOneGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.agents.web_surfer import MultimodalWebSurfer
from autogen_ext.agents.magentic_one import MagenticOneCoderAgent

# tracemalloc.start()

async def main() -> None:
    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", api_key="")

    surfer = MultimodalWebSurfer(
        "WebSurfer",
        model_client=model_client,
    )
    coder = MagenticOneCoderAgent(
        "Coder",
        model_client=model_client
    )
    team = MagenticOneGroupChat([coder], model_client=model_client)

    task = "Create a simple program in Java and will print Hello World"

    await Console(team.run_stream(task=task))

asyncio.run(main())