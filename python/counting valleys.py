def countingValleys():
    steps = 8
    keepTrackOfCount = 0
    count = 0
    path = "UDDDUDUU"
    for step in path:
        if step == "U":
            keepTrackOfCount += 1
            if keepTrackOfCount == 0:
                count += 1
        else:
            keepTrackOfCount -= 1
    return count


if __name__ == '__main__':
    result = countingValleys()
    print(result)
