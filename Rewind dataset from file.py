mlist = []
with open("dataset_24465_4.txt", "r") as d, open("dataset_rewind_write", "w") as dr:
    for lines in d:
        mlist.append(lines)
    dr.writelines(mlist[::-1])
