from domain.models.common.value_object import ValueObject


class BookId(ValueObject[str]):
    # --- クラス内のみで使用する定数 ---
    _MIN_LENGTH = 10
    _MAX_LENGTH = 13
    _INVALID_LENGTH = (
        f"ISBNの文字数が{_MIN_LENGTH}か{_MAX_LENGTH}である必要があります。"
    )
    _ISBN13_PREFIXES = ("978", "979")

    def __init__(self, isbn: str):
        super().__init__(isbn)

    def validate(self, value: str) -> None:
        if not (len(value) == self._MIN_LENGTH or len(value) == self._MAX_LENGTH):
            raise ValueError(self._INVALID_LENGTH)

    def to_isbn(self) -> str:
        """ISBNフォーマットの文字列に変換します。"""
        # ISBNが10桁の場合の、'ISBN' フォーマットに変換します。
        if self._is_valid_isbn10(self._value):
            group_identifier = self._value[0:1]  # 国コードなど（1桁）
            publisher_code = self._value[1:3]  # 出版社コード（2桁）
            book_code = self._value[3:9]  # 書籍コード（6桁）
            checksum = self._value[9:]  # チェックディジット（1桁）
            return f"ISBN{group_identifier}-{publisher_code}-{book_code}-{checksum}"
        # ISBNが13桁の場合の、'ISBN' フォーマットに変換します。
        else:
            isbn_prefix = self._value[0:3]  # プレフィックス（3桁）
            group_identifier = self._value[3:4]  # 国コードなど（1桁）
            publisher_code = self._value[4:6]  # 出版社コード（2桁）
            book_code = self._value[6:12]  # 書籍コード（6桁）
            checksum = self._value[12:]  # チェックディジット（1桁）
            return f"ISBN{isbn_prefix}-{group_identifier}-{publisher_code}-{book_code}-{checksum}"

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
        return (
            isbn13.startswith(BookId._ISBN13_PREFIXES)
            and len(isbn13) == BookId._MAX_LENGTH
        )
