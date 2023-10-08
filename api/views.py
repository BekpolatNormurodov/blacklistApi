from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person = [
    {
        "photo": "",
        "name": "Bekpolat",
        "surname": "Normurodov",
        "fathersName": "Ergash O'g'li",
        "age": "22.07.1992",
        "sud": "Ha",
        "car": "Yo'q",
        "about": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable.",
        "passportNumber": "AB 0112196",
        "idNumber": "12345671234567",
        "phoneNumbers": [
            "+998(97)379 19 95"
        ],
        "cards": [
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            }
        ],
        "friends": [
            {
                "name": "Bekpolat",
                "photo": ""
            },
            {
                "name": "Murod",
                "photo": ""
            },
            {
                "name": "Islom",
                "photo": ""
            },
            {
                "name": "Jonibek",
                "photo": ""
            },
            {
                "name": "Abror",
                "photo": ""
            },
            {
                "name": "Hasan",
                "photo": ""
            }
        ]
    },
    {
        "photo": "",
        "name": "Jonibek",
        "surname": "Normurodov",
        "fathersName": "Ergash O'g'li",
        "age": "22.07.1992",
        "sud": "Ha",
        "car": "Yo'q",
        "about": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. ",
        "passportNumber": "AB 0112196",
        "idNumber": "12345671234567",
        "phoneNumbers": [
            "+998(93)805 22 95",
            "+998(97)379 19 95"
        ],
        "cards": [
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "8600 8790 6789 5482",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            }
        ],
        "friends": [
            {
                "name": "Bekpolat",
                "photo": ""
            },
            {
                "name": "Murod",
                "photo": ""
            },
            {
                "name": "Islom",
                "photo": ""
            },
            {
                "name": "Jonibek",
                "photo": ""
            },
            {
                "name": "Abror",
                "photo": ""
            },
            {
                "name": "Hasan",
                "photo": ""
            }
        ]
    },
    {
        "photo": "",
        "name": "Murod",
        "surname": "Normurodov",
        "fathersName": "Ergash O'g'li",
        "age": "22.07.1992",
        "sud": "Ha",
        "car": "Yo'q",
        "about": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text.",
        "passportNumber": "AB 0112196",
        "idNumber": "12345671234567",
        "phoneNumbers": [
            "+998(93)805 22 95",
            "+998(97)379 19 95"
        ],
        "cards": [
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "8600 8790 6789 5482",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            }
        ],
        "friends": [
            {
                "name": "Bekpolat",
                "photo": ""
            },
            {
                "name": "Murod",
                "photo": ""
            },
            {
                "name": "Islom",
                "photo": ""
            },
            {
                "name": "Jonibek",
                "photo": ""
            },
            {
                "name": "Abror",
                "photo": ""
            },
            {
                "name": "Hasan",
                "photo": ""
            }
        ]
    },
    {
        "photo": "",
        "name": "Islom",
        "surname": "Normurodov",
        "fathersName": "Ergash O'g'li",
        "age": "22.07.1992",
        "sud": "Ha",
        "car": "Yo'q",
        "about": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable.",
        "passportNumber": "AB 0112196",
        "idNumber": "12345671234567",
        "phoneNumbers": [
            "+998(93)805 22 95",
            "+998(97)379 19 95"
        ],
        "cards": [
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "8600 8790 6789 5482",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            }
        ],
        "friends": [
            {
                "name": "Bekpolat",
                "photo": ""
            },
            {
                "name": "Murod",
                "photo": ""
            },
            {
                "name": "Islom",
                "photo": ""
            },
            {
                "name": "Jonibek",
                "photo": ""
            },
            {
                "name": "Abror",
                "photo": ""
            },
            {
                "name": "Hasan",
                "photo": ""
            }
        ]
    },
    {
        "photo": "",
        "name": "Hasan",
        "surname": "Normurodov",
        "fathersName": "Ergash O'g'li",
        "age": "22.07.1992",
        "sud": "Ha",
        "car": "Yo'q",
        "about": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. ",
        "passportNumber": "AB 0112196",
        "idNumber": "12345671234567",
        "phoneNumbers": [
            "+998(93)805 22 95",
            "+998(97)379 19 95"
        ],
        "cards": [
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "8600 8790 6789 5482",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            }
        ],
        "friends": [
            {
                "name": "Bekpolat",
                "photo": ""
            },
            {
                "name": "Murod",
                "photo": ""
            },
            {
                "name": "Islom",
                "photo": ""
            },
            {
                "name": "Jonibek",
                "photo": ""
            },
            {
                "name": "Abror",
                "photo": ""
            },
            {
                "name": "Hasan",
                "photo": ""
            }
        ]
    },
    {
        "photo": "",
        "name": "Husan",
        "surname": "Normurodov",
        "fathersName": "Ergash O'g'li",
        "age": "22.07.1992",
        "sud": "Ha",
        "car": "Yo'q",
        "about": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. ",
        "passportNumber": "AB 0112196",
        "idNumber": "12345671234567",
        "phoneNumbers": [
            "+998(93)805 22 95",
            "+998(97)379 19 95"
        ],
        "cards": [
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "8600 8790 6789 5482",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            }
        ],
        "friends": [
            {
                "name": "Bekpolat",
                "photo": ""
            },
            {
                "name": "Murod",
                "photo": ""
            },
            {
                "name": "Islom",
                "photo": ""
            },
            {
                "name": "Jonibek",
                "photo": ""
            },
            {
                "name": "Abror",
                "photo": ""
            },
            {
                "name": "Hasan",
                "photo": ""
            }
        ]
    },
    {
        "photo": "",
        "name": "Shaxboz",
        "surname": "Normurodov",
        "fathersName": "Ergash O'g'li",
        "age": "22.07.1992",
        "sud": "Ha",
        "car": "Yo'q",
        "about": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. ",
        "passportNumber": "AB 0112196",
        "idNumber": "12345671234567",
        "phoneNumbers": [
            "+998(93)805 22 95",
            "+998(97)379 19 95"
        ],
        "cards": [
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "8600 8790 6789 5482",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            }
        ],
        "friends": [
            {
                "name": "Bekpolat",
                "photo": ""
            },
            {
                "name": "Murod",
                "photo": ""
            },
            {
                "name": "Islom",
                "photo": ""
            },
            {
                "name": "Jonibek",
                "photo": ""
            },
            {
                "name": "Abror",
                "photo": ""
            },
            {
                "name": "Hasan",
                "photo": ""
            }
        ]
    },
    {
        "photo": "",
        "name": "Xurshid",
        "surname": "Normurodov",
        "fathersName": "Ergash O'g'li",
        "age": "22.07.1992",
        "sud": "Ha",
        "car": "Yo'q",
        "about": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. ",
        "passportNumber": "AB 0112196",
        "idNumber": "12345671234567",
        "phoneNumbers": [
            "+998(93)805 22 95",
            "+998(97)379 19 95"
        ],
        "cards": [
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "8600 8790 6789 5482",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            }
        ],
        "friends": [
            {
                "name": "Bekpolat",
                "photo": ""
            },
            {
                "name": "Murod",
                "photo": ""
            },
            {
                "name": "Islom",
                "photo": ""
            },
            {
                "name": "Jonibek",
                "photo": ""
            },
            {
                "name": "Abror",
                "photo": ""
            },
            {
                "name": "Hasan",
                "photo": ""
            }
        ]
    },
    {
        "photo": "",
        "name": "Alisher",
        "surname": "Normurodov",
        "fathersName": "Ergash O'g'li",
        "age": "22.07.1992",
        "sud": "Ha",
        "car": "Yo'q",
        "about": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. ",
        "passportNumber": "AB 0112196",
        "idNumber": "12345671234567",
        "phoneNumbers": [
            "+998(93)805 22 95",
            "+998(97)379 19 95"
        ],
        "cards": [
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "8600 8790 6789 5482",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            }
        ],
        "friends": [
            {
                "name": "Bekpolat",
                "photo": ""
            },
            {
                "name": "Murod",
                "photo": ""
            },
            {
                "name": "Islom",
                "photo": ""
            },
            {
                "name": "Jonibek",
                "photo": ""
            },
            {
                "name": "Abror",
                "photo": ""
            },
            {
                "name": "Hasan",
                "photo": ""
            }
        ]
    },  
    {
        "photo": "",
        "name": "Bekpolat",
        "surname": "Normurodov",
        "fathersName": "Ergash O'g'li",
        "age": "22.07.1992",
        "sud": "Ha",
        "car": "Yo'q",
        "about": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable.",
        "passportNumber": "AB 0112196",
        "idNumber": "12345671234567",
        "phoneNumbers": [
            "+998(97)379 19 95"
        ],
        "cards": [
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            }
        ],
        "friends": [
            {
                "name": "Bekpolat",
                "photo": ""
            },
            {
                "name": "Murod",
                "photo": ""
            },
            {
                "name": "Islom",
                "photo": ""
            },
            {
                "name": "Jonibek",
                "photo": ""
            },
            {
                "name": "Abror",
                "photo": ""
            },
            {
                "name": "Hasan",
                "photo": ""
            }
        ]
    },
    {
        "photo": "",
        "name": "Jonibek",
        "surname": "Normurodov",
        "fathersName": "Ergash O'g'li",
        "age": "22.07.1992",
        "sud": "Ha",
        "car": "Yo'q",
        "about": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. ",
        "passportNumber": "AB 0112196",
        "idNumber": "12345671234567",
        "phoneNumbers": [
            "+998(93)805 22 95",
            "+998(97)379 19 95"
        ],
        "cards": [
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "8600 8790 6789 5482",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            }
        ],
        "friends": [
            {
                "name": "Bekpolat",
                "photo": ""
            },
            {
                "name": "Murod",
                "photo": ""
            },
            {
                "name": "Islom",
                "photo": ""
            },
            {
                "name": "Jonibek",
                "photo": ""
            },
            {
                "name": "Abror",
                "photo": ""
            },
            {
                "name": "Hasan",
                "photo": ""
            }
        ]
    },
    {
        "photo": "",
        "name": "Murod",
        "surname": "Normurodov",
        "fathersName": "Ergash O'g'li",
        "age": "22.07.1992",
        "sud": "Ha",
        "car": "Yo'q",
        "about": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text.",
        "passportNumber": "AB 0112196",
        "idNumber": "12345671234567",
        "phoneNumbers": [
            "+998(93)805 22 95",
            "+998(97)379 19 95"
        ],
        "cards": [
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "8600 8790 6789 5482",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            }
        ],
        "friends": [
            {
                "name": "Bekpolat",
                "photo": ""
            },
            {
                "name": "Murod",
                "photo": ""
            },
            {
                "name": "Islom",
                "photo": ""
            },
            {
                "name": "Jonibek",
                "photo": ""
            },
            {
                "name": "Abror",
                "photo": ""
            },
            {
                "name": "Hasan",
                "photo": ""
            }
        ]
    },
    {
        "photo": "",
        "name": "Islom",
        "surname": "Normurodov",
        "fathersName": "Ergash O'g'li",
        "age": "22.07.1992",
        "sud": "Ha",
        "car": "Yo'q",
        "about": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable.",
        "passportNumber": "AB 0112196",
        "idNumber": "12345671234567",
        "phoneNumbers": [
            "+998(93)805 22 95",
            "+998(97)379 19 95"
        ],
        "cards": [
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "8600 8790 6789 5482",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            }
        ],
        "friends": [
            {
                "name": "Bekpolat",
                "photo": ""
            },
            {
                "name": "Murod",
                "photo": ""
            },
            {
                "name": "Islom",
                "photo": ""
            },
            {
                "name": "Jonibek",
                "photo": ""
            },
            {
                "name": "Abror",
                "photo": ""
            },
            {
                "name": "Hasan",
                "photo": ""
            }
        ]
    },
    {
        "photo": "",
        "name": "Hasan",
        "surname": "Normurodov",
        "fathersName": "Ergash O'g'li",
        "age": "22.07.1992",
        "sud": "Ha",
        "car": "Yo'q",
        "about": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. ",
        "passportNumber": "AB 0112196",
        "idNumber": "12345671234567",
        "phoneNumbers": [
            "+998(93)805 22 95",
            "+998(97)379 19 95"
        ],
        "cards": [
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "8600 8790 6789 5482",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            }
        ],
        "friends": [
            {
                "name": "Bekpolat",
                "photo": ""
            },
            {
                "name": "Murod",
                "photo": ""
            },
            {
                "name": "Islom",
                "photo": ""
            },
            {
                "name": "Jonibek",
                "photo": ""
            },
            {
                "name": "Abror",
                "photo": ""
            },
            {
                "name": "Hasan",
                "photo": ""
            }
        ]
    },
    {
        "photo": "",
        "name": "Husan",
        "surname": "Normurodov",
        "fathersName": "Ergash O'g'li",
        "age": "22.07.1992",
        "sud": "Ha",
        "car": "Yo'q",
        "about": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. ",
        "passportNumber": "AB 0112196",
        "idNumber": "12345671234567",
        "phoneNumbers": [
            "+998(93)805 22 95",
            "+998(97)379 19 95"
        ],
        "cards": [
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "8600 8790 6789 5482",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            }
        ],
        "friends": [
            {
                "name": "Bekpolat",
                "photo": ""
            },
            {
                "name": "Murod",
                "photo": ""
            },
            {
                "name": "Islom",
                "photo": ""
            },
            {
                "name": "Jonibek",
                "photo": ""
            },
            {
                "name": "Abror",
                "photo": ""
            },
            {
                "name": "Hasan",
                "photo": ""
            }
        ]
    },
    {
        "photo": "",
        "name": "Shaxboz",
        "surname": "Normurodov",
        "fathersName": "Ergash O'g'li",
        "age": "22.07.1992",
        "sud": "Ha",
        "car": "Yo'q",
        "about": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. ",
        "passportNumber": "AB 0112196",
        "idNumber": "12345671234567",
        "phoneNumbers": [
            "+998(93)805 22 95",
            "+998(97)379 19 95"
        ],
        "cards": [
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "8600 8790 6789 5482",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            }
        ],
        "friends": [
            {
                "name": "Bekpolat",
                "photo": ""
            },
            {
                "name": "Murod",
                "photo": ""
            },
            {
                "name": "Islom",
                "photo": ""
            },
            {
                "name": "Jonibek",
                "photo": ""
            },
            {
                "name": "Abror",
                "photo": ""
            },
            {
                "name": "Hasan",
                "photo": ""
            }
        ]
    },
    {
        "photo": "",
        "name": "Xurshid",
        "surname": "Normurodov",
        "fathersName": "Ergash O'g'li",
        "age": "22.07.1992",
        "sud": "Ha",
        "car": "Yo'q",
        "about": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. ",
        "passportNumber": "AB 0112196",
        "idNumber": "12345671234567",
        "phoneNumbers": [
            "+998(93)805 22 95",
            "+998(97)379 19 95"
        ],
        "cards": [
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "8600 8790 6789 5482",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            }
        ],
        "friends": [
            {
                "name": "Bekpolat",
                "photo": ""
            },
            {
                "name": "Murod",
                "photo": ""
            },
            {
                "name": "Islom",
                "photo": ""
            },
            {
                "name": "Jonibek",
                "photo": ""
            },
            {
                "name": "Abror",
                "photo": ""
            },
            {
                "name": "Hasan",
                "photo": ""
            }
        ]
    },
    {
        "photo": "",
        "name": "Alisher",
        "surname": "Normurodov",
        "fathersName": "Ergash O'g'li",
        "age": "22.07.1992",
        "sud": "Ha",
        "car": "Yo'q",
        "about": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. ",
        "passportNumber": "AB 0112196",
        "idNumber": "12345671234567",
        "phoneNumbers": [
            "+998(93)805 22 95",
            "+998(97)379 19 95"
        ],
        "cards": [
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "1234 5678 1234 5678",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            },
            {
                "bank": "IPOTEKA BANK",
                "name": "Bekpolat Normurodov Ergash o'g'li",
                "number": "8600 8790 6789 5482",
                "phone": "+998(93)805 22 95",
                "date": "12/24"
            }
        ],
        "friends": [
            {
                "name": "Bekpolat",
                "photo": ""
            },
            {
                "name": "Murod",
                "photo": ""
            },
            {
                "name": "Islom",
                "photo": ""
            },
            {
                "name": "Jonibek",
                "photo": ""
            },
            {
                "name": "Abror",
                "photo": ""
            },
            {
                "name": "Hasan",
                "photo": ""
            }
        ]
    }
]
    return Response(person)