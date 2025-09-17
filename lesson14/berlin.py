from random import choice

capital = "Berlin"  # Berlin is both a city and a state in Germany

bird = "Common Blackbird"  # Common city bird in Berlin

flower = "Bear's Ear"  # Traditional flower associated with Berlin

song = "Berliner Luft"  # Famous Berlin song


def randomfunfact():
    funfacts = [
        "Berlin has more bridges than Venice - over 1,700 bridges span the city's waterways.",
        "The city was divided by the Berlin Wall for 28 years, from 1961 to 1989.",
        "Berlin is home to the largest train station in Europe - Berlin Hauptbahnhof.",
        "The city has more museums than rainy days - over 180 museums and collections.",
        "Berlin's Tempelhof Airport is now one of the world's largest urban parks.",
        "The Brandenburg Gate was once a symbol of division, now it represents unity."
    ]

    index = choice("012345")

    print(funfacts[int(index)])


if __name__ == "__main__":
    randomfunfact()
