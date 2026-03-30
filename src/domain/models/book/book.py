from __future__ import annotations
from domain.models.book.bookId.book_id import BookId
from domain.models.book.book_identity.book_identity import BookIdentity
from domain.models.book.price.price import Price
from domain.models.book.title.title import Title
from domain.models.book.author.author import Author


class Book:
    """
    書籍エンティティ
    """

    def __init__(self, identity: BookIdentity, price: Price):
        # 内部変数として保持
        self._identity = identity
        self._price = price

    @staticmethod
    def create(identity: BookIdentity, price: Price) -> Book:
        """新規作成用ファクトリメソッド"""
        return Book(identity, price)

    @staticmethod
    def reconstruct(identity: BookIdentity, price: Price) -> Book:
        """再構築用（DBからの復元など）ファクトリメソッド"""
        return Book(identity, price)

    def equals(self, other: Book) -> bool:
        """
        別の書籍と同一かどうかを判定（BookIdentityのequalsに委譲）
        """
        if not isinstance(other, Book):
            return False
        return self._identity.equals(other._identity)

    # --- Getter ---
    @property
    def book_id(self) -> BookId:
        return self._identity.book_id

    @property
    def title(self) -> Title:
        return self._identity.title

    @property
    def author(self) -> Author:
        return self._identity.author

    @property
    def price(self) -> Price:
        return self._price

    # --- Behavior ---
    def change_price(self, new_price: Price) -> "Book":
        """価格を変更します"""
        return Book(self._identity, new_price)
