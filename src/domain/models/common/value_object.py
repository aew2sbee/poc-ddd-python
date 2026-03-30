from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any

# 保持する値の型を表すジェネリクス（TypeScriptの T に相当）
T = TypeVar("T")


class ValueObject(ABC, Generic[T]):
    """
    値オブジェクトの基底クラス。
    不変性とバリデーションをサポートします。

    不変性は本クラスの __setattr__ / __delattr__ で保証しているため、
    サブクラスで @dataclass(frozen=True) を付ける必要はありません。
    """

    _value: T

    def __init__(self, value: T) -> None:
        # 1. 構築時にビジネスルールに基づくバリデーションを実行
        self.validate(value)
        # 2. object.__setattr__ を直接呼び、下記の __setattr__ をバイパスしてセット
        object.__setattr__(self, "_value", value)

    @abstractmethod
    def validate(self, value: T) -> None:
        """
        継承先で必ず実装するバリデーションロジック。
        不正な値の場合は ValueError などを発生させます。
        """
        pass

    @property
    def value(self) -> T:
        """
        保持している値を返します（TypeScriptの get value() に相当）。
        """
        return self._value

    def __eq__(self, other: Any) -> bool:
        """
        他のオブジェクトと同値か比較します。
        Python では == 演算子がこのメソッドを自動的に呼び出します。
        """
        if not isinstance(other, ValueObject):
            return False

        # クラス（型）が一致しているかチェック（名目的型付けの再現）
        # これにより BookId と Title を間違えて比較しても False になります
        if type(self) is not type(other):
            return False

        # 値の比較（Pythonの == は辞書やリストも深く比較します）
        return bool(self._value == other._value)

    def __hash__(self) -> int:
        """
        __eq__ と整合性のあるハッシュ値を返します。
        set や dict のキーとして使用できるようにします。
        """
        return hash(self._value)

    def __repr__(self) -> str:
        """デバッグ時に内容を見やすくするための特殊メソッドです。"""
        return f"{self.__class__.__name__}({self._value})"

    def __setattr__(self, name: str, value: Any) -> None:
        """構築後の属性変更を禁止し、不変性を保証します。"""
        raise AttributeError(
            f"{self.__class__.__name__} は不変オブジェクトです。属性を変更できません。"
        )

    def __delattr__(self, name: str) -> None:
        """属性の削除を禁止し、不変性を保証します。"""
        raise AttributeError(
            f"{self.__class__.__name__} は不変オブジェクトです。属性を削除できません。"
        )
