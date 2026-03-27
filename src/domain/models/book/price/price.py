from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class Price:
    """
    価格を扱う値オブジェクト
    """

    amount: int
    currency: Literal["JPY"] = "JPY"

    # 定数の定義
    _MAX_AMOUNT = 1000000
    _MIN_AMOUNT = 1
    _INVALID_MIN_AMOUNT = f"価格は{_MIN_AMOUNT}円以上である必要があります。"
    _INVALID_MAX_AMOUNT = f"価格は{_MAX_AMOUNT}円以下である必要があります。"
    _INVALID_CURRENCY = "現在は日本円のみを扱います。"

    def __post_init__(self) -> None:
        """
        インスタンス生成時にバリデーションを実行します
        """
        self._validate()

    def _validate(self) -> None:
        if self.currency != "JPY":
            raise ValueError(self._INVALID_CURRENCY)

        if not (self._MIN_AMOUNT <= self.amount <= self._MAX_AMOUNT):
            if self.amount < self._MIN_AMOUNT:
                raise ValueError(self._INVALID_MIN_AMOUNT)
            if self.amount > self._MAX_AMOUNT:
                raise ValueError(self._INVALID_MAX_AMOUNT)

    @property
    def value_amount(self) -> int:
        return self.amount

    @property
    def value_currency(self) -> str:
        return self.currency
