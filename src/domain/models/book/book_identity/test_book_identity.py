from domain.models.book.bookId.book_id import BookId
from domain.models.book.title.title import Title
from domain.models.book.author.author import Author
from domain.models.book.book_identity.book_identity import BookIdentity


class TestBookIdentity:
    def test_can_create_book_identity(self) -> None:
        """BookIdentityが正しく作成できる"""
        # Arrange
        book_id = BookId("9781234567890")
        title = Title("テスト書籍")
        author = Author("テスト著者")

        # Act
        identity = BookIdentity(book_id, title, author)

        # Assert
        assert identity.book_id == book_id
        assert identity.title == title
        assert identity.author == author

    def test_equals_with_same_book_id(self) -> None:
        """同じBookIdを持つBookIdentityはequalsでTrueを返す"""
        # Arrange
        book_id = BookId("9781234567890")
        identity1 = BookIdentity(book_id, Title("書籍A"), Author("著者A"))
        identity2 = BookIdentity(book_id, Title("書籍B"), Author("著者B"))

        # Act
        result = identity1.equals(identity2)

        # Assert
        assert result is True

    def test_not_equals_with_different_book_id(self) -> None:
        """異なるBookIdを持つBookIdentityはequalsでFalseを返す"""
        # Arrange
        identity1 = BookIdentity(
            BookId("9781234567890"), Title("書籍A"), Author("著者A")
        )
        identity2 = BookIdentity(
            BookId("9789876543210"), Title("書籍A"), Author("著者A")
        )

        # Act
        result = identity1.equals(identity2)

        # Assert
        assert result is False
