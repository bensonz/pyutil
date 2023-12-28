import sys
import json

contains = ["apiKey", "path", "assistant"]


def prune_config(file_path: str):
    """
    prune a config file. Let's say the file is config.json
    it will remove all values of the keys that has "apiKey", or path.
    and then output the result to config.sample.json, in the same directory
    """
    with open(file_path, 'r') as f:
        config = json.load(f)
    for key in config:
        if any([c in key for c in contains]):
            config[key] = ""
    with open(file_path.replace(".json", ".sample.json"), 'w') as f:
        json.dump(config, f, indent=2, sort_keys=False, ensure_ascii=False)
    return


def main():
    """
    prune a config file. Let's say the file is config.json
    it will remove all values of the keys that has "apiKey", or path.
    and then output the result to config.sample.json, in the same directory
    """
    args = sys.argv[1:]
    if len(args) == 0:
        print("Please provide a file path.")
        return
    file_path = args[0]
    prune_config(file_path)

    return


if __name__ == '__main__':
    main()
