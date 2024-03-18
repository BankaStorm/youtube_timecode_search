#CREATED BY https://github.com/BankaStorm/youtube_timecode_search

#But you can use this code anywhere because it is simple)

def find_time_codes_with_word(file_path, target_word):
    try:
        # Opens a file for reading
        with open(file_path, 'r', encoding='utf-8') as file:
            # Reading lines from a file
            lines = file.readlines()

            # Initialize a variable to store time codes and word counter
            time_codes = []
            word_count = 0

            # Iterate over the rows and check the conditions
            for line_num, line in enumerate(lines):
                # Checking if the string contains the target word
                words_in_line = line.lower().split()
                if target_word.lower() in words_in_line:
                    # remember the time code (assuming it is in the previous line)
                    if line_num > 0:
                        time_code = lines[line_num - 1].strip()
                        time_codes.append(time_code)
                        word_count += words_in_line.count(target_word.lower())

            # If time codes are found, display them separated by a space
            if time_codes:
                print(f'\nTotal words found "{target_word}": {word_count}')
                print(f'Words found "{target_word}" in the following time codes:')
                for time_code in time_codes:
                    print(f'{time_code}', end=' ')
                print(f' ')
            else:
                print(f'Words "{target_word}" not found.')

    except FileNotFoundError:
        print(f'File named {file_path} not found.')
    
    except Exception as e:
        print(f'An error has occurred: {e}')

if __name__ == "__main__":
    # Prompts the user to select a .txt file
    file_path = input('Enter the path to the file (.txt): ')

    # Prompts the user to enter the target word
    target_word = input('Enter a search word: ')

    # Calling a function to search for time codes with the target word
    find_time_codes_with_word(file_path, target_word)
