import tkinter as tk
from tkinter import messagebox
import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed is crucial for programmers.",
    "Practice makes a person perfect.",
    "Always code as if the guy who ends up maintaining your code is a violent psychopath."
]

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x400")
        self.root.resizable(False, False)

        self.text_to_type = random.choice(sentences)
        self.start_time = None

        self.sentence_label = tk.Label(root, text=self.text_to_type, font=("Arial", 16), wraplength=600)
        self.sentence_label.pack(pady=20)

        self.input_text = tk.Text(root, height=5, font=("Arial", 14), wrap="word")
        self.input_text.pack(pady=10)
        self.input_text.bind("<KeyPress>", self.start_timer)

        self.done_button = tk.Button(root, text="Done", command=self.calculate_speed)
        self.done_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def start_timer(self, event):
        if not self.start_time:
            self.start_time = time.time()

    def calculate_speed(self):
        end_time = time.time()
        if not self.start_time:
            messagebox.showinfo("Typing Test", "Please start typing first!")
            return

        elapsed_time = end_time - self.start_time
        typed_text = self.input_text.get("1.0", "end-1c").strip()

        total_words = len(typed_text.split())
        wpm = round((total_words / elapsed_time) * 60)

        accuracy = self.calculate_accuracy(typed_text, self.text_to_type)

        self.result_label.config(text=f"Typing Speed: {wpm} WPM | Accuracy: {accuracy}%")

    def calculate_accuracy(self, typed, actual):
        typed_words = typed.split()
        actual_words = actual.split()
        correct = 0
        for t, a in zip(typed_words, actual_words):
            if t == a:
                correct += 1
        accuracy = (correct / len(actual_words)) * 100
        return round(accuracy)


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()