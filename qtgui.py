import sys
import mysql.connector
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMenu, QFrame, QAction
from PIL import Image, ImageQt

class DatabaseConnection:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor(dictionary=True)

db_connection = DatabaseConnection(host='localhost', user='root', password="", database='pharmgui')

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Mckesson Rx Enterprise - Login"
        self.setGeometry(100, 100, 750, 500)
        self.setWindowTitle(self.title)

        self.setStyleSheet("background-color: white;")

        self.orange = QLabel('World Class Pharmacy Systems', self)
        self.orange.setStyleSheet('font-size: 18px; color: white; background-color: #DA7533;')
        self.orange.setGeometry(0, 150, 800, 30)

        self.Mick = QLabel(self)
        mick_image = QImage("Mickey.png")
        self.Mick.setPixmap(QPixmap.fromImage(mick_image).scaled(183, 43))
        self.Mick.setGeometry(4, 60, 183, 43)

        self.Pillori = QLabel(self)
        pillori_image = QImage("pillbottlesblurgrey.png")
        self.Pillori.setPixmap(QPixmap.fromImage(pillori_image))
        self.Pillori.setGeometry(0, 175, pillori_image.width(), pillori_image.height())

        self.Username_Entry = QLineEdit(self)
        self.Password_Entry = QLineEdit(self)
        self.Username_Entry.setGeometry(290, 250, 200, 25)
        self.Username_Entry.setStyleSheet("color: black; font: 12pt 'Vintage Typewriter';")
        self.userlabel = QLabel('Username', self)
        self.userlabel.setStyleSheet("color: black; background-color:transparent;font: 12pt 'Vintage Typewriter'; font-style: italic;")
        self.userlabel.setGeometry(220,250,75,25)

        self.Password_Entry.setStyleSheet("color: black; font: 12pt 'Vintage Typewriter'; font-style: italic;")
        self.Password_Entry.setGeometry(290, 285, 200, 25)
        self.passlabel = QLabel('Password', self)
        self.passlabel.setStyleSheet("color: black; background-color:transparent;font: 12pt 'Vintage Typewriter'; font-style: italic;")
        self.passlabel.setGeometry(220,285,75,25)

        self.messlabel = QLabel('Enter your Username and Password to log in', self)
        self.messlabel.setStyleSheet("color: black; background-color:transparent;font: 12pt 'Vintage Typewriter'; font-style: italic;")
        self.messlabel.setGeometry(210,220,260,25)
        # Retry counter for database connection attempts
        self.retry_counter = 0

        self.Username_Entry.installEventFilter(self)
        self.Password_Entry.installEventFilter(self)

        self.log_button = QPushButton('Login', self)
        self.log_button.setGeometry(330, 340, 70, 25)
        self.log_button.setStyleSheet("color: black; font: 12pt")

        self.log_button.clicked.connect(self.correct_login)


    def correct_login(self):
        username = self.Username_Entry.text()
        password = self.Password_Entry.text()

        try:
            db_connection.cursor.execute('SELECT Username, Password FROM UserEntry WHERE Username = %s AND Password = %s', (username, password))
            result = db_connection.cursor.fetchone()

            if result:
                # Close the database cursor and connection
                db_connection.cursor.close()
                db_connection.close()

                # Create the main window
                self.main_window = MainWindow()
                self.main_window.show()
                self.hide()
            else:
                incorrect = QLabel("Incorrect Username/Password", self)
                incorrect.setStyleSheet('font-size: 11px; color: red;')
                incorrect.setGeometry(290, 300, 200, 25)
                self.layout().addWidget(incorrect)  # Add the error message to the layout
                # Remove the error message after a certain time
                QTimer.singleShot(5000, incorrect.deleteLater)  # Hide the error message after 5 seconds

        except mysql.connector.Error as err:
            if self.retry_counter < 2:  # Retry up to 2 times
                self.retry_counter += 1
                self.correct_login()  # Retry the login attempt
            else:
                # Display error message in a dialog box
                error_dialog = QDialog(self)
                error_dialog.setWindowTitle("Database Error")
                error_label = QLabel(f"Error connecting to the database: {err}", error_dialog)
                error_label.setStyleSheet('font-size: 11px; color: red;')
                error_label.setGeometry(10, 10, 300, 50)

                retry_button = QPushButton("Retry", error_dialog)
                retry_button.setGeometry(100, 70, 70, 25)
                retry_button.clicked.connect(lambda: self.correct_login())  # Reconnect and retry login

                cancel_button = QPushButton("Cancel", error_dialog)
                cancel_button.setGeometry(180, 70, 70, 25)
                cancel_button.clicked.connect(error_dialog.close)

                error_dialog.exec()

                self.retry_counter = 0  # Reset retry counter after displaying error






        # Add event handlers for menu actions
