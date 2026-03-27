from domain.models.book.bookId.book_id import BookId
from domain.models.book.title.title import Title
from domain.models.book.author.author import Author
from domain.models.book.book_identity.book_identity import BookIdentity
from domain.models.book.price.price import Price
from domain.models.book.book import Book


class TestBook:
    def _create_identity(
        self,
        isbn: str = "9781234567890",
        title: str = "テスト書籍",
        author: str = "テスト著者",
    ) -> BookIdentity:
        return BookIdentity(BookId(isbn), Title(title), Author(author))

    def test_can_create_book(self) -> None:
        """Book.createで書籍を作成できる"""
        # Arrange
        identity = self._create_identity()
        price = Price(amount=1500)

        # Act
        book = Book.create(identity, price)

        # Assert
        assert book.book_id == BookId("9781234567890")
        assert book.title == Title("テスト書籍")
        assert book.author == Author("テスト著者")
        assert book.price == price

    def test_can_reconstruct_book(self) -> None:
        """Book.reconstructで書籍を再構築できる"""
        # Arrange
        identity = self._create_identity()
        price = Price(amount=2000)

        # Act
        book = Book.reconstruct(identity, price)

        # Assert
        assert book.book_id == BookId("9781234567890")
        assert book.price == price

    def test_equals_with_same_book_id(self) -> None:
        """同じBookIdを持つ書籍はequalsでTrueを返す"""
        # Arrange
        identity = self._create_identity()
        book1 = Book.create(identity, Price(amount=1500))
        book2 = Book.create(identity, Price(amount=2000))

        # Act
        result = book1.equals(book2)

        # Assert
        assert result is True

    def test_not_equals_with_different_book_id(self) -> None:
        """異なるBookIdを持つ書籍はequalsでFalseを返す"""
        # Arrange
        book1 = Book.create(
            self._create_identity(isbn="9781234567890"), Price(amount=1500)
        )
        book2 = Book.create(
            self._create_identity(isbn="9789876543210"), Price(amount=1500)
        )

        # Act
        result = book1.equals(book2)

        # Assert
        assert result is False

    def test_change_price(self) -> None:
        """change_priceで価格を変更できる"""
        # Arrange
        book = Book.create(self._create_identity(), Price(amount=1500))
        new_price = Price(amount=2000)

        # Act
        book.change_price(new_price)

        # Assert
        assert book.price == new_price
