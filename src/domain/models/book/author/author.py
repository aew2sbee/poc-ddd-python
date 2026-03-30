from domain.models.common.value_object import ValueObject


class Author(ValueObject[str]):
    _MIN_LENGTH = 1
    _INVALID_MIN_LENGTH = f"著者名の文字数が{_MIN_LENGTH}以上である必要があります。"
    _MAX_LENGTH = 100
    _INVALID_MAX_LENGTH = f"著者名の文字数が{_MAX_LENGTH}以下である必要があります。"

    def __init__(self, value: str):
        super().__init__(value)

    def validate(self, value: str) -> None:
        if len(value) < self._MIN_LENGTH:
            raise ValueError(self._INVALID_MIN_LENGTH)
        if len(value) > self._MAX_LENGTH:
            raise ValueError(self._INVALID_MAX_LENGTH)
