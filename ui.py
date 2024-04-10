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
            src=r'C:\Users\danie\VSCProjects\python-project\lib\front_image.jpg',
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
        self.page.add(Row(controls=[Text(value=f'Welcome {self.text_userName.value}', size=20)]))

  
    
    
