# 4.2.14
print("Q14 is:")


def main():

    composers = ["Johann Sebastian Bach", "Wolfgang Amadeus Mozart", "Franz Joseph Haydn", "Ralph Vaughn Williams"]
    composers.sort(key=length)
    for composer in composers:
        print(composer)


def length(composer):
    comp = composer.split
    return len(comp[-1])


main()

