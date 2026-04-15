This readme file was generated on 2026-04-10 by Wandendeya Paul Wamakiya


GENERAL INFORMATION

Project name: Magredea Software
Version: v1

Short description: This is a school tool for manipulate and access of attendance and performance of each child in a school

PROJECT OVERVIEW

Full description: The project shall track the attendance, performance marks and grades of each child in the school.
The software program shall improve academic standards by ensuring that teachers are marking exercises, homework assignment, progress test, and examination, each mark is recorded and tracked and that parents and schools can monitor their progress. Daily attendance is also recorded, and monthly termly reports will be generated sent to parents, including stakeholders and sponsor, by online/ by post and by phone. 
This will allow parents to react to and manage poor performance and truancy issues in a timely fashion, thereby reducing dropouts in the academics.
Date of creation: 2026-Apr-20 - 2026-Sep-20
- Project Organization: Megradea

- Step by step instructions: 
- System requirements: Windows, Linux, 16, 64GB
Required libraries, packages, modules: Python pip, Mysql, redis-py, kivyMD
Setup requirements: 
REDIS Server, SDK, Python, vs
- Step by step instructions: 
   
https://drive.google.com/file/d/1pQ7ufCFO6p5W7E4W0dzyyl0VXC-8n9Ub/view?usp=drivesdk
    
 Here is a clear, step-by-step guide for someone using the app, based on the code and UI provided:

Step-by-step User Guide

1. Launch the App

Open (run) your app.
You’ll see the Login Screen.


2. Login or Sign Up
A. Login (Existing Users)
- Enter your Name in the Name field.
- Enter your PIN*l in the PIN field.
- Click the "Select Account Type" drop-down and choose your role (for example, Teacher, Learner, etc.).
- Press Login.
    - If you filled all fields and the PIN/account type is valid, you’ll be taken to the Program Menu screen.
    - If not, a dialog will appear saying "Sign In Failed".

If you don’t have an account:
- Click the Sign Up button at the bottom.  
- (Or if already on the Sign Up screen, you can click "Sign In" button at bottom to get back to Login.)

---

B. Sign Up (New Users)
- Fill in these fields:
    - School Name
    - School ID
    - Name (Your own name)
    - Pin (Choose a secret code)
    - Confirm Pin (Must match the PIN you just set)
    - Select Account Type (choose your role)
- (You may also have an image select component for profile/school image, if implemented.)


3. Select an Image File.

 Image Selection:
   - When the application starts, you will see a button labeled "Select Image".
   - Click on the "Select Image" button to open the file chooser popup.

4. File Chooser Popup:
   - In the file chooser popup window that appears:
     - You can navigate to the directory where your images are located.
     - The default path is set to '/storage/emulated/0/DCIM/Camera'.
     - Only files with extensions '.jpg' and '.png' will be displayed in the file list.

5. Selecting an Image:
   - Browse through the files using the file chooser.
   - Click on the image file you want to select.
   - Click the "Open" button to select the image.
   - The selected image will be displayed on the screen.

6. Cancel Operation:
   - If you decide not to select an image, click the "Cancel" button to close the file chooser popup without selecting any image.

7. Changing the Image:
   - If you want to select a
 different image, click the "Select Image" button again to open the file chooser and select a new image.
- When all fields are filled and pins match, the Create Account button becomes clickable.
- Click Create Account.
    - If info is complete and PINs match, a dialog says account creation successful.
    - If not, a dialog says “Account creation failed.”

8. After Login: Main Menu

- If you logged in successfully, you are taken to the Program Menu Screen.
- Here, you’ll see:
    - App title and logo/image.
    - The "Menu" button (sample).
    - The program/navigation drawer title ("SOM" label).

- The Navigationdrawer button is meant to show further navigation, though its function is a stub in your code.


9. Return/Navigate

- To sign out or return, you’d need to implement a back or logout function.  
- The code does not currently create new screens beyond the Program Menu.

Summary Table

| Step            | What to Do                                              | Result                                                                  |
|-----------------|--------------------------------------------------------|-------------------------------------------------------------------------|
| Start app   | Open/run app                                           | See Login screen                                                        |
| Login       | Input Name, PIN, pick Account Type, click Login        | Go to Program Menu if correct; else see an error dialog                 |
| Switch screens | Click Sign Up at Login, or Sign In at Sign Up       | Move between Login/Sign Up screens                                      |
| Sign up     | Fill in School Name, School ID, Name, Pin, Confirm Pin, Account Type, then click Create Account | Success or failure dialog, then return to login and can re-log in       |
| After Login | Use Menu/Main screen                                   | (Menu button and layout, for future features)                           |


EXTRA TIPS

- The app is designed for basic school-user logins: teacher/learner/parent/etc.
- All input fields must be complete to enable account creation.
- PIN and Confirm PIN must match on Sign Up.
- Selecting the right Account Type is mandatory.


LICENSE

-  Software License: BY
CC-BY Commercial Use 4.0
        
-  Preferred citation: <Provide a citation that users can reference in publications>


CONTACT INFORMATION

Contact
Name: Wandendaye Paul Wandendeya
Role:  copyright owner
ORCID: 0009-0006-0412-3106
https://orcid.org/0009-0006-0412-3106
Institution: Mudaddi prod's Ltd
Email: wandendeyawamakiyapaul@gmail.com/mudaddp@rocketmail.com

Contact
Name:Elliot Garbus
Role: maintainer
ORCID:
Institution: Kivy.org
Email: elliot


ACKNOWLEDGEMENTS

- Funding:
NASA FUNDS
UNESCO FUNDS
STATE HOUSE GRANTs
NASE
- Publications using our software: 
 *Cite any publications using* this software project:
- Project is available: zenodo, github, google play/store, plasma store, Microsoft store, airtel store, mtn store, safari com store.

 *Related relationships* 

Let's bring Socratic education system to life.

The system likely involves tracking student attendance, performance, and engagement. Here are some ancillary scripts, applications, and data sets that might be relevant:

- *Attendance Tracking (Script)*: A script that logs student attendance, perhaps using facial recognition. Think of it as the digital roll call.
- *Performance Analytics (Application)*: A dashboard that analyzes student performance, highlighting areas of strength and weakness. It's like having a personal tutor.
- *Student Profiles (Data Set)*: A database storing student information, including attendance, grades, and learning habits. This is the central hub of your system
 Data Set: A database outlining learning objectives, outcomes, and assessments. It's the roadmap for your education system.
- *Notification System (Script)*: A script that sends alerts to parents, teachers, or administrators about student progress or attendance issues. Think of it as the messenger.
- *Remote Dictionary Server (REDIS) Integration (Application)*: Integration with an Redis  server to store and retrieve data. It's like having a virtual classroom.
- *Assessment Tools (Script)*: Scripts that generate quizzes, tests, or assignments to evaluate student understanding. Think of it as the digital exam room.

These components work together to create a comprehensive education system. By integrating these scripts, applications, and data sets, you can:

- Track attendance and engagement
- Analyze student performance
- Personalize learning experiences
- Streamline communication
- Enhance assessment and evaluation


- Contributors: 
   -Elliot Garbus providing feedback guidance on how to fix issue. Edit, perform action, create pull request and merge changes.
 - Carl Hostetter provide data expertise, feedback to the results, specialized expertise and support, creating tools essential for carrying on project activities.
 - Guy Rouse provide feedback to the results, handle issues relented to integrating mobile apo with redis server, open a connection and store and display datasets.

