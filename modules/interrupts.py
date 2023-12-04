class Interrupts:
    @staticmethod
    def exit(user_input):
        if user_input.lower() == "exit":
            return True
