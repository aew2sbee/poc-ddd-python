from dataclasses import dataclass
from domain.models.common.value_object import ValueObject


@dataclass(frozen=True, init=False)
class Price(ValueObject[int]):
    """
    価格を扱う値オブジェクト
    """

    _value: int

    # --- クラス内のみで使用する定数 ---
    _CURRENCY = "JPY"
    _MAX_AMOUNT = 1000000
    _MIN_AMOUNT = 1
    _INVALID_MIN_AMOUNT = f"価格は{_MIN_AMOUNT}円以上である必要があります。"
    _INVALID_MAX_AMOUNT = f"価格は{_MAX_AMOUNT}円以下である必要があります。"

    def __init__(self, amount: int):
        super().__init__(amount)

    def validate(self, value: int) -> None:
        if value < self._MIN_AMOUNT:
            raise ValueError(self._INVALID_MIN_AMOUNT)
        if value > self._MAX_AMOUNT:
            raise ValueError(self._INVALID_MAX_AMOUNT)

    @property
    def amount(self) -> int:
        return self._value

    @property
    def currency(self) -> str:
        return self._CURRENCY
