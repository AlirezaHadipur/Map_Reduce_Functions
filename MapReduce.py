import numpy as np, pandas as pd

dataset = pd.read_csv("hotel_reviews.csv")

#Preprocessing dataset
dataset.dropna(axis=0, inplace=True)
dataset.drop_duplicates(inplace=True)
dataset.reset_index(inplace=True)

# Specify keywords
positive_words = ["good", "comfort", "beautiful", "best", "comfortable", "joy", "pleasant", "amazing", "wonderful", "lovely", "love", "terrefic", "excellent", "great", "happy", "friendly", "helpful", "bra", "komfort", "vacker", "bäst", "bekväm", "glädje", "trevlig", "fantastisk", "underbar", "älskvärd", "kärlek", "fantastisk", "utmärkt", "stor", "glad", "vänlig", "hjälpsam", "bueno", "comodidad", "hermoso", "mejor", "cómodo", "alegría", "agradable", "asombroso", "maravilloso", "encantador", "amor", "terrífico", "excelente", "genial", "feliz", "amigable", "servicial"]
negative_words = ["bad", "awful", "sad", "terrible", "poor", "angry", "horrible", "hate", "dislike", "malo", "triste", "pobre", "enojado", "odio", "mauvais", "affreux", "triste", "pauvre", "en colère", "haine", "cattivo", "orribile", "triste", "povero", "arrabbiato", "dålig", "hemsk", "ledsen", "fruktansvärd", "fattig", "arg", "hat"]
neutral = ["fine", "ok", "normal", "average", "bra", "genomsnitt", "bene", "normale", "media", "bien", "moyenne", "promedio"]


# Mapper Function
def mapper(row):
    # Initial values
    hotelName = row["name"]
    opinion = row["reviews.text"].lower().split()
    pos = 0
    neg = 0
    nut = 0

    # Count the number of pos, neg or neutural words in an opinion
    for word in opinion:
        if word in positive_words:
            pos += 1
        elif word in negative_words:
            neg += 1
        elif word in neutral:
            nut += 1

    # Specify the category of an opinion
    if (pos > neg) and (pos > nut) :
        return (hotelName, "positive")
    if (neg > pos) and (neg > nut):
        return (hotelName, "negative")
    if (nut > pos) and (nut > neg):
        return (hotelName, "neutural")



def shuffle_and_sort(mapped_dataset):
    # sort hotels based on their names
    sorted_hotels = sorted(mapped_dataset, key=lambda x: x[0])

    shuffled_dataset = {}

    for hotel, opinion in sorted_hotels:

        # Create a list for each hotel for the fisrt time
        if hotel not in shuffled_dataset:
            shuffled_dataset[hotel] = []

        shuffled_dataset[hotel].append(opinion)

    return shuffled_dataset


def reducer(shuffled_data):
    reduced_dataset = {}

    for hotelName , opinion in shuffled_data.items():

        if hotelName not in reduced_dataset:
            reduced_dataset[hotelName] = {}

        pos = 0
        neg = 0
        nut = 0

        for item in opinion:
            if item == "positive":
                pos += 1
            if item == "negative":
                neg += 1
            if item == "neutral":
                nut += 1

        reduced_dataset[hotelName] = {"positive": pos, "negative": neg, "neutral": nut}

    return reduced_dataset


mapped_data = []
for i in range(dataset.shape[0]):
    pair = mapper(dataset.iloc[i])
    mapped_data.append(pair)

# Remove nulls
mapped_data = [item for item in mapped_data if item is not None]

shuffled_data = shuffle_and_sort(mapped_data)

reduced_data = reducer(shuffled_data)

print(reduced_data)
