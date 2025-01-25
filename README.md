## Folder structure
.autogenstudio - appdir for autogen studio
myautogen - Python virtual environment for AutoGen Studio

## Instruction
To start autogen studio:
1. Activate Python virtual environment
` source myautogen/bin/activate
1. Run autogenstudio command
` autogenstudio ui --port 8081 --appdir .autogenstudio
1. Open browser and navigate to http://localhost:8081
1. WHen done, run deactivate to end Python virtual environment


OpenAI Configuration
Project - autogen
OPENAI_API_KEY=
Allowed model - gpt-4o, gpt-4