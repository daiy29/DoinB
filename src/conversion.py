def msToTime(ms):
    seconds = int((ms / 1000) % 60)
    minutes = int((ms / (1000 * 60)) % 60)
    return str("%d:%d" % (minutes, seconds))