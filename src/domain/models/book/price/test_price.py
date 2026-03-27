import pytest
from domain.models.book.price.price import Price


class TestPrice:
    def test_can_create_with_min_amount(self) -> None:
        """最小金額(1円)でPriceが作成できる"""
        # Arrange
        amount = 1

        # Act
        price = Price(amount=amount)

        # Assert
        assert price.value_amount == amount
        assert price.value_currency == "JPY"

    def test_can_create_with_max_amount(self) -> None:
        """最大金額(1000000円)でPriceが作成できる"""
        # Arrange
        amount = 1000000

        # Act
        price = Price(amount=amount)

        # Assert
        assert price.value_amount == amount

    def test_error_when_less_than_min_amount(self) -> None:
        """最小金額未満でPriceを生成するとエラーを投げる"""
        # Arrange
        amount = 0

        # Act & Assert
        with pytest.raises(ValueError, match="価格は1円以上である必要があります。"):
            Price(amount=amount)

    def test_error_when_exceeds_max_amount(self) -> None:
        """最大金額を超えるとPriceを生成するとエラーを投げる"""
        # Arrange
        amount = 1000001

        # Act & Assert
        with pytest.raises(
            ValueError, match="価格は1000000円以下である必要があります。"
        ):
            Price(amount=amount)

    def test_equality_with_same_amount(self) -> None:
        """同じ金額のPriceは等しい"""
        # Arrange & Act
        price1 = Price(amount=500)
        price2 = Price(amount=500)

        # Assert
        assert price1 == price2

    def test_inequality_with_different_amount(self) -> None:
        """異なる金額のPriceは等しくない"""
        # Arrange & Act
        price1 = Price(amount=500)
        price2 = Price(amount=600)

        # Assert
        assert price1 != price2
