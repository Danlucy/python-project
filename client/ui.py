from flet import *
import flet_core.control_event as ControlEvent

class UI(UserControl):
    def build(self) -> Container:
       #Text fields
        self.text_userName: TextField = TextField(label="User name", width=300)
        self.text_password: TextField = TextField(label="Password", width=300, password=True)

        #Buttons
        self.button: ElevatedButton = ElevatedButton(text='Log In', width=300, disabled=True)

        #Logic implementation
        self.text_userName.on_change = self.validate
        self.text_password.on_change = self.validate
        self.button.on_click = self.submit  

        #Image
        image = Image(
            src=r'C:\Users\danie\VSCProjects\python-project\client\front_image.jpg',
            height=400,
            width=400,
            opacity=0.5,  
            border_radius=border_radius.all(200), 
        )

  
        text = Container(content=Text('Library of Alexandria', size=20, color='blue800'))

        #Returning UI
        return Column( horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[image,Container(
            content=Row(
                controls=[
                    Column(
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        controls=[text, self.text_userName, self.text_password, self.button],
                        alignment=CrossAxisAlignment.CENTER
                    )
                ],
                alignment=MainAxisAlignment.CENTER
            ),
            bgcolor='amber50',
            border_radius=border_radius.all(30),
            padding=padding.all(20)
        )])
    
    #Logic
    def validate(self,e :ControlEvent) -> None:
        if all([self.text_userName.value, self.text_password.value]):
            self.button.disabled = False
        else:
            self.button.disabled = True

        self.update()

    def submit(self, e :ControlEvent) -> None:
        print(f"User name: {self.text_userName.value}")
        print(f"Password: {self.text_password.value}")
        self.clean()
        self.page.add(HomeUI())

class HomeUI (UserControl):
    
    def build(self):
        
        textfield = TextField(label='Search', width=300, border=InputBorder.UNDERLINE,
            filled=True,)
        return Row(controls=[Column(
            controls=[textfield],expand=True,
         alignment=CrossAxisAlignment.START,horizontal_alignment=MainAxisAlignment.CENTER
            )  ],vertical_alignment=MainAxisAlignment.CENTER,alignment=CrossAxisAlignment.CENTER    ,expand=True, )


def main(page: Page):
    
    page.title = "Library of Alexandria"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.theme_mode = ThemeMode.LIGHT
    page.window_resizable = False
    login= UI()
    page.add(login)

if __name__ == "__main__":
    print('Running login screen...')
    app(target=main)
