from Languages import Languages


def get_hangman_words(lang: Languages) -> [str]:
    match lang:
        case Languages.en:
            return [
                "apple",
                "banana",
                "car",
                "dog",
                "elephant",
                "flower",
                "guitar",
                "house",
                "island",
                "jungle",
                "kite",
                "lion",
                "monkey",
                "night",
                "orange",
                "parrot",
                "queen",
                "rainbow",
                "sun",
                "tiger",
                "umbrella",
                "violin",
                "watermelon",
                "xylophone",
                "yellow",
                "zebra",
                "airplane",
                "ball",
                "cat",
                "dolphin",
                "eagle",
                "fish",
                "giraffe",
                "hat",
                "ice cream",
                "jacket",
                "king",
                "lemon",
                "mouse",
                "nose",
                "ocean",
                "piano",
                "quilt",
                "rose",
                "snake",
                "turtle",
                "uniform",
                "vase",
                "whale",
                "xylophone",
                "yacht",
                "zeppelin",
                "arch",
                "bridge",
                "cactus",
                "desert",
                "eclipse",
                "forest",
                "garden",
                "horizon",
                "island",
                "jungle",
                "koala",
                "lighthouse",
                "mountain",
                "nature",
                "oasis",
                "palm",
                "quiet",
                "river",
                "sand",
                "tree",
                "underwater",
                "valley",
                "waterfall",
                "xenophobia",
                "yawn",
                "zipper",
                "astronaut",
                "balloon",
                "comet",
                "rocket",
                "spaceship",
                "telescope",
                "universe",
                "asteroid",
                "black hole",
                "cosmos",
                "galaxy",
                "meteor",
                "planet",
                "satellite",
                "star",
                "constellation",
                "alien",
                "spacesuit"
            ]
        case Languages.pt:
            return [
                "abacaxi",
                "abelha",
                "abobora",
                "acrobacia",
                "alface",
                "amarelo",
                "anjo",
                "aranha",
                "arcoiris",
                "ave",
                "azul",
                "banana",
                "barco",
                "bicicleta",
                "bola",
                "borboleta",
                "cachorro",
                "cadeira",
                "camelo",
                "caneta",
                "carro",
                "castelo",
                "cavalo",
                "ceu",
                "chave",
                "coelho",
                "computador",
                "coracao",
                "dado",
                "danca",
                "dinossauro",
                "elefante",
                "escada",
                "espada",
                "estrela",
                "fada",
                "felicidade",
                "flor",
                "fogo",
                "gato",
                "girafa",
                "guitarra",
                "hamburguer",
                "igreja",
                "ilha",
                "indio",
                "inverno",
                "jabuti",
                "jacare",
                "joaninha",
                "jogo",
                "jornal",
                "lapis",
                "leao",
                "limao",
                "lua",
                "maca",
                "magica",
                "mar",
                "melancia",
                "minhoca",
                "morango",
                "musica",
                "navio",
                "noite",
                "nuvem",
                "olho",
                "orelha",
                "palhaco",
                "pao",
                "passaro",
                "peixe",
                "pipa",
                "planta",
                "ponte",
                "princesa",
                "queijo",
                "raposa",
                "rio",
                "roda",
                "rosa",
                "sapo",
                "sol",
                "telefone",
                "tigre",
                "trem",
                "tristeza",
                "uva",
                "vaca",
                "vento",
                "verao",
                "viagem",
                "xicara",
                "zebra"
            ]


def select_language() -> Languages:
    print("Select a language:")
    for lang in Languages:
        print(f"[{lang.value}] - {lang.name}")
    lang_value = int(input("Type the numeric value of the desired language: "))

    for lang in Languages:
        if lang.value == lang_value:
            return lang
