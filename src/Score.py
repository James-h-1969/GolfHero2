class Score():
    def __init__(self):
        self.score = 0

    def add_to_score(self, i:int) -> None:
        self.score += i
    
    def take_from_score(self, i:int) -> None:
        self.score -= i

    def get_score(self) -> int:
        return self.score