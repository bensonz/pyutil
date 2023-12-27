import sys


def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print("File not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Please provide a file path.")
        return
    file_path = args[0]
    word_count = count_words_in_file(file_path)
    print(f"The file contains {word_count} words.")


if __name__ == "__main__":
    main()
