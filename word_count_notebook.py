import io
import os
import json

while(True):
    name = input("Jupyter file name WITHOUT extension\n")
    extension = ".ipynb"
    fname = name + extension
    pname = os.path.dirname(__file__) + "\\" + fname
    print(pname)

    f = open(pname, "r")
    json_file = json.load(f)

    word_count = 0
    for cell in json_file["cells"]:
        if cell["cell_type"] == "markdown":
            for line in cell["source"]:
                word_count += len(line.replace("#", "").lstrip().split(" "))
    print(f"Number of words: {word_count}\n\n")