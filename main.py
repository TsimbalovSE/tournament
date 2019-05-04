from tkinter import Tk, Button, Label, Text

def create_tournament(event):
    create_tournament_window = Tk()
    tournament_name_label = Label(create_tournament_window, 
                                  text="Введите название турнира: ")
    tournament_name_label.pack()
    tournament_name_text = Text(create_tournament_window )
    tournament_name_text.pack()
    tournament_name_button = Button(create_tournament_window, text="Продолжить")
    tournament_name_button.pack()
    create_tournament_window.mainloop()
    
    print("Создание турнира")

main_window = Tk()
create_tournament_button = Button(main_window, text="Создать турнир")
create_tournament_button.bind("<Button-1>", create_tournament)
create_tournament_button.pack()
main_window.mainloop()