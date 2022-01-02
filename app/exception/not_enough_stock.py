class NotEnoughStockError(Exception):
    def __str__(self) -> str:
        return "제고는 음수가 될 수 없음"