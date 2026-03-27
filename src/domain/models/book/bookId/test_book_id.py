import pytest
from domain.models.book.bookId.book_id import BookId


class TestBookId:
    def test_can_create_with_isbn10(self) -> None:
        """10文字のISBN-10でBookIdが作成できる"""
        # Arrange
        isbn = "1234567890"

        # Act
        book_id = BookId(isbn)

        # Assert
        assert book_id.value == isbn

    def test_can_create_with_isbn13(self) -> None:
        """13文字のISBN-13でBookIdが作成できる"""
        # Arrange
        isbn = "9781234567890"

        # Act
        book_id = BookId(isbn)

        # Assert
        assert book_id.value == isbn

    def test_error_when_less_than_min_length(self) -> None:
        """最小長未満の値でBookIdを生成するとエラーを投げる"""
        # Arrange
        isbn = "123456789"

        # Act & Assert
        with pytest.raises(
            ValueError, match="ISBNの文字数が10以上である必要があります。"
        ):
            BookId(isbn)

    def test_error_when_exceeds_max_length(self) -> None:
        """最大長を超える値でBookIdを生成するとエラーを投げる"""
        # Arrange
        isbn = "12345678901234"

        # Act & Assert
        with pytest.raises(
            ValueError, match="ISBNの文字数が13以下である必要があります。"
        ):
            BookId(isbn)

    def test_equality_with_same_value(self) -> None:
        """同じ値のBookIdは等しい"""
        # Arrange
        isbn = "1234567890"

        # Act
        book_id1 = BookId(isbn)
        book_id2 = BookId(isbn)

        # Assert
        assert book_id1 == book_id2

    def test_inequality_with_different_value(self) -> None:
        """異なる値のBookIdは等しくない"""
        # Arrange
        isbn1 = "1234567890"
        isbn2 = "9781234567890"

        # Act
        book_id1 = BookId(isbn1)
        book_id2 = BookId(isbn2)

        # Assert
        assert book_id1 != book_id2
