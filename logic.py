from random import choice, seed, randint

def prediction(quest: str):
    seed(quest)
    section = randint(1, 4)

    if section == 1:
        return posAnsw()
    elif section == 2:
        return posNeutAnsw()
    elif section == 3:
        return neutAnsw()
    else:
        return negatAnsw() 

def posAnsw():
    answ = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определенно да", "Можешь быть уверен в этом"]
    
    return choice(answ)

def posNeutAnsw():
    answ = ["Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да"]
    
    return choice(answ)

def neutAnsw():
    answ = ["Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять"]
    
    return choice(answ)

def negatAnsw():
    answ = ["Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]
    
    return choice(answ)