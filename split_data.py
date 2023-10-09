import os


def split_data(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Create a folder with the name of the file (without extension)
    folder_name = os.path.splitext(os.path.basename(input_file))[0]
    os.makedirs(folder_name, exist_ok=True)

    current_data = []
    current_count = 1

    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue

        # Split the line by ":"
        parts = line.split(':')
        data_part = parts[0].strip()

        # Check if it's a new set of data
        if len(data_part.split()) != current_count:
            # Save the current data to a new file
            save_data_to_file(current_data, folder_name, current_count)

            # Reset for the new set of data
            current_data = []
            current_count = len(data_part.split())

        current_data.append(line)

    # Save the last set of data
    save_data_to_file(current_data, folder_name, current_count)


def save_data_to_file(data, folder_name, count):
    # Create a new file for the set of data
    file_name = f"{folder_name}_count_{count}.txt"
    with open(os.path.join(folder_name, file_name), 'w') as file:
        file.write('\n'.join(data))


if __name__ == "__main__":
    # Get all .txt files in the current directory
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.txt')]

    for file in files:
        split_data(file)
