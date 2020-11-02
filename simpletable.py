#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
HEADER = 0
BODY = 1
# COLUMN1 = 0
# COLUMN2 = 1
# COLUMN3 = 2
# CHECKVAR = 1
# WIDGET = 0


class SimpleTable(tk.Frame):
    def __init__(self, parent, column_names, rows=10, checkbox=True):
        """
        параметры:
            @parent - tkframe родителя, в которого отрисовываем таблицу
            @column_names - название колонок
            @rows - Количество начальных строк в body таблицы
        """
        tk.Frame.__init__(self, parent, background="black")
        count_column = len(column_names) + int(checkbox)
        # В первом списке всего одна строка - шапка
        # Во втором списке остальные строки таблицы (часть body)
        self.widgets = [[], []]
        self.vars = [[], []]
        self.checkbox = checkbox
        self.__END = 0
        self.count_column = count_column
        self.column_names = column_names
        # hrader
        self.__add_header()
        # body
        for row in range(1, rows+1):
            self.__add_line_end(row)

        for column in range(count_column):
            if column == count_column-int(checkbox):
                self.grid_columnconfigure(column, weight=0)
            else:
                self.grid_columnconfigure(column, weight=1)

        # Добавляем события копирования при русской раскладке
        self.event_add('<<Paste>>', '<Control-igrave>')
        self.event_add("<<Copy>>", "<Control-ntilde>")

    def set_in_body(self, row, column, value):
        """
        устанавливаем значение в определенную ячейку
        """
        var = self.vars[BODY][row][column]
        var.set(value)

    def __add_header(self):
        """
        Создаем шапку таблицы
        """
        count_column = self.count_column
        checkbox = self.checkbox
        column_names = self.column_names

        current_row_widgets = []
        current_row_values = []

        for column in range(count_column):
            if column == count_column-int(checkbox):
                check_var = tk.BooleanVar()
                check_button_widget = tk.Checkbutton(
                    self, text="", variable=check_var, onvalue=1, offvalue=0,
                    command=self.get_obr_header())
                check_button_widget.grid(row=0, column=column, sticky="e", padx=1,
                                         pady=1)
                current_row_widgets.append(check_button_widget)
                current_row_values.append(check_var)
            else:
                entry_var = tk.StringVar()
                entry_widget = tk.Entry(
                    self, text=entry_var, borderwidth=0,
                    width=30, justify=tk.CENTER, state='readonly')
                entry_widget.grid(row=0, column=column, sticky="nsew", padx=1, pady=1)
                entry_var.set(column_names[column])
                current_row_widgets.append(entry_widget)
                current_row_values.append(entry_var)

        self.widgets[HEADER].append(current_row_widgets)
        self.vars[HEADER].append(current_row_values)

    def add_line_end(self, values):
        """
        Добавляем запись в конец таблицы
        Тут расчитываются все необходимые параметры
        """
        self.__END += 1
        self.__add_line_end(self.__END, values)

    def __add_line_end(self, row, values=None):
        """
        Добавляем запись в конец таблицы
        """
        count_column = self.count_column
        checkbox = self.checkbox

        current_row_widgets = []
        current_row_values = []

        for column in range(count_column):
            if column == count_column-int(checkbox):
                check_var = tk.BooleanVar()
                check_button_widget = tk.Checkbutton(
                    self, text="", variable=check_var, onvalue=1, offvalue=0,
                    command=self.get_obr_body(row-1))
                check_button_widget.grid(
                    row=row, column=column, sticky="e", padx=1, pady=1)
                current_row_widgets.append(check_button_widget)
                current_row_values.append(check_var)
            else:
                entry_var = tk.StringVar()
                entry_widget = tk.Entry(
                    self, text=entry_var, borderwidth=0,
                    width=30, justify=tk.LEFT, state='readonly')
                entry_widget.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                if values:
                    entry_var.set(values[column])
                else:
                    entry_var.set("%s/%s" % (row-1, 0))
                current_row_widgets.append(entry_widget)
                current_row_values.append(entry_var)

        self.widgets[BODY].append(current_row_widgets)
        self.vars[BODY].append(current_row_values)

    def get_obr_body(self, row):
        """
        Это замыкание.
        Оно создаёт для каждого чекбокса (в body таблици) свою функцию,
        которую связывает по указанной строке при инициализации
        """
        count_column = self.count_column

        def eventcheck():
            """
            Выполняет переключение чекбокса в одной строке body таблицы
            """
            var = self.vars[BODY][row][-1]
            if var.get():
                for i in range(count_column-1):
                    widget = self.widgets[BODY][row][i]
                    widget.config(state='normal')
            else:
                for i in range(count_column-1):
                    widget = self.widgets[BODY][row][i]
                    widget.config(state='readonly')

        return eventcheck

    def get_obr_header(self):
        """
        Это замыкание.
        Оно создаёт функцию для чекбокса в header
        """
        count_column = self.count_column

        def eventcheck():
            """
            Выполняет переключение всех чекбоксов в body таблицы
            Выполняет переключение доступности поля в колонке 2
            """
            var_head = self.vars[HEADER][0][-1]
            value_head = var_head.get()
            for row_i in range(len(self.widgets[BODY])):
                if not self.vars[BODY][row_i]:
                    continue
                var_line = self.vars[BODY][row_i][-1]
                if value_head != var_line.get():
                    widget_check = self.widgets[BODY][row_i][-1]
                    if value_head == 0:
                        widget_check.deselect()
                        for column_i in range(count_column-1):
                            widget = self.widgets[BODY][row_i][column_i]
                            widget.config(state='readonly')
                    else:
                        widget_check.select()
                        for column_i in range(count_column-1):
                            widget = self.widgets[BODY][row_i][column_i]
                            widget.config(state='normal')

        return eventcheck
    
    def cleaning(self):
        """
        Отчистка таблицы от записей. Удаление виджетов.
        """
        widgets = self.widgets[BODY]
        for row_widgets in widgets:
            if row_widgets:
                for widget in row_widgets:
                    widget.destroy()
        
        self.widgets[BODY] = list()
        self.vars[BODY] = list()

    def get_true_lines(self):
        """
        Возвращает матрицу (кортеж кортежей) в которой находятся
        значения строк с отмечеными чекбоксами
        """
        checkbox = self.checkbox
        count_column = self.count_column - int(checkbox)

        table = []
        
        for vars_line in self.vars[BODY]:
            if not checkbox or (vars_line and vars_line[-1].get()):
                line = tuple(vars_line[i_var].get() for i_var in range(count_column))
                table.append(line)
        
        return tuple(table)

    @property
    def END(self):
        return self.__END


if __name__ == "__main__":
    class ExampleApp(tk.Tk):
        def __init__(self):
            tk.Tk.__init__(self)
            self.table = SimpleTable(
                self, ["Original value", "Translate value"], 10)
            self.table.pack(side="top", fill="x")
            self.table.set_in_body(6, 1, "1111")

    app = ExampleApp()
    app.mainloop()
