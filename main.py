from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.graphics import Color, Rectangle
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# Definición de la clase "Inicio" que hereda de "Screen" en KivyMD
class Inicio(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Agregar un Widget que sirva como fondo con el tema Turquoise
        background = RelativeLayout()
        with background.canvas.before:
            Color(64/255, 224/255, 208/255, 1)  # Color de fondo Turquesa
            self.rect = Rectangle(size=(Window.width, Window.height))

        label = Label(
            text=" DOMUSTRACK \n      SYSTEM",
            font_name="Arial",
            font_size=32,
            size_hint_y=None,
            height=dp(900),
            color=(0, 0, 0.3, 1)
        )

        container = RelativeLayout(size_hint_y=None, height=dp(60))

        image = Image(
            source='cerebro.png',
            size_hint=(None, None),
            size=(dp(250), dp(250)),
            pos_hint={'center_x': 0.5, 'center_y': 4.5}  # Posición de la imagen
        )

        button = Button(
            text="INICIAR SESIÓN",
            font_name="Arial",
            font_size=24,
            size_hint=(None, None),
            size=(dp(200), dp(60)),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},  # Posición del botón
        )

        button.background_color = (1, 1, 0, 1)  # Color de fondo del botón
        button.bind(on_press=self.show_login_screen)  # Asociar evento de clic a una función

        container.add_widget(image)
        container.add_widget(button)

        background.add_widget(container)

        self.add_widget(background)
        self.add_widget(label)

    def show_login_screen(self, instance):
        self.parent.current = 'login'  # Cambiar a la pantalla de inicio de sesión

# Definición de la clase "LoginScreen" que hereda de "Screen" en Kivy
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Fondo turquesa para la pantalla de inicio de sesión
        background = RelativeLayout()
        with background.canvas.before:
            Color(64/255, 224/255, 208/255, 1)  # Color de fondo Turquesa
            self.rect = Rectangle(size=(Window.width, Window.height))

        # Diseño para la pantalla de inicio de sesión
        layout = BoxLayout(orientation='vertical', padding=dp(48), spacing=dp(16))

        title_label = Label(
            text="DOMUSTRACK SYSTEM",
            font_name="Arial",
            font_size=32,
            color=(0, 0, 0.3, 1)
        )

        username_label = Label(
            text="Usuario",
            font_size=20,
            color=(0, 0, 0.3, 1)
        )

        self.username_input = TextInput(
            hint_text='Ingrese su usuario',
            font_size=20
        )

        password_label = Label(
            text="Contraseña",
            font_size=20,
            color=(0, 0, 0.3, 1)
        )

        self.password_input = TextInput(
            hint_text='Ingrese su contraseña',
            password=True,
            font_size=20
        )

        login_button = Button(
            text="ENTRAR",
            font_name="Arial",
            font_size=24,
            size_hint=(None, None),
            size=(dp(200), dp(60)),
            pos_hint={'center_x': 0.5},
        )

        login_button.background_color = (1, 1, 0, 1)  # Color de fondo del botón
        login_button.bind(on_press=self.login)  # Asociar evento de clic a una función

        layout.add_widget(title_label)
        layout.add_widget(username_label)
        layout.add_widget(self.username_input)
        layout.add_widget(password_label)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)

        background.add_widget(layout)

        self.add_widget(background)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        # Realiza la lógica de inicio de sesión aquí (verificar nombre de usuario y contraseña)
        if username == 'conusion' and password == 'hola':
            self.add_widget(Label(text='Inicio de sesión exitoso', font_size=16))
        else:
            self.add_widget(Label(text='Nombre de usuario o contraseña incorrectos', font_size=16))

# Clase principal de la aplicación
class MyApp(App):
    def build(self):
        sm = ScreenManager()

        # Definir la pantalla de inicio
        inicio_screen = Inicio(name='inicio')
        sm.add_widget(inicio_screen)

        # Definir la pantalla de inicio de sesión
        login_screen = LoginScreen(name='login')
        sm.add_widget(login_screen)

        return sm

# Ejecutar la aplicación si este archivo es el punto de entrada
if __name__ == '__main__':
    Window.size = (dp(300), dp(450))
    app = MyApp()
    app.run()
