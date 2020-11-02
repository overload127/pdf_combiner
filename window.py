import tkinter as tk
import tkinter.filedialog as filedialog

import simpletable as my_table
import scrollable as my_scroll
import pdf_combiner


class Mywindow:
    def __init__(self, master):
        # Переменная хранит путь к рабочей папки
        self.path = tk.StringVar()

        # создаём контейнеры, для правильного размещения объектов
        self.frame_top = tk.LabelFrame(master, text="Кнопки управления")
        self.frame_bot = tk.LabelFrame(master, text="Таблица файлов")
        self.frame_top_1 = tk.Frame(self.frame_top)
        self.frame_top_2 = tk.Frame(self.frame_top)
        # Размещаем контейнеры на форме
        self.frame_top.pack(side=tk.TOP, expand=tk.NO, fill=tk.X)
        self.frame_bot.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)
        self.frame_top_1.pack(side=tk.TOP, expand=tk.NO, fill=tk.X)
        self.frame_top_2.pack(side=tk.TOP, expand=tk.NO, fill=tk.X)

        # Создаём кнопки
        self.button_selectfolder = tk.Button(
            self.frame_top_1, text="Выбрать папку с файлами",
            command=self.selectfolder)
        self.button_loadfiles = tk.Button(
            self.frame_top_1, text="Добавить файлы",
            command=self.loadfiles)
        self.button_execute = tk.Button(
            self.frame_top_1, text="Объединить",
            command=self.execute)
        self.button_cleaner = tk.Button(
            self.frame_top_1, text="Отчистить таблицу",
            command=self.cleaner)
        
        # Создаем поле и подпись для показа пути рабочей папки
        self.label_path = tk.Label(
            self.frame_top_2, text="Путь к папке с файлами:")
        self.path_field = tk.Entry(
            self.frame_top_2, textvariable=self.path)

        # Размещаем элементы (кнопки и поля) в соответствующих контейнерах
        self.button_selectfolder.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        self.button_loadfiles.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        self.button_execute.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        self.button_cleaner.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        self.label_path.pack(side=tk.TOP, expand=tk.YES, fill=tk.X)
        self.path_field.pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.X)

        # Создаём контейнер для таблицы
        self.scrollable_body = my_scroll.Scrollable(self.frame_bot, width=32)
        # Создаём таблицу внутри контейнера для таблицы
        self.table = my_table.SimpleTable(
            self.scrollable_body, ['Путь к файлу'], 0)
        self.table.pack(side=tk.TOP, expand=tk.YES, fill=tk.X)
        self.scrollable_body.update()

        self.root = master

    def selectfolder(self):
        """
        Выбираем папку с файлами
        """
        self.path.set(filedialog.askdirectory())
    
    def loadfiles(self):
        """
        Добавить файлы из папки
        """
        list_file = pdf_combiner.get_file_from_dir(self.path.get())
        
        for path_file in list_file:
            self.table.add_line_end((path_file,))
        
        self.scrollable_body.update()
    
    def execute(self):
        """
        Выполняем объединение файлов в один
        """
        list_file = self.table.get_true_lines()
        clean_list_file = []
        for line in list_file:
            clean_list_file.append(line[0])

        if clean_list_file:
            pdf_combiner.create_from_files(tuple(clean_list_file), self.path.get())

    def cleaner(self):
        """
        Отчищаем таблицу от файлов
        """
        self.table.cleaning()
        self.scrollable_body.update()


if __name__ == "__main__":
    root = tk.Tk()
    first_win = Mywindow(root)
    root.mainloop()
