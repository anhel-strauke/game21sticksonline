page_template = """<!DOCTYPE HTML>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto+Slab:400,700&amp;subset=cyrillic" rel="stylesheet">
    <style type="text/css">
        html {{
            font-family: "Roboto Slab", serif;
            font-size: 16pt;
            color: black;
            background: #f9f8f2;
        }}
        body {{
            max-width: 960px;
            margin: 0 auto;
        }}
        h1 {{
            border-bottom: 1px solid black;
        }}
        footer {{
            font-size: 80%;
            border-top: 1px solid black;
        }}
        a {{
            color: #161616;
        }}
        p.sticks {{
            font-size: 140%;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <h1><a href="/">21 палочка онлайн</a></h1>
    <div id="content">
{content}
    </div>
    <footer>
        <p>&copy; 2017, Анатолий Грико.</p>
        <p>Разработано для <a href="https://anhel.in/python/" target="_blank">учебного курса по языку Python</a>.</p>
</body>
</html>
"""


start_page_template = """
    <h2>Правила игры</h2>
    <p>Играют двое. На столе перед ними 21 палочка. Ходят игроки по очереди. В свой ход игрок может взять со стола
    одну, две или три палочки, после чего ход делает другой игрок.</p>
    <p>Проигрывает тот, кто возьмёт последнюю палочку.</p>
    <p align="center">
        <a href="/start/">Начать игру!</a>
    </p>
"""

first_turn_template = """
    <p>Начало игры! На столе 21 палочка. Ваш ход.</p>
    <p>Сколько палочек вы возьмёте?</p>
    <p class="sticks">{sticks}</p>
    <p><a href="/take/1/">Возьму 1</a> | <a href="/take/2/">Возьму 2</a> | <a href="/take/3/">Возьму 3</a></p>
"""

turn_template = """
    <p>Вы взяли {player_turn_sticks}, на столе {player_left_sticks}. Мой ход.</p>
    <p>Я беру {computer_take_sticks}. На столе {computer_left_sticks}. Ваш ход.</p>
    <p>Сколько палочек вы возьмёте?</p>
    <p class="sticks">{sticks}</p>
    <p><a href="/take/1/">Возьму 1</a> | <a href="/take/2/">Возьму 2</a> | <a href="/take/3/">Возьму 3</a> | <a href="/start/">Начать заново</a></p>
"""

win_template = """
    <p>Вы взяли {player_turn_sticks}, на столе {player_left_sticks}. Мой ход.</p>
    <p>Я беру {computer_take_sticks}. На столе осталась последняя палочка.</p>
    <p>Вы проиграли.</p>
    <p class="sticks">{sticks}</p>
    <p><a href="/start/">Начать игру с начала!</a></p>
"""
