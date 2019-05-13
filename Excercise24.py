with open('file1.txt','r') as read_file:
    txt = read_file.readlines()
    with open('file2.txt','w') as write_file:
        for temp in txt:
            if '<a href' in temp:
                new_str = temp[temp.index('"')+1:temp.index('"',temp.index('"')+1)]
                write_file.write(new_str+'\n')