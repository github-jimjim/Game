import datetime
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import pygame
import random
from cryptography.fernet import Fernet
import sys
import time
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QDialog
from screeninfo import get_monitors

window = tk.Tk()
window.withdraw()

key = b'cSimLy4xjxpi1G1TVNoO-cOdaJZoOR8BUglMqUemvOM='
cipher_suite = Fernet(key)


def encrypt(message):
    return cipher_suite.encrypt(message.encode())


def decrypt(token):
    return cipher_suite.decrypt(token).decode()


Tickets = messagebox.askyesno("Tickets", "Do you have already enought tickets?")
if not Tickets:
    key = b'cSimLy4xjxpi1G1TVNoO-cOdaJZoOR8BUglMqUemvOM='
    cipher_suite = Fernet(key)


    def encrypt(message):
        return cipher_suite.encrypt(message.encode())


    def decrypt(token):
        return cipher_suite.decrypt(token).decode()


    try_again = True
    streak = 0
    total_attempts = 0
    total_tickets = 0
    time_limit = 30


    def update_tickets(result):
        global total_tickets
        if streak < 5:
            total_tickets += 0
        elif streak > 4:
            total_tickets += (streak - 5)
        else:
            print("Error")


    def save_game_stats(total_tickets):
        try:
            with open('game_stats.txt', 'rb') as file:
                encrypted_data = file.read()
                decrypted_data = decrypt(encrypted_data)
                previous_tickets = int(decrypted_data)
        except FileNotFoundError:
            previous_tickets = 0

        new_total_tickets = previous_tickets + int(total_tickets)

        with open('game_stats.txt', 'wb') as file:
            encrypted_data = encrypt(str(new_total_tickets))
            file.write(encrypted_data)

        messagebox.showinfo("Maths Game", f"Total Tickets: {new_total_tickets}")


    def load_game_stats():
        global total_tickets
        try:
            with open('game_stats.txt', 'rb') as file:
                encrypted_data = file.read()
                decrypted_data = decrypt(encrypted_data)
                messagebox.showinfo("Maths Game", "Ticket/s: " + decrypted_data)
                tickets_split = decrypted_data.split(": ")
                if len(tickets_split) >= 2:
                    total_tickets = int(tickets_split[1])
                else:
                    total_tickets = 0
        except FileNotFoundError:
            messagebox.showinfo("Maths Game",
                                "No previous game stats found. So you are new. For each question you have 30 seconds.")


    load_game_stats()

    root = tk.Tk()
    root.withdraw()

    while try_again:
        random_arithmetic_operation = random.choice(["+", "-", "*", "/", "**"])
        start_time = datetime.datetime.now()
        total_attempts += 1

        if random_arithmetic_operation == "+":
            random_number_plus = random.randint(1, 1000)
            random_number2_plus = random.randint(1, 1000)
            result_plus = random_number_plus + random_number2_plus
            input_plus = simpledialog.askinteger("Maths Game",
                                                 "Give the result! " + str(random_number_plus) + " + " + str(
                                                     random_number2_plus) + ": ")
            if input_plus == result_plus:
                end_time = datetime.datetime.now()
                elapsed_time = end_time - start_time

                if elapsed_time.total_seconds() > time_limit:
                    messagebox.showinfo("Time's up!", "Time's up!")
                    streak = 0
                    update_tickets(False)
                else:
                    messagebox.showinfo("Congratulations", "Congratulations. Your answer is correct.")
                    streak += 1
                    update_tickets(True)
                    messagebox.showinfo("Streak", "You have solved " + str(streak) + " in one go.")
                    if streak > 4:
                        total_tickets += 1
                        messagebox.showinfo("Earned Tickets", f"You earned 1 ticket. Total Tickets: {total_tickets}")
                        if total_tickets > 1:
                            total_tickets += 1
                            messagebox.showinfo("Earned Extra Tickets",
                                                f"You earned 2 extra tickets for a streak of 5 or more. Total Tickets: {total_tickets}")
                    continue_learning_plus = messagebox.askquestion("Continue", "Do you want to continue?")
                    if continue_learning_plus.lower() != "yes":
                        try_again = False
            else:
                messagebox.showerror("Error", "Error. The correct result is: " + str(result_plus))
                streak = 0
                update_tickets(False)
                messagebox.showinfo("Reset", "Your series has been reset to 0.")

        elif random_arithmetic_operation == "-":
            random_number_minus = random.randint(500, 1000)
            random_number2_minus = random.randint(1, 1000)
            result_minus = random_number_minus - random_number2_minus
            input_minus = simpledialog.askinteger("Maths Game",
                                                  "Give the result! " + str(random_number_minus) + " - " + str(
                                                      random_number2_minus) + ": ")
            if input_minus == result_minus:
                end_time = datetime.datetime.now()
                elapsed_time = end_time - start_time

                if elapsed_time.total_seconds() > time_limit:
                    messagebox.showinfo("Time's up!", "Time's up!")
                    streak = 0
                    update_tickets(False)
                else:
                    messagebox.showinfo("Congratulations", "Congratulations. Your answer is correct.")
                    streak += 1
                    update_tickets(True)
                    messagebox.showinfo("Streak", "You have solved " + str(streak) + " in one go.")
                    if streak > 4:
                        total_tickets += 1
                        messagebox.showinfo("Earned Tickets", f"You earned 1 ticket. Total Tickets: {total_tickets}")
                        if total_tickets > 1:
                            total_tickets += 1
                            messagebox.showinfo("Earned Extra Tickets",
                                                f"You earned 2 extra tickets for a streak of 5 or more. Total Tickets: {total_tickets}")
                    continue_learning_plus = messagebox.askquestion("Continue", "Do you want to continue?")
                    if continue_learning_plus.lower() != "yes":
                        try_again = False
            else:
                messagebox.showerror("Error", "Error. The correct result is: " + str(result_minus))
                streak = 0
                update_tickets(False)
                messagebox.showinfo("Reset", "Your series has been reset to 0.")

        elif random_arithmetic_operation == "*":
            random_number_mal = random.randint(1, 50)
            random_number2_mal = random.randint(1, 50)
            result_mal = random_number_mal * random_number2_mal
            input_mal = simpledialog.askinteger("Maths Game",
                                                "Give the result! " + str(random_number_mal) + " * " + str(
                                                    random_number2_mal) + ": ")
            if input_mal == result_mal:
                end_time = datetime.datetime.now()
                elapsed_time = end_time - start_time

                if elapsed_time.total_seconds() > time_limit:
                    messagebox.showinfo("Time's up!", "Time's up!")
                    streak = 0
                    update_tickets(False)
                else:
                    messagebox.showinfo("Congratulations", "Congratulations. Your answer is correct.")
                    streak += 1
                    update_tickets(True)
                    messagebox.showinfo("Streak", "You have solved " + str(streak) + " in one go.")
                    if streak > 4:
                        total_tickets += 1
                        messagebox.showinfo("Earned Tickets", f"You earned 1 ticket. Total Tickets: {total_tickets}")
                        if total_tickets > 1:
                            total_tickets += 1
                            messagebox.showinfo("Earned Extra Tickets",
                                                f"You earned 2 extra tickets for a streak of 5 or more. Total Tickets: {total_tickets}")

                    continue_learning_plus = messagebox.askquestion("Continue", "Do you want to continue?")
                    if continue_learning_plus.lower() != "yes":
                        try_again = False
            else:
                messagebox.showerror("Error", "Error. The correct result is: " + str(result_mal))
                streak = 0
                update_tickets(False)
                messagebox.showinfo("Reset", "Your series has been reset to 0.")

        elif random_arithmetic_operation == "**":
            random_number_potenz = random.randint(1, 50)
            random_number2_potenz = random.randint(1, 3)
            result_potenz = random_number_potenz ** random_number2_potenz
            input_potenz = simpledialog.askinteger("Maths Game",
                                                   "Give the result! " + str(random_number_potenz) + " ^ " + str(
                                                       random_number2_potenz) + ": ")
            if input_potenz == result_potenz:
                end_time = datetime.datetime.now()
                elapsed_time = end_time - start_time

                if elapsed_time.total_seconds() > time_limit:
                    messagebox.showinfo("Time's up!", "Time's up!")
                    streak = 0
                    update_tickets(False)
                else:
                    messagebox.showinfo("Congratulations", "Congratulations. Your answer is correct.")
                    streak += 1
                    update_tickets(True)
                    messagebox.showinfo("Streak", "You have solved " + str(streak) + " in one go.")
                    if streak > 4:
                        total_tickets += 1
                        messagebox.showinfo("Earned Tickets", f"You earned 1 ticket. Total Tickets: {total_tickets}")
                        if total_tickets > 1:
                            total_tickets += 1
                            messagebox.showinfo("Earned Extra Tickets",
                                                f"You earned 2 extra tickets for a streak of 5 or more. Total Tickets: {total_tickets}")
                        streak = 0
                    continue_learning_plus = messagebox.askquestion("Continue", "Do you want to continue?")
                    if continue_learning_plus.lower() != "yes":
                        try_again = False
            else:
                messagebox.showerror("Error", "Error. The correct result is: " + str(result_potenz))
                streak = 0
                update_tickets(False)
                messagebox.showinfo("Reset", "Your series has been reset to 0.")

        elif random_arithmetic_operation == "/":
            random_number = random.randint(1, 1000)
            random_number2 = random.randint(1, 100)
            result = random_number / random_number2
            input_geteilt = simpledialog.askfloat("Maths Game", "Give the result! " + str(random_number) + " / " + str(
                random_number2) + ": ")
            if input_geteilt == result:
                end_time = datetime.datetime.now()
                elapsed_time = end_time - start_time

                if elapsed_time.total_seconds() > time_limit:
                    messagebox.showinfo("Time's up!", "Time's up!")
                    streak = 0
                    update_tickets(False)
                else:
                    messagebox.showinfo("Congratulations", "Congratulations. Your answer is correct.")
                    streak += 1
                    update_tickets(True)
                    messagebox.showinfo("Streak", "You have solved " + str(streak) + " in one go.")
                    if streak > 4:
                        total_tickets += 1
                        messagebox.showinfo("Earned Tickets", f"You earned 1 ticket. Total Tickets: {total_tickets}")
                        if total_tickets > 1:
                            total_tickets += 1
                            messagebox.showinfo("Earned Extra Tickets",
                                                f"You earned 2 extra tickets for a streak of 5 or more. Total Tickets: {total_tickets}")
                    continue_learning_plus = messagebox.askquestion("Continue", "Do you want to continue?")
                    if continue_learning_plus.lower() != "yes":
                        try_again = False
            else:
                messagebox.showerror("Error", "Error. The correct result is: " + str(result))
                streak = 0
                update_tickets(False)
                messagebox.showinfo("Reset", "Your series has been reset to 0.")

        root.update()
        root.geometry("600x1200")

    save_game_stats(total_tickets)
else:

    window.destroy()


    def load_game_stats():
        global total_tickets
        try:
            with open('game_stats.txt', 'rb') as file:
                encrypted_data = file.read()
                decrypted_data = decrypt(encrypted_data)
                if int(decrypted_data) > 0:
                    return int(decrypted_data)
                else:
                    sys.exit()
        except FileNotFoundError:
            messagebox.showinfo("Error", "No previous game stats found. Restart the game!")
            sys.exit()


    total_tickets = load_game_stats()


    def save_game_stats():
        try:
            with open('game_stats.txt', 'rb') as file:
                encrypted_data = file.read()
                decrypted_data = decrypt(encrypted_data)
                previous_tickets = int(decrypted_data)
        except FileNotFoundError:
            previous_tickets = 0

        new_total_tickets = previous_tickets - 1

        with open('game_stats.txt', 'wb') as file:
            encrypted_data = encrypt(str(new_total_tickets))
            file.write(encrypted_data)

        messagebox.showinfo("Maths Game", f"Total Tickets: {new_total_tickets}. You had {previous_tickets}")


    save_game_stats()

    monitors = get_monitors()
    primary_monitor = monitors[0]
    screen_width, screen_height = primary_monitor.width, primary_monitor.height

    time.sleep(1)

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Jimmy´s Game")

    score = 0
    font = pygame.font.Font(None, 36)
    speed_increase_score = 5
    speed_increase_amount = 1
    play_again_times = 0

    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)

    player = int(0.08 * screen_height)
    player_s = int(0.014 * screen_height)

    dragon_sx = int(0.002 * screen_width)

    obstacle = int(0.1 * screen_height)
    obstacle_s = int(0.005 * screen_height)

    powerup = int(0.06 * screen_height)
    powerup_s = int(0.007 * screen_height)

    laser = int(0.003 * screen_width)
    laser_s = int(0.03 * screen_height)

    fireball_s = int(0.005 * screen_height)

    player_width = player
    player_height = player
    player_x = screen_width // 2 - player_width // 2
    player_y = screen_height - player_height - 10
    player_speed = player_s

    obstacle_width = obstacle
    obstacle_height = obstacle
    obstacle_x1 = random.randint(0, screen_width - obstacle_width)
    obstacle_y1 = -obstacle_height
    obstacle_speed1 = obstacle_s

    obstacle_width2 = obstacle
    obstacle_height2 = obstacle
    obstacle_x2 = random.randint(0, screen_width - obstacle_width2)
    obstacle_y2 = -obstacle_height2
    obstacle_speed2 = obstacle_s

    obstacle_width3 = obstacle
    obstacle_height3 = obstacle
    obstacle_x3 = random.randint(0, screen_width - obstacle_width3)
    obstacle_y3 = -obstacle_height3
    obstacle_speed3 = obstacle_s

    powerup_width = powerup
    powerup_height = powerup
    powerup_x = random.randint(0, screen_width - powerup_width)
    powerup_y = -powerup_height
    powerup_speed = powerup_s

    laser_width = laser
    laser_height = screen_height
    laser_x = 0
    laser_y = 0
    laser_speed = laser_s
    laser_fired = False
    laser_cooldown_max = 100
    laser_cooldown = laser_cooldown_max

    powerup_effect_duration = 5000
    powerup_active = False
    original_player_size = (player_width, player_height)
    original_player_speed = player_speed
    powerup_end_time = 0

    max_laser_energy = 750
    current_laser_energy = max_laser_energy
    energy_regeneration_rate = 1
    last_shot_time = 0
    anticheat = 0

    dragon_x = 0
    dragon_y = 0
    right_dragon = True
    dragon_speed_x = dragon_sx
    dragon_image = pygame.image.load("dragon.png")
    dragon_imageb = pygame.image.load("dragon2.png")
    dragon = False
    dragon_width = 822
    dragon_heigth = 625
    dragon_damaged = 0
    dragon_forever = True

    fireball_times = 0
    fireball_speed = fireball_s
    fireball_y = 500
    fireball_image = pygame.image.load("fireball.png")
    fireball_image2 = pygame.image.load("fireball2.png")


    class Dialog(QWidget):
        def __init__(self, text, title, choices):
            super().__init__()
            self.setWindowTitle(title)
            layout = QVBoxLayout()
            label = QLabel(text)
            layout.addWidget(label)
            layout.addWidget(QPushButton(choices[0], clicked=self.accept))
            layout.addWidget(QPushButton(choices[1], clicked=self.reject))
            self.setLayout(layout)
            self.setGeometry(0, 0, 300, 150)

        def accept(self):
            self.close()
            self.result = "Accept"

        def reject(self):
            self.close()
            self.result = "Disagree"


    def show_custom_dialog(text, title, choices):
        app = QApplication(sys.argv)
        dialog = Dialog(text, title, choices)
        dialog.move(QApplication.desktop().screen().rect().center() - dialog.rect().center())
        dialog.show()
        app.exec_()
        return dialog.result


    class Dialog(QWidget):
        def __init__(self, text, title, choices):
            super().__init__()
            self.setWindowTitle(title)
            layout = QVBoxLayout()
            label = QLabel(text)
            layout.addWidget(label)
            layout.addWidget(QPushButton(choices[0], clicked=self.accept))
            layout.addWidget(QPushButton(choices[1], clicked=self.reject))
            self.setLayout(layout)
            self.setGeometry(0, 0, 300, 150)

        def accept(self):
            self.close()
            self.result = "Accept"

        def reject(self):
            self.close()
            self.result = "Disagree"


    def show_custom_dialog(text, title, choices):
        app = QApplication(sys.argv)
        dialog = Dialog(text, title, choices)
        dialog.move(QApplication.desktop().screen().rect().center() - dialog.rect().center())
        dialog.show()
        app.exec_()
        return dialog.result


    confirmation = show_custom_dialog(
        """The file 'highscores.txt' will be generated. Please do not delete them. We
    guarantee that the two files are not viruses. The highscore won´t be updated right away.""",
        "Warning", ["Accept", "Disagree"])

    if confirmation == "Disagree":
        app = QApplication(sys.argv)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText("You disagreed to proceed. Exiting the program.")
        msg_box.setWindowTitle("Warning")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()
        pygame.quit()
        sys.exit()

    confirmation2 = show_custom_dialog(
        """This is a game from Jimmy Luong. You must accept the Terms of Use: 21.04.2024
        1. You aren´t allowed to open the program with other programs.
        2. The executable file must not be converted to other files.
        3. You aren´t allowed to modify the file.
        4. We have no warranty on your device.
        5. The and highscore.txt files must not be edited.
    For tips please contact:
    nguyenhungjimmy.luong@yahoo.com

    verion = newest(1.2)

    Happy playing from Jimmy.
        """, "Terms of Use", ["Accept", "Disagree"])

    if confirmation2 == "Disagree":
        app = QApplication(sys.argv)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText("You disagreed to proceed. Exiting the program.")
        msg_box.setWindowTitle("Warning")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()
        pygame.quit()
        sys.exit()

    KEY = b'MeAqQAJJjMI5xqtcf4jkPFalNw2mzp5yflwNyPl1w5s='

    cipher_suite = Fernet(KEY)


    def encrypt_data(data):
        return cipher_suite.encrypt(data.encode())


    def decrypt_data(encrypted_data):
        return cipher_suite.decrypt(encrypted_data).decode()


    def show_score(score):
        score_text = font.render("Score: " + str(score), True, white)
        screen.blit(score_text, (10, 10))


    def game_over(score):
        class GameOverDialog(QDialog):
            def __init__(self, score):
                super().__init__()
                self.score = score
                self.setWindowTitle("Game Over")
                layout = QVBoxLayout()
                layout.addWidget(QLabel("Game Over! Enter your name:"))
                self.name_input = QLineEdit()
                layout.addWidget(self.name_input)
                layout.addWidget(QPushButton("Submit", clicked=self.submit))
                self.setLayout(layout)

            def closeEvent(self, event):
                event.ignore()

            def submit(self):
                global anticheat
                global play_again_times
                name = self.name_input.text()
                if name:
                    improved_message = check_improvement(name, self.score)
                    msg_box = QMessageBox()
                    msg_box.setText(improved_message)
                    msg_box.setWindowTitle("Game Over")
                    msg_box.exec_()
                    self.close()
                    highscores_message = "Highscores:\n" + "\n".join(load_highscores())
                    score_message = f"Your score is: {self.score}"
                    update_highscores(name, self.score)
                    play_again = QMessageBox.question(self, "Game Over",
                                                      score_message + "\n\n" + highscores_message + "\n\nPlay Again? (Doesn't cost anything.) You have 3 play agains.",
                                                      QMessageBox.Yes | QMessageBox.No)
                    if play_again == QMessageBox.Yes:
                        reset_game()
                        play_again_times += 1
                        if play_again_times == 2:
                            play_again_2 = QMessageBox.question(self, "Game Over",
                                                              "You played too long. For playing another time, please reset the game!",
                                                              QMessageBox.OK)

                            try:
                                if play_again_2 == QMessageBox.Yes:
                                    pygame.quit()
                                    quit()
                            except Exception as e:
                                print("error:" + e)
                                pygame.quit()
                                quit()


                            else:
                                self.close()
                                pygame.quit()
                                quit()

                    else:
                        pygame.quit()
                        quit()
                    self.accept()
                    self.close()
                else:
                    QMessageBox.warning(self, "Game Over", "Please enter your name!")
                    self.close()
                    anticheat += 1
                    if int(anticheat) == 3:
                        pygame.quit()
                        quit()

        app = QApplication(sys.argv)
        dialog = GameOverDialog(score)
        dialog.exec_()
        app.quit()


    def check_improvement(name, current_score):
        highscores = load_highscores()
        for entry in highscores:
            if entry.startswith(f"{name}:"):
                previous_score = int(entry.split(": ")[1])
                if current_score > previous_score:
                    update_highscores(name, current_score)
                    return f"Congratulations, {name}! You have improved your score from {previous_score} to {current_score}."
                else:
                    return f"Unfortunately, {name}, you have not improved your previous score of {previous_score}."
        return f"Congratulations, {name}! You have achieved a new high score of {current_score}."


    def load_highscores():
        try:
            with open("highscores.txt", "rb") as file:
                encrypted_data = file.read()
                decrypted_data = decrypt_data(encrypted_data)
                highscores = decrypted_data.splitlines()
            return highscores
        except FileNotFoundError:
            return []


    def save_highscores(highscores):
        encrypted_data = encrypt_data("\n".join(highscores))
        with open("highscores.txt", "wb") as file:
            file.write(encrypted_data)


    def update_highscores(name, score):
        highscores = load_highscores()
        new_entry = f"{name}: {score}"
        found = False

        for i, entry in enumerate(highscores):
            if entry.startswith(f"{name}:"):
                found = True
                previous_score = int(entry.split(": ")[1])
                if score > previous_score:
                    highscores[i] = new_entry
                    break

        if not found:
            highscores.append(new_entry)

        highscores.sort(reverse=True, key=lambda x: int(x.split(": ")[1]))
        if len(highscores) > 10:
            highscores = highscores[:10]
        save_highscores(highscores)


    def check_collision(rect1, rect2):
        return rect1.colliderect(rect2)


    def roll_dice():
        return random.randint(1, 6)


    def activate_powerup():
        global player_width, player_height, player_speed, powerup_active, powerup_end_time

        original_player_size = (player_width, player_height)
        original_player_speed = player_speed

        player_width //= 1.02
        player_height //= 1.02

        player_speed *= 1.05

        powerup_active = True
        powerup_end_time = pygame.time.get_ticks() + powerup_effect_duration


    def check_powerup_status():
        global player_width, player_height, player_speed, powerup_active

        if powerup_active and pygame.time.get_ticks() > powerup_end_time:
            player_width, player_height = original_player_size
            player_speed = original_player_speed
            powerup_active = False


    def reset_game():
        global anticheat, dragon, score, obstacle_y1, obstacle_y2, obstacle_y3, powerup_y, player_x, player_y, obstacle_speed1, obstacle_speed2, obstacle_speed3, powerup_x, player_speed, current_laser_energy
        score = 0
        anticheat = 0
        obstacle_y1 = -obstacle_height
        obstacle_y2 = -obstacle_height2
        obstacle_y3 = -obstacle_height3
        powerup_y = -powerup_height
        player_x = screen_width // 2 - player_width // 2
        player_y = screen_height - player_height - 10
        obstacle_speed1 = 4
        obstacle_speed2 = 4
        obstacle_speed3 = 4
        powerup_x = random.randint(0, screen_width - powerup_width)
        player_speed = original_player_speed
        current_laser_energy = max_laser_energy
        dragon = False


    def initialize_highscores():
        players = [("Thomas", 200), ("Max", 400), ("Mary", 600), ("Nicolas", 800), ("Greta", 1600)]
        for player, initial_score in players:
            update_highscores(player, initial_score)


    initialize_highscores()

    energy_regeneration_rate = 0.0005


    def update_laser_energy():

        global current_laser_energy
        if current_laser_energy > 0:
            energy_to_fill = max_laser_energy * energy_regeneration_rate
            current_laser_energy = min(max_laser_energy, current_laser_energy + energy_to_fill)
        else:
            pass


    energy_bar_color = green
    running = True
    clock = pygame.time.Clock()




    while running:

        game_over_flag = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x += player_speed

        if player_x < 10:
            player_x = 10
        elif player_x + player_width > screen_width - 10:
            player_x = screen_width - player_width - 10

        laser_energy_consumption = 1

        if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[
            pygame.K_w] and pygame.time.get_ticks() - last_shot_time >= laser_cooldown_max:
            if current_laser_energy >= laser_energy_consumption:
                laser_x = player_x + player_width / 2 - laser_width / 2
                laser_y = player_y
                last_shot_time = pygame.time.get_ticks()
                current_laser_energy -= laser_energy_consumption
                laser_fired = True

        if laser_fired:
            if laser_y > 0:
                laser_y -= laser_speed
                if obstacle_x1 < laser_x < obstacle_x1 + obstacle_width and obstacle_y1 < laser_y < obstacle_y1 + obstacle_height:
                    obstacle_y1 = screen_height + obstacle_height
                    score += 10
                    current_laser_energy -= 2
                if obstacle_x2 < laser_x < obstacle_x2 + obstacle_width2 and obstacle_y2 < laser_y < obstacle_y2 + obstacle_height2:
                    obstacle_y2 = screen_height + obstacle_height2
                    score += 10
                    current_laser_energy -= 2
                if obstacle_x3 < laser_x < obstacle_x3 + obstacle_width3 and obstacle_y3 < laser_y < obstacle_y3 + obstacle_height3:
                    obstacle_y3 = screen_height + obstacle_height3
                    score += 10
                    current_laser_energy -= 2
                if dragon_x < laser_x < dragon_x + dragon_width and dragon_y < laser_y < dragon_y + dragon_heigth:
                    dragon_damaged += 
                    current_laser_energy -= 1

                if dragon_damaged > 1250:
                    if dragon < 1260:
                        dragon_forever = False
                        score += 50

            else:
                laser_fired = False

        obstacle_y1 += obstacle_speed1
        if obstacle_y1 > screen_height:
            obstacle_x1 = random.randint(0, screen_width - obstacle_width)
            obstacle_y1 = -obstacle_height
            if score % speed_increase_score == 0:
                obstacle_speed1 += speed_increase_amount
            score += 1

        obstacle_y2 += obstacle_speed2
        if obstacle_y2 > screen_height:
            obstacle_x2 = random.randint(0, screen_width - obstacle_width2)
            obstacle_y2 = -obstacle_height2
            if score % speed_increase_score == 0:
                obstacle_speed2 += speed_increase_amount
            score += 1

        obstacle_y3 += obstacle_speed3
        if obstacle_y3 > screen_height:
            obstacle_x3 = random.randint(0, screen_width - obstacle_width3)
            obstacle_y3 = -obstacle_height3
            if score % speed_increase_score == 0:
                obstacle_speed3 += speed_increase_amount
            score += 1

        powerup_y += powerup_speed
        if powerup_y > screen_height and random.random() < 0.1:
            powerup_x = random.randint(0, screen_width - powerup_width)
            powerup_y = -powerup_height

        if (
                player_x < obstacle_x1 + obstacle_width and player_x + player_width > obstacle_x1 and player_y < obstacle_y1 + obstacle_height and player_y + player_height > obstacle_y1) or (
                player_x < obstacle_x2 + obstacle_width2 and player_x + player_width > obstacle_x2 and player_y < obstacle_y2 + obstacle_height2 and player_y + player_height > obstacle_y2) or (
                player_x < obstacle_x3 + obstacle_width3 and player_x + player_width > obstacle_x3 and player_y < obstacle_y3 + obstacle_height3 and player_y + player_height > obstacle_y3):
            game_over_flag = True

        if player_x < powerup_x + powerup_width and player_x + player_width > powerup_x and player_y < powerup_y + powerup_height and player_y + player_height > powerup_y:
            score += 5
            powerup_x = random.randint(0, screen_width - powerup_width)
            powerup_y = -powerup_height
            activate_powerup()

        check_powerup_status()

        screen.fill(black)

        if dragon_forever:
            if score > 9:
                dragon = True
        else:
            dragon = False

        if dragon:
            if right_dragon:
                dragon_x += dragon_speed_x
            else:
                dragon_x -= dragon_speed_x

            if dragon_x > (screen_width + 3000):
                right_dragon = False
                dragon_x = screen_width + 3000
            elif dragon_x < - 3000:
                right_dragon = True
                dragon_x = -3000

            if right_dragon:
                screen.blit(dragon_image, (dragon_x, dragon_y))
                fireball_x = dragon_x + 800
            else:
                screen.blit(dragon_imageb, (dragon_x, dragon_y))
                fireball_x = dragon_x - 30
            fireball_times += 1
            if fireball_times == 1:
                if right_dragon:
                    fireball_y += fireball_speed
                    screen.blit(fireball_image, (fireball_x, fireball_y))
                    fireball_times = 0
                else:
                    fireball_y += fireball_speed
                    screen.blit(fireball_image2, (fireball_x, fireball_y))
                fireball_times = 0

            if fireball_y > screen_height + 10:
                fireball_y = 500

            fireball_heigth = 125
            fireball_width = 155


            if (fireball_x <= player_x + player_width and
                    fireball_x + fireball_width >= player_x and
                    fireball_y + fireball_heigth >= player_y and
                    fireball_y <= player_y + player_height):
                game_over(score)
                game_over_flag = True



        pygame.draw.rect(screen, green, (player_x, player_y, player_width, player_height))
        pygame.draw.rect(screen, blue, (obstacle_x1, obstacle_y1, obstacle_width, obstacle_height))
        pygame.draw.rect(screen, blue, (obstacle_x2, obstacle_y2, obstacle_width2, obstacle_height2))
        pygame.draw.rect(screen, blue, (obstacle_x3, obstacle_y3, obstacle_width3, obstacle_height3))
        pygame.draw.rect(screen, red, (powerup_x, powerup_y, powerup_width, powerup_height))

        if current_laser_energy >= 700:
            energy_bar_color = green
        elif current_laser_energy <= 150:
            energy_bar_color = red
        else:
            energy_bar_color = yellow

        pygame.draw.rect(screen, energy_bar_color,
                         (screen_width - 20, screen_height - current_laser_energy, 20, current_laser_energy))

        if laser_fired:
            pygame.draw.rect(screen, red, (laser_x, laser_y, laser_width, laser_height))

        pygame.draw.rect(screen, energy_bar_color,
                         (screen_width - 20, screen_height - current_laser_energy, 20, current_laser_energy))

        speed_text = font.render("Player Speed: " + str(player_speed), True, white)
        screen.blit(speed_text, (10, 40))

        dragon_live_calculation = dragon_damaged

        obstacle_speed1_text = font.render("Obstacle Speed 1: " + str(obstacle_speed1), True, white)
        obstacle_speed2_text = font.render("Obstacle Speed 2: " + str(obstacle_speed2), True, white)
        obstacle_speed3_text = font.render("Obstacle Speed 3: " + str(obstacle_speed3), True, white)
        dragon_live_show = font.render("You damaged the dragon: " + str(dragon_live_calculation) + " from 1250", True, white)

        screen.blit(obstacle_speed1_text, (10, 70))
        screen.blit(obstacle_speed2_text, (10, 100))
        screen.blit(obstacle_speed3_text, (10, 130))

        if dragon_forever:
            screen.blit(dragon_live_show, (10, 160))

        update_laser_energy()

        show_score(score)
        pygame.display.update()

        if game_over_flag:
            game_over(score)
            game_over_flag = False

        clock.tick(90)

    pygame.quit()
    quit()

