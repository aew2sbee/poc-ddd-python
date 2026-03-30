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
        """ISBNが最小長未満の値でBookIdを生成するとエラーを投げる"""
        # Arrange
        isbn = "123456789"

        # Act & Assert
        with pytest.raises(ValueError, match=BookId._INVALID_LENGTH):
            BookId(isbn)

    def test_error_when_invalid_length_11(self) -> None:
        """ISBNが11文字の無効な長さの値でBookIdを生成するとエラーを投げる"""
        # Arrange
        isbn = "12345678901"

        # Act & Assert
        with pytest.raises(ValueError, match=BookId._INVALID_LENGTH):
            BookId(isbn)

    def test_error_when_invalid_length_12(self) -> None:
        """ISBNが12文字の無効な長さの値でBookIdを生成するとエラーを投げる"""
        # Arrange
        isbn = "123456789012"

        # Act & Assert
        with pytest.raises(ValueError, match=BookId._INVALID_LENGTH):
            BookId(isbn)

    def test_error_when_exceeds_max_length(self) -> None:
        """ISBNが最大長を超える値でBookIdを生成するとエラーを投げる"""
        # Arrange
        isbn = "12345678901234"

        # Act & Assert
        with pytest.raises(ValueError, match=BookId._INVALID_LENGTH):
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

    def test_to_isbn_with_isbn10(self) -> None:
        """ISBN-10をISBNフォーマットに変換できる"""
        # Arrange
        book_id = BookId("1234567890")

        # Act
        result = book_id.to_isbn()

        # Assert
        assert result == "ISBN1-23-456789-0"

    def test_to_isbn_with_isbn13(self) -> None:
        """ISBN-13をISBNフォーマットに変換できる"""
        # Arrange
        book_id = BookId("9781234567890")

        # Act
        result = book_id.to_isbn()

        # Assert
        assert result == "ISBN978-1-23-456789-0"
