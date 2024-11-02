import customtkinter as ctk
from tkinter import filedialog, messagebox
import shutil
import os

class AppBackup(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        self.title('SIB - Sistema Integrado de Backup')
        self.geometry('500x200')
        self.resizable(False,False)
        #self.config(bg='#708090')
        self.tela_principal()

    def selecionar_origem(self):
        self.caminho_pasta_origem = filedialog.askdirectory(title='Selecionar Pasta')

        if self.caminho_pasta_origem:
            self.entry_pasta_origem.delete(0, ctk.END)
            self.entry_pasta_origem.insert(0, self.caminho_pasta_origem)

    def selecionar_destino(self):
        self.caminho_pasta_destino = filedialog.askdirectory(title='Selecionar Pasta')

        if self.caminho_pasta_destino:
            self.entry_pasta_destino.delete(0, ctk.END)
            self.entry_pasta_destino.insert(0, self.caminho_pasta_destino)

    def backup(self):
        
        if os.path.exists(self.caminho_pasta_origem):
            self.arquivo =  os.listdir(self.caminho_pasta_origem)

            for arquivos in self.arquivo:
            
                caminho_arquivo_origem = os.path.join(self.caminho_pasta_origem, arquivos)
            
                caminho_arquivo_destino = os.path.join(self.caminho_pasta_destino, arquivos)

            
                if os.path.isfile(caminho_arquivo_origem):
                
                    shutil.copy(caminho_arquivo_origem, caminho_arquivo_destino)
            messagebox.showinfo(title='Backup', message='Arquivos copiados com sucesso!!')

        else:
            messagebox.showerror(title='Backup', message='Arquivo não existe')

    def tela_principal(self):
        
        self.frame = ctk.CTkFrame(self, width=490, height=190, fg_color='#708090')
        self.frame.place(x=5,y=5)

        self.lb_pasta_origem = ctk.CTkLabel(self.frame, text='Pasta Origem', font=('Verdana', 14))
        self.lb_pasta_origem.place(x=5,y=10)

        self.entry_pasta_origem = ctk.CTkEntry(self.frame, width=350, height=30)
        self.entry_pasta_origem.place(x=5,y=35)

        self.bt_pasta_origem = ctk.CTkButton(self.frame, width=50, text='Selecionar Pasta', border_color='#FFFFFF', border_width=2, command=self.selecionar_origem)
        self.bt_pasta_origem.place(x=370,y=35)


        self.lb_pasta_destino = ctk.CTkLabel(self.frame, text='Pasta Destino', font=('Verdana', 14))
        self.lb_pasta_destino.place(x=5,y=70)

        self.entry_pasta_destino = ctk.CTkEntry(self.frame, width=350, height=30)
        self.entry_pasta_destino.place(x=5,y=100)

        self.bt_pasta_destino = ctk.CTkButton(self.frame, width=50, text='Selecionar Pasta', border_color='#FFFFFF', border_width=2, command=self.selecionar_destino)
        self.bt_pasta_destino.place(x=370,y=100)

        self.bt_backup = ctk.CTkButton(self.frame, text='Backup', anchor='CENTER', font=('Verdana',14), width=110, border_color='#FFFFFF', border_width=2, command=self.backup)
        self.bt_backup.place(x=370,y=150)

if __name__ == '__main__':
    app = AppBackup()
    app.mainloop()