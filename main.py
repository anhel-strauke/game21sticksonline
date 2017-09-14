from bottle import run, route, request, response, redirect
from templates import page_template, start_page_template, first_turn_template, turn_template, win_template

### Views ##########################################

@route("/")
def main_view():
    return make_page("", start_page_template)

@route("/start/")
def start_view():
    set_sticks(21)
    page = first_turn_template.format(sticks=draw_sticks(21))
    return make_page("Начало игры", page)

@route("/take/<n>/")
def turn_view(n):
    sticks_num = get_sticks()
    print("Sticks in cookie:", repr(sticks_num))
    try:
    	n = int(n)
    except ValueError:
        print("n is not int")
        redirect("/start")
        return
    if sticks_num is None:
        print("bad cookie")
        redirect("/start/")
    elif n < 1 or n > 3:
        print("n should be between 1 and 3")
        redirect("/start/")
    else:
        sticks_after_player = sticks_num - n
        comp_n = 4 - n
        sticks_after_comp = sticks_after_player - comp_n
        if sticks_after_comp == 1:
            page = win_template.format(
                player_turn_sticks=make_sticks_string(n),
                player_left_sticks=make_sticks_string(sticks_after_player),
                computer_take_sticks=make_sticks_string(comp_n),
                sticks=draw_sticks(1))
            set_sticks(sticks_after_comp)
            return make_page("Конец игры", page)
        else:
            page = turn_template.format(
                player_turn_sticks=make_sticks_string(n),
                player_left_sticks=make_sticks_string(sticks_after_player),
                computer_take_sticks=make_sticks_string(comp_n),
                computer_left_sticks=make_sticks_string(sticks_after_comp),
                sticks=draw_sticks(sticks_after_comp))
            set_sticks(sticks_after_comp)
            return make_page("Идёт игра", page)


### Functions ######################################

def get_sticks():
    sticks_str = request.cookies.get("sticks", "")
    if sticks_str != "":
        try:
            return int(sticks_str)
        except ValueError:
                return None
    else:
        return None

def set_sticks(new_sticks_number):
    response.set_cookie("sticks", str(new_sticks_number), max_age=60 * 60 * 24, path="/")

def make_sticks_string(n):
    if 10 <= n <= 20:
        return "{} палочек".format(n)
    last_digit = str(n)[-1]
    if last_digit == "1":
        return "{} палочка".format(n)
    elif last_digit in ("2", "3", "4"):
        return "{} палочки".format(n)
    else:
        return "{} палочек".format(n)

def draw_sticks(n):
    return " ".join("|" * n)

def make_page(title, content):
    if title == "":
        t = "21 палочка онлайн"
    else:
        t = title + " – 21 палочка онлайн"
    return page_template.format(title=t, content=content)

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
