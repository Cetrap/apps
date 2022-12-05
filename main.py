import customtkinter


class App(customtkinter.CTk): 
    def __init__(self): 
        super().__init__() 

        self.geometry("950X700") 
        self.minsize(950, 700) 
        self.title("clone stepik") 
        self.configure(fg_color="#FFFFFF")

        self.sign_in_btn = customtkinter.CTkButton(master=self, 
            text="войти", command=self.sign_in_btn_cb, fg_color="#222222", text_color="#FFFFFF")
        self.sign_in_btn.grid(row=1, column=1, padx=0, pady=0) 

        self.sign_up_btn = customtkinter.CTkButton(master=self, 
            text="регистрация", command=self.sign_up_btn_cb, fg_color="#222222", text_color="#FFFFFF")
        self.sign_up_btn.grid(row=1, column=2, padx=0, pady=0) 

        self.sign_out_btn = customtkinter.CTkButton(master=self, text="выйти", 
            command=self.sign_out_btn_cb, fg_color="#222222", text_color="#FFFFFF")
        self.sign_out_btn.grid(row=1, column=3, padx=0, pady=0) 

        self.sign_in_btn.bind("<Enter>", self.on_enter_btn)
        self.sign_in_btn.bind("<Leave>", self.on_leave_btn) 

    def sign_in_btn_cb(self):
        pass

    def sign_up_btn_cb(self):
        pass

    def sign_out_btn_cb(self):
        pass

    def on_enter_btn(self, e): 
        e.widget['background'] = '#333333'
    
    def on_leave_btn(self, e): 
        e.widget['background'] = '#222222'

if __name__ == "__main__": 
    app = App() 
    app.mainloop() 