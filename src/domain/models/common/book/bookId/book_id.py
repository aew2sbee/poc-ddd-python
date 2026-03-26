from dataclasses import dataclass
from domain.models.common.value_object import ValueObject

@dataclass(frozen=True)
class BookId(ValueObject[str]):
    # --- クラス内のみで使用する定数 ---
    _MIN_LENGTH = 10
    _INVALID_MIN_LENGTH = f"ISBNの文字数が{_MIN_LENGTH}以上である必要があります。"
    _MAX_LENGTH = 13
    _INVALID_MAX_LENGTH = f"ISBNの文字数が{_MAX_LENGTH}以下である必要があります。"
    _ISBN13_PREFIXES = ("978", "979")
    def __init__(self, id: str):
        super().__init__(id)

    def validate(self, value: str) -> None:
        if len(value) < self._MIN_LENGTH:
            raise ValueError(self._INVALID_MIN_LENGTH)
        if len(value) > self._MAX_LENGTH:
            raise ValueError(self._INVALID_MAX_LENGTH)

    @staticmethod
    def _is_valid_isbn10(isbn10: str) -> bool:
        """
        ISBN-10 のバリデーション（内部用）。
        先頭の _ は、外部から呼び出さない「プライベート」な意図を表します。
        """
        # 実際にはここにチェックディジットの計算ロジックなどを実装します
        return len(isbn10) == BookId._MIN_LENGTH

    @staticmethod
    def _is_valid_isbn13(isbn13: str) -> bool:
        """
        ISBN-13 のバリデーション（内部用）。
        """
        # 実際にはより詳細なチェックロジックを実装します
        return isbn13.startswith(BookId._ISBN13_PREFIXES) and len(isbn13) == BookId._MAX_LENGTH
