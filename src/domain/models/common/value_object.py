from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any

# 保持する値の型を表すジェネリクス（TypeScriptの T に相当）
T = TypeVar("T")


class ValueObject(ABC, Generic[T]):
    """
    値オブジェクトの基底クラス。
    不変性とバリデーションをサポートします。
    """

    _value: T

    def __init__(self, value: T) -> None:
        # 1. 構築時にビジネスルールに基づくバリデーションを実行
        self.validate(value)
        # 2. 外部から直接変更されないよう、慣習的にアンダースコアを付与
        # frozen=True なデータクラスに対応するため、object.__setattr__ を使用します
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

    def equals(self, other: Any) -> bool:
        """
        他のオブジェクトと同値か比較します。
        """
        if not isinstance(other, ValueObject):
            return False

        # クラス（型）が一致しているかチェック（名目的型付けの再現）
        # これにより UserId と ChannelId を間違えて比較しても False になります
        if type(self) is not type(other):
            return False

        # 値の比較（Pythonの == は辞書やリストも深く比較します）
        return bool(self._value == other._value)

    def __eq__(self, other: Any) -> bool:
        """
        Pythonの == 演算子で equals メソッドを呼び出せるようにします。
        """
        return self.equals(other)

    def __hash__(self) -> int:
        """
        __eq__ と整合性のあるハッシュ値を返します。
        set や dict のキーとして使用できるようにします。
        """
        return hash(self._value)

    def __repr__(self) -> str:
        """デバッグ時に内容を見やすくするための特殊メソッドです。"""
        return f"{self.__class__.__name__}({self._value})"
