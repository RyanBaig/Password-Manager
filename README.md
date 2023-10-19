# Password Manager GUI Application

A simple password manager GUI application built using Python's Tkinter library for creating graphical user interfaces.

## Description

This repository contains a basic password manager application that allows users to store and manage their passwords along with corresponding email addresses. The application provides the following features:

- Add new passwords along with associated email addresses and password locations.
- View stored passwords and associated email addresses.
- Delete stored password information based on password location.

## Usage

To run the application, follow these steps:

1. Make sure you have Python installed on your machine.
2. Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/RyanBaig/password-manager.git
```
3. Navigate to the repository directory:
```bash
cd password-manager
```
4. Run the application:
```bash
python main.py
```
5. The application window will open, presenting two tabs: "Add Passwords" and "View Passwords."

6. In the "Add Passwords" tab, you can enter the password location, email, and password. Click the "Submit" button to save the information.

7. In the "View Passwords" tab, you can select a password location from the dropdown and click the "Retrieve" button to view the associated email and password. You can also delete stored information using the "Delete" button.

## Dependencies
The application uses the following Python libraries:

- tkinter: Python's standard GUI library for creating graphical user interfaces.
- ttkbootstrap: For Styling tkinter's GUI.
- pickle: Python's serialization module for saving and loading data in binary format.
- os: Python's library for interacting with the operating system.
- sys: Python's library for system-specific functions and parameters.
- ttk: Tkinter's themed widget library.
- messagebox: Tkinter's module for displaying dialog boxes.
- info.pkl: Stores the information in binary/machine language.
  
## Disclaimer
This application is meant for educational purposes and should not be used as a secure password management solution for sensitive data. It lacks encryption and other security features found in professional password managers.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
