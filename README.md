# ChatGPT_history_parser
Strips the conversations.json file down to a reasonable size so you can chat with chatgpt about the content

This script is designed to parse a JSON file containing conversation data and extract meaningful information from it. The script performs the following steps:

1. Load the JSON file containing the chat history.
2. Process the chat history to include speaker information, filtering out system messages unless they are marked as user system messages.
3. Change the speaker's name from "assistant" to "ChatGPT" and handle custom user info for system messages.
4. Create a new JSON structure with the conversations and speaker information.
5. Save the new structure to a new JSON file.

To use this script, you need to:
- Replace the `file_path` variable with the path to your JSON file containing the conversation data.
- Run the script to generate a new JSON file with the extracted conversation and speaker information.

The output JSON file will be saved to the path specified in `new_file_path_with_speaker`.

Go from this: 

<img src="https://github.com/DanPace725/ChatGPT_history_parser/blob/main/Better1.png" alt="Alt text" width="500" height="500">


To this: 

<img src="https://github.com/DanPace725/ChatGPT_history_parser/blob/main/Better2.png" alt="Alt text" width="500" height="500">
