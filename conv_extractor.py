# conv_extractor.py
import json
import os

def process_chat_history(file_path, output_file_path):
    """
    Extracts conversations with speakers from a chat history file and saves them to a new JSON file.

    Parameters:
        file_path (str): The path to the chat history file.
        output_file_path (str): The path to save the extracted conversations.

    Returns:
        None
    """
    with open(file_path, 'r') as file:
        chat_history = json.load(file)

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

    # Save the new structure to a new JSON file
    with open(output_file_path, 'w') as new_file:
        json.dump(extracted_conversations_with_speaker, new_file, indent=4)

def process_all_files(input_dir, output_dir):
    """
    Process all files in the given input directory and save the processed files
    in the specified output directory.

    Parameters:
    - input_dir (str): The path to the directory containing the input files.
    - output_dir (str): The path to the directory where the processed files will be saved.

    Returns:
    - None
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.json'):
            input_file_path = os.path.join(input_dir, filename)
            output_file_path = os.path.join(output_dir, f'processed_{filename}')
            process_chat_history(input_file_path, output_file_path)

# Usage
split_output_dir = 'split_json'  # Directory where split_json.py saves its output
processed_output_dir = 'processed_json'  # New directory for processed files
process_all_files(split_output_dir, processed_output_dir)