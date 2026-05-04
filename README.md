# Laboratory-work-9

## Тема: AI Агенти з Google ADK

## Мета: Навчитись створювати AI агентів з використанням Google ADK (Python) та Poetry для управління залежностями проекту


## 1.Підготовка робочого середовища

### Ось версії python та poetry, які я встановив:

![alt text](https://github.com/Oleksii-dot278/Laboratory-work-9/blob/main/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-04-28%20215925.png)

## 2.Встановлення Google ADK

### 1. У мене створився файл poetry.lock.  Файл poetry.lock жорстко фіксує точні версії всіх встановлених бібліотек та їхніх підзалежностей. Це потрібно для того, щоб гарантувати стабільність: у будь-якого іншого розробника цей проєкт розгорнеться з абсолютно ідентичними версіями пакетів, що виключає помилки через їхні несумісні оновлення.


### 2. У мене встановлена ADK версія 1.31.1

![alt text](https://github.com/Oleksii-dot278/Laboratory-work-9/blob/main/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-04-30%20210016.png)

### 3. Ось основні команди ADK: 1. create-creates a new app in the current folder with prepopulated agent template. 2.run-runs an interactive CLI for a certain agent. 3.web-starts a FastAPI server with Web UI for agents.


## 3.Створення простого агента з інструментом

### Agent клас це головний будівельний блок у бібліотеці Google ADK. Він представляє саму сутність штучного інтелекту в коді
### Параметр tools дозволяє передати агенту список звичайних Python-функцій, які ШІ має дозвіл самостійно викликати
### Функція get_current_time зчитує системний час комп'ютера, а потім упаковує цей час разом із назвою міста у формат словника (dict) і повертає його


## 4.Запуск агента через командний рядок

### Я спитав у робота який час у Львові:
![alt-text](https://github.com/Oleksii-dot278/Laboratory-work-9/blob/main/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-05-04%20175608.png)

### Я спитав у робота час у інших містах:

![alt-text](https://github.com/Oleksii-dot278/Laboratory-work-9/blob/main/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-05-04%20180306.png)

