def import_file(file_name):
    file = open(file_name, "r", encoding="utf-8")
    file_text = file.read()
    file.close()
    return file_text
