# Let's start by loading the JSON file to understand its structure
import json

# Load the JSON file
file_path = '11.28.23/conversations.json'

with open(file_path, 'r') as file:
    chat_history = json.load(file)


# Process the chat history again to include speaker information
extracted_conversations_with_speaker = []

for conversation in chat_history:
    # Start from the current node and traverse backwards
    current_node = conversation.get('current_node')
    while current_node:
        node = conversation.get('mapping', {}).get(current_node)
        if node:
            message = node.get('message')
            if message:
                content = message.get('content', {}).get('parts', [])
                speaker = message.get('author', {}).get('role')
                is_user_system_message = message.get('metadata', {}).get('is_user_system_message', False)
                # Filter out system messages unless they are marked as user system messages
                if content and speaker and (speaker != "system" or is_user_system_message):
                    # Change the speaker's name from "assistant" to "ChatGPT"
                    if speaker == "assistant":
                        speaker = "ChatGPT"
                    # Handle the custom user info case for system messages
                    elif speaker == "system" and is_user_system_message:
                        speaker = "Custom user info"
                    # Include both the content and the speaker in the extracted data
                    for part in content:
                        extracted_conversations_with_speaker.insert(0, {"speaker": speaker, "content": part})
            current_node = node.get('parent')

# Create a new JSON structure with conversations and speaker information
new_json_structure_with_speaker = {"conversations": extracted_conversations_with_speaker}

# Save the new structure to a new JSON file
new_file_path_with_speaker = '11.28.23/extracted_chat_history_with_speaker2.json'
with open(new_file_path_with_speaker, 'w') as new_file:
    json.dump(new_json_structure_with_speaker, new_file, indent=4)


