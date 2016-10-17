 def scan(sentence):
    defined = { 'direction': ['north', 'south', 'east', 'west'],
             'verb': ['go', 'stop', 'kill', 'eat'],
             'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
             'noun': ['door', 'bear', 'princess', 'cabinet']
    }
    index = {}
    for k,v in defined.iteritems():
        for i in v:
            index.update({i:k})

    words = sentence.split()
    result = []

    for w in words:
        if w in index:
            result.append((index[w], w))
        else:
            try:
                result.append(('number', int(w)))
            except ValueError:
                result.append(('error', w))
    return result