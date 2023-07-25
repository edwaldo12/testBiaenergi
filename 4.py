def intersect(bagA, bagB):
    setB = set(bagB)
    return [item for item in bagA if item in setB]
