import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog

import simpletable as my_table
import scrollable as my_scroll
import pdf_combiner
import image_to_pdf


class Mywindow:
    def __init__(self, master):
        # Контейнер вкладок
        self.tabs = ttk.Notebook(master)
        # Размещаем вкладку на форме
        self.tabs.pack(fill='both', expand='yes')

        ################################################################
        # Создаём вкладку 1 (pdf to pdf)
        ################################################################
        # Переменная хранит путь к рабочей папки
        self.tab_1_path = tk.StringVar()

        # создаём контейнеры, для правильного размещения объектов на вкладке
        self.tab_1_frame = tk.Frame(master)
        self.tab_1_frame_top = tk.LabelFrame(self.tab_1_frame, text="Кнопки управления")
        self.tab_1_frame_bot = tk.LabelFrame(self.tab_1_frame, text="Таблица файлов")
        self.tab_1_frame_top_1 = tk.Frame(self.tab_1_frame_top)
        self.tab_1_frame_top_2 = tk.Frame(self.tab_1_frame_top)
        # Размещаем контейнеры на вкладке
        self.tab_1_frame.pack(expand=tk.YES, fill=tk.BOTH)
        self.tab_1_frame_top.pack(side=tk.TOP, expand=tk.NO,  fill=tk.X)
        self.tab_1_frame_bot.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)
        self.tab_1_frame_top_1.pack(side=tk.TOP, expand=tk.NO,  fill=tk.X)
        self.tab_1_frame_top_2.pack(side=tk.TOP, expand=tk.NO,  fill=tk.X)
        
        self.tabs.add(self.tab_1_frame, text='PDF-ки')

        # Создаём кнопки
        self.tab_1_button_selectfolder = tk.Button(
            self.tab_1_frame_top_1, text="Выбрать папку с файлами",
            command=self.tab_1_selectfolder)
        self.tab_1_button_loadfiles = tk.Button(
            self.tab_1_frame_top_1, text="Добавить файлы",
            command=self.tab_1_loadfiles)
        self.tab_1_button_execute = tk.Button(
            self.tab_1_frame_top_1, text="Объединить",
            command=self.tab_1_execute)
        self.tab_1_button_cleaner = tk.Button(
            self.tab_1_frame_top_1, text="Отчистить таблицу",
            command=self.tab_1_cleaner)
        
        # Создаем поле и подпись для показа пути рабочей папки
        self.tab_1_label_path = tk.Label(
            self.tab_1_frame_top_2, text="Путь к папке с файлами:")
        self.tab_1_path_field = tk.Entry(
            self.tab_1_frame_top_2, textvariable=self.tab_1_path)

        # Размещаем элементы (кнопки и поля) в соответствующих контейнерах
        self.tab_1_button_selectfolder.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        self.tab_1_button_loadfiles.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        self.tab_1_button_execute.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        self.tab_1_button_cleaner.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        self.tab_1_label_path.pack(side=tk.TOP, expand=tk.YES, fill=tk.X)
        self.tab_1_path_field.pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.X)

        # Создаём контейнер для таблицы
        self.tab_1_scrollable_body = my_scroll.Scrollable(self.tab_1_frame_bot, width=32)
        # Создаём таблицу внутри контейнера для таблицы
        self.tab_1_table = my_table.SimpleTable(
            self.tab_1_scrollable_body, ['Путь к файлу'], 0)
        self.tab_1_table.pack(side=tk.TOP, expand=tk.YES, fill=tk.X)
        self.tab_1_scrollable_body.update()


        ################################################################
        # Создаём вкладку 2
        ################################################################
        # Переменная хранит путь к рабочей папки
        self.tab_2_path = tk.StringVar()

        # создаём контейнеры, для правильного размещения объектов на вкладке
        self.tab_2_frame = tk.Frame(master)
        self.tab_2_frame_top = tk.LabelFrame(self.tab_2_frame, text="Кнопки управления")
        self.tab_2_frame_bot = tk.LabelFrame(self.tab_2_frame, text="Таблица файлов")
        self.tab_2_frame_top_1 = tk.Frame(self.tab_2_frame_top)
        self.tab_2_frame_top_2 = tk.Frame(self.tab_2_frame_top)
        # Размещаем контейнеры на вкладке
        self.tab_2_frame.pack(expand=tk.YES, fill=tk.BOTH)
        self.tab_2_frame_top.pack(side=tk.TOP, expand=tk.NO,  fill=tk.X)
        self.tab_2_frame_bot.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)
        self.tab_2_frame_top_1.pack(side=tk.TOP, expand=tk.NO,  fill=tk.X)
        self.tab_2_frame_top_2.pack(side=tk.TOP, expand=tk.NO,  fill=tk.X)
        
        self.tabs.add(self.tab_2_frame, text="Изображения")

        # Создаём кнопки
        self.tab_2_button_selectfolder = tk.Button(
            self.tab_2_frame_top_1, text="Выбрать папку с файлами",
            command=self.tab_2_selectfolder)
        self.tab_2_button_loadfiles = tk.Button(
            self.tab_2_frame_top_1, text="Добавить файлы",
            command=self.tab_2_loadfiles)
        self.tab_2_button_execute = tk.Button(
            self.tab_2_frame_top_1, text="Объединить",
            command=self.tab_2_execute)
        self.tab_2_button_cleaner = tk.Button(
            self.tab_2_frame_top_1, text="Отчистить таблицу",
            command=self.tab_2_cleaner)
        
        # Создаем поле и подпись для показа пути рабочей папки
        self.tab_2_label_path = tk.Label(
            self.tab_2_frame_top_2, text="Путь к папке с файлами:")
        self.tab_2_path_field = tk.Entry(
            self.tab_2_frame_top_2, textvariable=self.tab_2_path)

        # Размещаем элементы (кнопки и поля) в соответствующих контейнерах
        self.tab_2_button_selectfolder.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        self.tab_2_button_loadfiles.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        self.tab_2_button_execute.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        self.tab_2_button_cleaner.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        self.tab_2_label_path.pack(side=tk.TOP, expand=tk.YES, fill=tk.X)
        self.tab_2_path_field.pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.X)

        # Создаём контейнер для таблицы
        self.tab_2_scrollable_body = my_scroll.Scrollable(self.tab_2_frame_bot, width=32)
        # Создаём таблицу внутри контейнера для таблицы
        self.tab_2_table = my_table.SimpleTable(
            self.tab_2_scrollable_body, ['Путь к файлу'], 0)
        self.tab_2_table.pack(side=tk.TOP, expand=tk.YES, fill=tk.X)
        self.tab_2_scrollable_body.update()


        self.root = master

    def tab_1_selectfolder(self):
        """
        Выбираем папку с файлами
        """
        self.tab_1_path.set(filedialog.askdirectory())
    
    def tab_1_loadfiles(self):
        """
        Добавить файлы из папки
        """
        list_file = pdf_combiner.get_file_from_dir(self.tab_1_path.get())
        
        for path_file in list_file:
            self.tab_1_table.add_line_end((path_file,))
        
        self.tab_1_scrollable_body.update()
    
    def tab_1_execute(self):
        """
        Выполняем объединение файлов в один
        """
        list_file = self.tab_1_table.get_true_lines()
        clean_list_file = []
        for line in list_file:
            clean_list_file.append(line[0])

        if clean_list_file:
            pdf_combiner.create_from_files(tuple(clean_list_file), self.tab_1_path.get())

    def tab_1_cleaner(self):
        """
        Отчищаем таблицу от файлов
        """
        self.tab_1_table.cleaning()
        self.tab_1_scrollable_body.update()
    
    def tab_2_selectfolder(self):
        """
        Выбираем папку с файлами
        """
        self.tab_2_path.set(filedialog.askdirectory())
    
    def tab_2_loadfiles(self):
        """
        Добавить файлы из папки
        """
        list_file = image_to_pdf.get_file_from_dir(self.tab_2_path.get())
        
        for path_file in list_file:
            self.tab_2_table.add_line_end((path_file,))
        
        self.tab_2_scrollable_body.update()
    
    def tab_2_execute(self):
        """
        Выполняем объединение файлов в один
        """
        list_file = self.tab_2_table.get_true_lines()
        clean_list_file = []
        for line in list_file:
            clean_list_file.append(line[0])

        if clean_list_file:
            image_to_pdf.create_from_files(tuple(clean_list_file), self.tab_2_path.get())

    def tab_2_cleaner(self):
        """
        Отчищаем таблицу от файлов
        """
        self.tab_2_table.cleaning()
        self.tab_2_scrollable_body.update()


if __name__ == "__main__":
    root = tk.Tk()
    first_win = Mywindow(root)
    root.mainloop()
