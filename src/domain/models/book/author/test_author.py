import pytest
from domain.models.book.author.author import Author


class TestAuthor:
    def test_author_can_be_created_with_one_character(self) -> None:
        """1文字でAuthorが作成できる"""
        # Arrange
        author_name = "A"

        # Act
        author = Author(author_name)

        # Assert
        assert author.value == author_name

    def test_author_can_be_created_with_max_length(self) -> None:
        """100文字でAuthorが作成できる"""
        # Arrange
        author_name = "A" * 100

        # Act
        author = Author(author_name)

        # Assert
        assert author.value == author_name

    def test_author_raises_error_when_less_than_min_length(self) -> None:
        """最小長未満の値でAuthorを生成するとエラーを投げる"""
        # Arrange
        author_name = ""

        # Act & Assert
        with pytest.raises(
            ValueError, match="著者名の文字数が1以上である必要があります。"
        ):
            Author(author_name)

    def test_author_raises_error_when_exceeds_max_length(self) -> None:
        """最大長を超える値でAuthorを生成するとエラーを投げる"""
        # Arrange
        author_name = "A" * 101

        # Act & Assert
        with pytest.raises(
            ValueError, match="著者名の文字数が100以下である必要があります。"
        ):
            Author(author_name)
