import pyray
import time

f1 = 0
g1 = 0
f2 = 0
g2 = 0
f3 = 0
g3 = 0
f4 = 0
g4 = 0
f5 = 0
g5 = 0
f6 = 0
g6 = 0
f7 = 0
g7 = 0
f8 = 0
g8 = 0
f9 = 0
g9 = 0
posX = 0
posY = 0
detect = 1
f_toggle = True
win = 0
close = 0

pyray.init_window(300,300,"TicTacToe")
while not pyray.window_should_close():

    if pyray.is_key_down(pyray.KeyboardKey.KEY_ESCAPE):
        pyray.close_window()

    pyray.begin_drawing()

    pyray.clear_background(pyray.WHITE)
    pyray.draw_line(100,0,100,300,pyray.BLACK)
    pyray.draw_line(200, 0, 200, 300, pyray.BLACK)
    pyray.draw_line(0, 100, 300, 100, pyray.BLACK)
    pyray.draw_line(0, 200, 300, 200, pyray.BLACK)

    pyray.end_drawing()

    if pyray.is_mouse_button_down(pyray.MouseButton.MOUSE_BUTTON_LEFT):
            posX = pyray.get_mouse_x()
            posY = pyray.get_mouse_y()

            if not (f1 == g1) or not (f2 == g2) or not (f3 == g3) or not (f4 == g4) or not (f5 == g5) or not (f6 == g6) or not (f7 == g7) or not (f8 == g8) or not (f9 == g9):
                f_toggle = not f_toggle
                g1 = f1
                g2 = f2
                g3 = f3
                g4 = f4
                g5 = f5
                g6 = f6
                g7 = f7
                g8 = f8
                g9 = f9
                time.sleep(0.2)

    if f_toggle == 1:
            detect = 1

    if not f_toggle:
            detect = 2

    if ((posX <= 100) and posY <= 100 and posX > 0 and posY > 0) or f1 == 1 or f1 == 2:
            if ((posX <= 100) and posY <= 100 and posX > 0 and posY > 0 and detect == 1 and f1 == 0) or f1 == 1:
                pyray.begin_drawing()
                pyray.draw_line(0, 0, 100, 100, pyray.DARKPURPLE)
                pyray.draw_line(0, 100, 100, 0, pyray.DARKPURPLE)
                f1 = 1

            if ((posX <= 100) and posY <= 100 and posX > 0 and posY > 0 and detect == 2 and f1 == 0) or f1 == 2:
                pyray.begin_drawing()
                pyray.draw_line(0, 0, 100, 100, pyray.RED)
                pyray.draw_line(0, 100, 100, 0, pyray.RED)
                f1 = 2



    if ((posX <= 200) and (posY <= 100) and posX > 100 and posY > 0) or f2 == 1 or f2 == 2:
            if ((posX <= 200) and (posY <= 100) and posX > 100 and posY > 0 and detect == 1 and f2 == 0) or f2 == 1:
                pyray.begin_drawing()
                pyray.draw_line(100, 0, 200, 100, pyray.DARKPURPLE)
                pyray.draw_line(100, 100, 200, 0, pyray.DARKPURPLE)
                f2 = 1

            if ((posX <= 200) and (posY <= 100) and posX > 100 and posY > 0 and detect == 2 and f2 == 0) or f2 == 2:
                pyray.begin_drawing()
                pyray.draw_line(100, 0, 200, 100, pyray.RED)
                pyray.draw_line(100, 100, 200, 0, pyray.RED)
                f2 = 2



    if ((posX < 300) and posY <= 100 and posX > 200 and posY > 0) or f3 == 1 or f3 == 2:
            if ((posX < 300) and posY <= 100 and posX > 200 and posY > 0 and detect == 1 and f3 == 0) or f3 == 1:
                pyray.begin_drawing()
                pyray.draw_line(200, 0, 300, 100, pyray.DARKPURPLE)
                pyray.draw_line(200, 100, 300, 0, pyray.DARKPURPLE)
                f3 = 1

            if ((posX <= 300) and posY <= 100 and posX > 200 and posY > 0 and detect == 2 and f3 == 0) or f3 == 2:
                pyray.begin_drawing()
                pyray.draw_line(200, 0, 300, 100, pyray.RED)
                pyray.draw_line(200, 100, 300, 0, pyray.RED)
                f3 = 2



    if ((posX <= 100) and posY <= 200 and posX > 0 and posY > 100) or f4 == 1 or f4 == 2:
            if ((posX <= 100) and posY <= 200 and posX > 0 and posY > 100 and detect == 1 and f4 == 0) or f4 == 1:
                pyray.begin_drawing()
                pyray.draw_line(0, 100, 100, 200, pyray.DARKPURPLE)
                pyray.draw_line(0, 200, 100, 100, pyray.DARKPURPLE)
                f4 = 1

            if ((posX <= 100) and posY <= 200 and posX > 0 and posY > 100 and detect == 2 and f4 == 0) or f4 == 2:
                pyray.begin_drawing()
                pyray.draw_line(0, 100, 100, 200, pyray.RED)
                pyray.draw_line(0, 200, 100, 100, pyray.RED)
                f4 = 2



    if ((posX <= 200) and posY <= 200 and posX > 100 and posY > 100) or f5 == 1 or f5 == 2:
            if ((posX <= 200) and posY <= 200 and posX > 100 and posY > 100 and detect == 1 and f5 == 0) or f5 == 1:
                pyray.begin_drawing()
                pyray.draw_line(100, 100, 200, 200, pyray.DARKPURPLE)
                pyray.draw_line(100, 200, 200, 100, pyray.DARKPURPLE)
                f5 = 1

            if ((posX <= 200) and posY <= 200 and posX > 100 and posY > 100 and detect == 2 and f5 == 0) or f5 == 2:
                pyray.begin_drawing()
                pyray.draw_line(100, 100, 200, 200, pyray.RED)
                pyray.draw_line(100, 200, 200, 100, pyray.RED)
                f5 = 2



    if ((posX < 300) and (posY <= 200) and posX > 200 and posY > 100) or f6 == 1 or f6 == 2:
            if ((posX < 300) and (posY <= 200) and posX > 200 and posY > 100 and detect == 1 and f6 == 0) or f6 == 1:
                pyray.begin_drawing()
                pyray.draw_line(200, 100, 300, 200, pyray.DARKPURPLE)
                pyray.draw_line(200, 200, 300, 100, pyray.DARKPURPLE)
                f6 = 1

            if ((posX < 300) and (posY <= 200) and posX > 200 and posY > 100 and detect == 2 and f6 == 0) or f6 == 2:
                pyray.begin_drawing()
                pyray.draw_line(200, 100, 300, 200, pyray.RED)
                pyray.draw_line(200, 200, 300, 100, pyray.RED)
                f6 = 2



    if ((posX <= 100) and posY < 300 and posX > 0 and posY > 200) or f7 == 1 or f7 == 2:
            if ((posX <= 100) and posY < 300 and posX > 0 and posY > 200 and detect == 1 and f7 == 0) or f7 == 1:
                pyray.begin_drawing()
                pyray.draw_line(0, 200, 100, 300, pyray.DARKPURPLE)
                pyray.draw_line(0, 300, 100, 200, pyray.DARKPURPLE)
                f7 = 1

            if ((posX <= 100) and posY < 300 and posX > 0 and posY > 200 and detect == 2 and f7 == 0) or f7 == 2:
                pyray.begin_drawing()
                pyray.draw_line(0, 200, 100, 300, pyray.RED)
                pyray.draw_line(0, 300, 100, 200, pyray.RED)
                f7 = 2



    if ((posX <= 200) and posY < 300 and posX > 100 and posY > 200) or f8 == 1 or f8 == 2:
            if ((posX <= 200) and posY < 300 and posX > 100 and posY > 200 and detect == 1 and f8 == 0) or f8 == 1:
                pyray.begin_drawing()
                pyray.draw_line(100, 200, 200, 300, pyray.DARKPURPLE)
                pyray.draw_line(100, 300, 200, 200, pyray.DARKPURPLE)
                f8 = 1

            if ((posX <= 200) and posY < 300 and posX > 100 and posY > 200 and detect == 2 and f8 == 0) or f8 == 2:
                pyray.begin_drawing()
                pyray.draw_line(100, 200, 200, 300, pyray.RED)
                pyray.draw_line(100, 300, 200, 200, pyray.RED)
                f8 = 2



    if ((posX < 300) and posY < 300 and posX > 200 and posY > 200) or f9 == 1 or f9 == 2:
            if ((posX < 300) and posY < 300 and posX > 200 and posY > 200 and detect == 1 and f9 == 0) or f9 == 1:
                pyray.begin_drawing()
                pyray.draw_line(200, 200, 300, 300, pyray.DARKPURPLE)
                pyray.draw_line(200, 300, 300, 200, pyray.DARKPURPLE)
                f9 = 1

            if ((posX < 300) and posY < 300 and posX > 200 and posY > 200 and detect == 2 and f9 == 0) or f9 == 2:
                pyray.begin_drawing()
                pyray.draw_line(200, 200, 300, 300, pyray.RED)
                pyray.draw_line(200, 300, 300, 200, pyray.RED)
                f9 = 2


    if close == 1:
            time.sleep(3)
            pyray.close_window()


    if win == 1:
            pyray.begin_drawing()
            pyray.draw_text("Player 1 wins!", 100, 100, 20, pyray.DARKPURPLE)
            close = 1

    if win == 2:
            pyray.begin_drawing()
            pyray.draw_text("Player 2 wins!", 100, 100, 20, pyray.RED)
            close = 1

    if win == 3:
            pyray.begin_drawing()
            pyray.draw_text("No Winner!", 100, 100, 20, pyray.GREEN)
            close = 1


    if not (f1 == 0) and not (f2 == 0) and not (f3 == 0) and not (f4 == 0) and not (f5 == 0) and not (f6 == 0) and not (f7 == 0) and not (f8 == 0) and not (f9 == 0):
            win = 3

    if (f1 == 1 and f2 == 1 and f3 == 1) or (f4 == 1 and f5 == 1 and f6 == 1) or (f7 == 1 and f8 == 1 and f9 == 1) or (f1 == 1 and f4 == 1 and f7 == 1) or (f2 == 1 and f5 == 1 and f8 == 1) or (f3 == 1 and f6 == 1 and f9 == 1) or (f1 == 1 and f5 == 1 and f9 == 1) or (f7 == 1 and f5 == 1 and f3 == 1):
            win = 1

    if (f1 == 2 and f2 == 2 and f3 == 2) or (f4 == 2 and f5 == 2 and f6 == 2) or (f7 == 2 and f8 == 2 and f9 == 2) or (f1 == 2 and f4 == 2 and f7 == 2) or (f2 == 2 and f5 == 2 and f8 == 2) or (f3 == 2 and f6 == 2 and f9 == 2) or (f1 == 2 and f5 == 2 and f9 == 2) or (f7 == 2 and f5 == 2 and f3 == 2):
            win = 2