import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')
        
        self.label1 = Label(window, text="샌드위치 (5000원)")
        self.label1.grid(row=1, column=0)
        self.input1 = Entry(window) # 샌드위치의 값
        self.input1.grid(row=1, column=1)
        
        
        self.label2 = Label(window, text="케이크 (20000원)")
        self.label2.grid(row=2, column=0)
        self.input2 = Entry(window) # 케이크의 값
        self.input2.grid(row=2, column=1)

        button = Button(window, text="주문하기", command=self.send_order)
        button.grid(row=3, column=0)

    def send_order(self):
        order_text = ""
        
        if self.name == "고객A": # 고객 A일때
            try:
                if int(self.input1.get()) > 0: # 샌드위치가 0보다 클때
                    order_text = "고객A: 샌드위치 (5000원) " + order_text + self.input1.get() +"개, "
                
            except ValueError:
                order_text = "고객A: " + order_text

            try:
                if int(self.input2.get()) > 0: # 케이크가 0보다 클때
                    order_text = order_text + " 케이크 (20000원) " + self.input2.get() + "개"
                
            except ValueError:
                order_text = order_text

        else: # 고객 B일때
            try:
                if int(self.input1.get()) > 0: # 샌드위치가 0보다 클때
                    order_text = "고객B: 샌드위치 (5000원) " + order_text + self.input1.get() + "개, "
            
            except ValueError:
                order_text = "고객B: " + order_text

            try:
                if int(self.input2.get()) > 0: # 케이크가 0보다 클때
                    order_text = order_text + " 케이크 (20000원) " + self.input2.get() + "개"

            except ValueError:
                order_text = order_text

        self.bakeryView.add_order(order_text)


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
