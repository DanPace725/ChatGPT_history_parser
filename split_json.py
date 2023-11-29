import ijson
import os
import simplejson as json

def split_json_file(input_file, output_dir, max_size_mb=10):
    """
    Split a JSON file into multiple smaller files based on a specified maximum size.

    Args:
        input_file (str): The path to the input JSON file.
        output_dir (str): The directory where the split JSON files will be saved.
        max_size_mb (int, optional): The maximum size in megabytes for each split file. Defaults to 10.

    Raises:
        FileNotFoundError: If the output directory does not exist.

    Returns:
        None
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'rb') as file:
        file_count = 1
        current_size = 0
        current_data = []

        for item in ijson.items(file, 'item'):
            json_str = json.dumps(item)
            item_size = len(json_str.encode('utf-8'))

            if current_size + item_size > max_size_mb * 1024 * 1024:
                output_file = os.path.join(output_dir, f'split_{file_count}.json')
                with open(output_file, 'w') as out_file:
                    json.dump(current_data, out_file)

                file_count += 1
                current_size = 0
                current_data = []

            current_data.append(item)
            current_size += item_size

        if current_data:
            output_file = os.path.join(output_dir, f'split_{file_count}.json')
            with open(output_file, 'w') as out_file:
                json.dump(current_data, out_file)

# Usage
input_file = '11.28.23\conversations.json'
output_dir = 'split_json'
split_json_file(input_file, output_dir)
