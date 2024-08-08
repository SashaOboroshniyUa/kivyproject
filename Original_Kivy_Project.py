from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.size = (1920, 1080)
class FinanceManagerApp(App):

    def build(self):
        self.balance = 0
        self.incomes = []
        self.expenses = []
        root = BoxLayout(orientation='vertical')
        input_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, None), height=40)
        self.sum_input = TextInput(hint_text='Сума', multiline=False, input_type='number')
        self.source_input = TextInput(hint_text='Джерело', multiline=False)
        self.sourc_input = TextInput(hint_text='Категорія', multiline=False)
        input_layout.add_widget(self.sum_input)
        input_layout.add_widget(self.source_input)
        input_layout.add_widget(self.sourc_input)
        add_income_button = Button(text='Добавити прибуток', size_hint=(1, None), height=40)
        add_income_button.bind(on_press=self.add_income)
        add_button = Button(text='Добавити видаток', size_hint=(1, None), height=40)
        add_button.bind(on_press=self.add_expense)
        self.balance_label = Label(text=f'Баланс: {self.balance}', size_hint=(1, 1), halign='center',
                                   valign='middle')
        root.add_widget(input_layout)
        root.add_widget(add_income_button)
        root.add_widget(add_button)
        root.add_widget(self.balance_label)

        return root

    def add_income(self, instance):
        try:
            amount = float(self.sum_input.text)
            source = self.source_input.text
            self.incomes.append({'sum': amount, 'source': source})
            self.balance += amount
            self.update_balance_label()
        except ValueError:
            pass

    def add_expense(self, instance):
        try:
            amount = float(self.sum_input.text)
            category = self.source_input.text
            if self.balance - amount >= 0:
                self.expenses.append({'sum': amount, 'category': category})
                self.balance -= amount
                self.update_balance_label()
        except ValueError:
            pass

    def update_balance_label(self):
        self.balance_label.text = f'Текущий баланс: {self.balance}'


if __name__ == "__main__":
    FinanceManagerApp().run()
