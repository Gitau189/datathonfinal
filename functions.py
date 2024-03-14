def getExtension(filename):
    filename_list = filename.split('.')
    ext_index = len(filename_list) - 1
    return ('.' + filename_list[ext_index])