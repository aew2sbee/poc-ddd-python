from dataclasses import dataclass
from typing import Any
from domain.models.book.bookId.book_id import BookId
from domain.models.book.title.title import Title
from domain.models.book.author.author import Author


@dataclass(frozen=True, eq=False)
class BookIdentity:
    """
    書籍の同一性を管理する値オブジェクト
    """

    _book_id: BookId
    _title: Title
    _author: Author

    def equals(self, other: "BookIdentity") -> bool:
        """
        書籍のIDのみで同一性を判定します
        """
        if not isinstance(other, BookIdentity):
            return False
        return self._book_id == other._book_id

    def __eq__(self, other: Any) -> bool:
        return self.equals(other)

    def __hash__(self) -> int:
        return hash(self._book_id)

    @property
    def book_id(self) -> BookId:
        return self._book_id

    @property
    def title(self) -> Title:
        return self._title

    @property
    def author(self) -> Author:
        return self._author
