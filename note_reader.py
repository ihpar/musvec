from collections import Counter

note_line_codes = ["1", "4", "7", "8", "9",
                   "10", "11", "12", "23", "24", "28", "44"]


def get_notes(file_list, as_pitch_classes=False, return_counts=False, makam=None):
    all_notes = []
    counts = Counter()

    for file_path in file_list:
        if makam and makam + "--" not in file_path:
            continue

        with open(file_path, "r") as in_file:
            lines = in_file.readlines()
            notes = []
            for line in lines:
                tokens = line.split("\t")
                if tokens[1] in note_line_codes:
                    note = tokens[3]
                    if note == "Es":
                        continue
                    if as_pitch_classes and note[1].isdigit():
                        pitch_class = note[0] + note[2:]
                        notes.append(pitch_class)
                    else:
                        notes.append(note)
            all_notes.append(notes)
            counts.update(notes)

    if return_counts:
        return all_notes, counts

    return all_notes
