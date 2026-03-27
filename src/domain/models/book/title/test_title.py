import pytest
from domain.models.book.title.title import Title


class TestTitle:
    def test_can_create_with_min_length(self) -> None:
        """Titleが1文字で作成できる"""
        # Arrange
        title_str = "A"

        # Act
        title = Title(title_str)

        # Assert
        assert title.value == title_str

    def test_can_create_with_max_length(self) -> None:
        """Titleが1000文字で作成できる"""
        # Arrange
        title_str = "A" * 1000

        # Act
        title = Title(title_str)

        # Assert
        assert title.value == title_str

    def test_error_when_more_than_max_length(self) -> None:
        """最大長を超える値でTitleを生成するとエラーを投げる"""
        # Arrange
        title_str = "A" * 1001

        # Act & Assert
        with pytest.raises(
            ValueError, match="タイトルの文字数が1000以下である必要があります。"
        ):
            Title(title_str)

    def test_error_when_less_than_min_length(self) -> None:
        """最小長未満の値でTitleを生成するとエラーを投げる"""
        # Arrange
        title_str = ""

        # Act & Assert
        with pytest.raises(
            ValueError, match="タイトルの文字数が1以上である必要があります。"
        ):
            Title(title_str)
