import tkinter as tk
import tkinter.font

class Application(tk.Frame):
    # フォントを設定して、label Widgetを表示する関数
    # フォントについて : https://www.weblio.jp/content/%E3%83%95%E3%82%A9%E3%83%B3%E3%83%88
    def getFontLabel(self):
        # label Widgetを作成する。
        # tk.Label(option1, option2, ...)
        # text : テキスト情報
        # width : 幅の設定
        # height : 高さの設定
        # bg : 背景色の設定
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # font : フォントの設定。
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label = tk.Label(text="test", width=15, height=5, bg="#008000", font=('arial', 50, 'underline'))
        # label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        label.pack()

    # フォント名に適応した、文字列一覧を確認する関数
    def getFontNameList(self):
        i = 0
        # tkinter.font.families() : フォント名一覧を取得する。
        for fontName in tkinter.font.families():
            # label Widgetを作成する。
            # tk.Label(option1, option2, ...)
            # text : テキスト情報
            # width : 幅の設定
            # bg : 背景色の設定
            # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
            # font : フォントの設定。
            # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
            label = tk.Label(text=fontName, width=20, bg="#008000", font=(fontName, 10, 'underline'))

            # 12個のlabel Widgetを横に表示して、次の行へ移動する。繰り返し、12個のlabel Widgetを横に表示する。
            # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
            label.grid(row=int((i / 12)), column=(i % 12))
            i = i + 1

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)
        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")
        # self.getFontLabel()
        self.getFontNameList()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)

    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
