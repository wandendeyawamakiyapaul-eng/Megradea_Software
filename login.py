from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.uix.button import Button
import image_select

KV = '''
ScreenManager:
    LoginScreen:
    SignUpScreen:
    ProgramMenuScreen:
    
<ProgramMenuScreen>:
    name: "program_menu_screen"
    
    BoxLayout:
        orientation: 'vertical'
        padding: dp(80)
        spacing: dp(200)
     

        BoxLayout:
            size_hint_y: None
            height: dp(60)
            padding: dp(10)
            spacing: dp(0)
            Label:
                text: "School Object Model"
                font_size: '20sp'
                halign: 'left'
                valign: 'middle'
                size_hint_x: None
                width: dp(200)
            ImageSelect:
                source: 'storage/emulated/0/DCIM/Camera'
                size_hint_x: .1
                allow_stretch: False
                keep_ratio: False
            Button:
                text: "Menu"
                size_hint: (None, 1)
                width: dp(100)
                on_release: app.show_menu()

        Label:
            text: "SOM"
            halign: "center"
            size_hint_y: None
            height: dp(80)
            color: 1, 1, 1  # background color
        


<LoginScreen>:
    name: "login_screen"

    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(10)
        

        MDLabel:
            text: "Megradea App"
            halign: "center"
            font_style: "H5"

        BoxLayout:
            orientation: 'horizontal'
            spacing: dp(10)
            MDLabel:
                text: "Name"
            MDTextField:
                id: name_field
                hint_text: "Enter Name"

        BoxLayout:
            orientation: 'horizontal'
            spacing: dp(10)
            MDLabel:
                text: "PIN"
            MDTextField:
                id: pin_field
                hint_text: "Enter PIN"
                password: True

        Spinner:
            id: account_type_spinner
            text: "Select Account Type"
            values: ["Teacher", "Learner", "Parent", "Stakeholder", "President", " Minister", "PS", " Commossioner", " Inspector Schools", "CAO", " DEO", "Sponsor", "Donor"]

        MDRaisedButton:
            text: "Login"
            on_release: app.sign_in(name_field.text, pin_field.text, account_type_spinner.text)

        MDLabel:
            text: "Already have an account?"
            halign: "center"
            theme_text_color: "Secondary"

        BoxLayout:
            orientation: 'horizontal'
            spacing: dp(10)
            MDRaisedButton:
                text: "Sign In"
                on_release: app.root.current = "login_screen"

            MDRaisedButton:
                text: "Sign Up"
                on_release: app.root.current = "sign_up_screen"

<SignUpScreen>:
    name: "sign_up_screen"

    BoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)

        MDLabel:
            text: "Sign Up"
            halign: "center"
            font_style: "H5"

        ImageSelect:  # Use ImageSelect  <-------------------------------------------------

        MDTextField:
            id: school_name_field
            hint_text: "School Name"

        MDTextField:
            id: school_id_field
            hint_text: "School ID"

        MDTextField:
            id: name_field
            hint_text: "Name"

        MDTextField:
            id: pin_field
            hint_text: "Pin"
            password: True

        MDTextField:
            id: confirm_id_field
            hint_text: "Confirm Pin"
            password: True

        Spinner:
            id: account_type_spinner
            text: "Select Account Type"
            values: ["Teacher", "Learner", "Parent", "Stakeholder", "President", " Minister", "PS", " Commossioner", " Inspector Schools", "CAO", " DEO", "Sponsor", "Donor"]


        MDRaisedButton:
            text: "Create Account"
            disabled: not root.inputs_complete(school_name_field.text, school_id_field.text, name_field.text, pin_field.text, confirm_id_field.text, account_type_spinner.text)
            on_release: app.create_account(school_name_field.text, school_id_field.text, name_field.text, pin_field.text, confirm_id_field.text, account_type_spinner.text)
'''


class LoginScreen(Screen):
    pass


class SignUpScreen(Screen):
    def inputs_complete(self, school_name, school_id, name, pin, confirm_id, account_type):
        return all([school_name, school_id, name, pin, confirm_id,
                    account_type != "Select Account Type", pin == confirm_id])

class ProgramMenuScreen(Screen):
    pass
    
class UserInfoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        return Builder.load_string(KV)

    def sign_in(self, name, pin, account_type):
        # Implement sign-in logic here
        if all([name, pin, account_type != "Select Account Type"]):
            # Show dialog or navigate to the next screen
            self.root.current = "program_menu_screen"  # Corrected screen name
        else:
            self.show_dialog("Sign In Failed", "Please fill in all fields correctly.")

    def create_account(self, school_name, school_id, name, pin, confirm_id, account_type):
        if all([school_name, school_id, name, pin, confirm_id, account_type != "Select Account Type",
                pin == confirm_id]):
            # Perform account creation logic here
            self.show_dialog("Account Creation Successful",
                             f"Account created for {name} at {school_name} as a {account_type}.")
        else:
            self.show_dialog("Account Creation Failed", "Please fill in all fields correctly.")

    def show_dialog(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            buttons=[
                Button(
                    text="Close",
                    on_release=lambda x: dialog.dismiss()
                ),
            ],
        )
        dialog.open()
    def save_user_data(self, filename, data):
        if not Path(filename).is_file():
            # is the file does not exist, put the data in a list and save it and return.
            with open(filename, 'w') as f:
                json.dump([data], f)
            return
        # if the file does exist, read it, append the data to the list and save it.
        with open(filename, 'r') as f:
            users = json.load(f)

        users.append(data)
        with open(filename, 'w') as f:
            json.dump(users, f)


if __name__ == "__main__":
    UserInfoApp().run()