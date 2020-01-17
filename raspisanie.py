import requests
import datetime
from collections import Counter
from bs4 import BeautifulSoup


def requestTo():
    url = "http://time-rtu.ru/?group=БСБО-02-16"
    r = requests.get(url)
    return r.text


def soupCreate(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup


def getDate(soup):
    date = []
    card = []

    card = soup.findAll('div', id='card')
    for i in card:
        temp_date = i.find('div', id='date')
        temp_date = temp_date.text
        date.append(temp_date.encode('l1').decode())
    return date


def getListOfDays():
    url = "http://time-rtu.ru/?group=БСБО-02-16"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    card = soup.findAll('div', id='day')


    list = []
    for i in card:
        lesson = i.find('td')
        if lesson != None:
            list.append(1)
        else:
            list.append(0)
    return list



def getCurrentDate():
    current = str(datetime.datetime.today())
    current = current.split(" ")
    current = current[0].split("-")
    return current


def getMaket(soup):
    maket = soup.findAll('div', id='day')

    return maket


def getTime(maket):
    time = []
    for i in maket:
        fullDay = i.findAll('tr')
        for lessonTime in fullDay:
            tempTime = lessonTime.find('td', id='time')
            time.append(tempTime.text.split()[0])

    return time


def getLessons(maket):
    finalLessons = []
    counter = 0
    for i in maket:
        fullDay = i.findAll('tr')

        for lessons in fullDay:

            lesson = lessons.findAll('td', id='lesson')
            for soloLesson in lesson:
                lessonName = soloLesson.find('div', id='dist')
                a = lessonName.text.encode('l1').decode().split()
                finalLessons.append(" ".join(a))

    return finalLessons


def getDateId(current, date):
    id = 0
    for i in date:
        tempDate = i.split()
        tempDate = tempDate[1].split("(")
        tempDate = tempDate[1]
        tempDate = tempDate[0:-1]
        print(tempDate)
        finalDate = tempDate.split(".")
        checkVar = Counter(finalDate) == Counter(current)
        id += 1
        if checkVar == True:
            break
    return id


def getMessageToSend(day_id, time, finalLessons):
    i = 0
    finalList = getListOfDays()
    message_to_send = ""
    for y in finalList:
        print(y)
        if y == 1:
            while i < 7*2:
                message_to_send = message_to_send + time[i] + finalLessons[i] + "\n"
                i += 1
        else:
            message_to_send = ""
            message_to_send = "Выходной"

    return message_to_send


text = requestTo()
soup = soupCreate(text)
date = getDate(soup)

current = getCurrentDate()
day_id = getDateId(current, date)

fullDay = getMaket(soup)
time = getTime(fullDay)
finalLessons = getLessons(fullDay)

message_to_send = getMessageToSend(day_id, time, finalLessons)
print(message_to_send)