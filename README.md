1)тема проекта с какой целью он создавался 
2)как запустить проект(устновка пайтон, установка с гита , создавние вирутального окружения , python main.py)
3)структура requirements описание кажого модуля , с какой целью они используються в проекте
4)схема проекта(figjam or in readme)
5)описание каждого пакета в modules и файлы в нутри пакета(код) , коментарии на англ или на укр 
6)с какой целью каждый файл
7)ссылка на библиотеки где брал информацию
8)какие были проблемы при создании проекта , как решил проблему с которой столкнулся
9)сделать работу над ошибками(потоки , не создавал классы)
10)висновок на укр и на англ(с чем помог проект, как он меня прокачал , чем он был мне полезен)

#Music PLayer


## Installation

First, clone this repository:

<!-- start:code block -->
# Clone this repository
git clone https://github.com/mfts/papermark.git
cd papermark

# Install dependencies
npm install

# Copy the example .env file
cp .env.example .env

# Initialize the database
npx prisma generate
npx prisma db push

# Run the app
npm run dev

# Open http://localhost:3000 in your browser
open http://localhost:3000
<!-- end:code block -->