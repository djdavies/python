def counting(i):
    print i
    i = i*2
    if i > 1024:
        return
    counting (i)
