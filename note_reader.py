def get_notes(file_list, makam=None):
    all_notes = []
    for file_path in file_list:
        if makam and makam + "--" not in file_path:
            continue

        with open(file_path, "r") as in_file:
            lines = in_file.readlines()
            notes = []
            for line in lines:
                tokens = line.split("\t")
                if tokens[1] in ["1", "4", "7", "8", "9", "10", "11", "12", "23", "24", "28", "44"]:
                    notes.append(tokens[3])
            all_notes.append(notes)

    return all_notes
