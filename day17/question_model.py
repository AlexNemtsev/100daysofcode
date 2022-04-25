class Question:
    def __init__(self, text, answer) -> None:
        self.text = text
        self.answer = answer

    def __repr__(self) -> str:
        return f"Question({self.text}, {self.answer})"
