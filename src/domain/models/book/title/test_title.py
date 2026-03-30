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
        title_str = "A" * Title._MAX_LENGTH

        # Act
        title = Title(title_str)

        # Assert
        assert title.value == title_str

    def test_error_when_more_than_max_length(self) -> None:
        """最大長を超える値でTitleを生成するとエラーを投げる"""
        # Arrange
        title_str = "A" * (Title._MAX_LENGTH + 1)

        # Act & Assert
        with pytest.raises(ValueError, match=Title._INVALID_MAX_LENGTH):
            Title(title_str)

    def test_error_when_less_than_min_length(self) -> None:
        """最小長未満の値でTitleを生成するとエラーを投げる"""
        # Arrange
        title_str = "A" * (Title._MIN_LENGTH - 1)

        # Act & Assert
        with pytest.raises(ValueError, match=Title._INVALID_MIN_LENGTH):
            Title(title_str)

    def test_immutable_cannot_reassign_value(self) -> None:
        """生成後に_valueを再代入するとAttributeErrorになる"""
        # Arrange
        title = Title("Python入門")

        # Act & Assert
        with pytest.raises(AttributeError):
            title._value = "改ざんされた値"

    def test_immutable_cannot_delete_value(self) -> None:
        """生成後に_valueを削除するとAttributeErrorになる"""
        # Arrange
        title = Title("Python入門")

        # Act & Assert
        with pytest.raises(AttributeError):
            del title._value

    def test_immutable_cannot_add_new_attribute(self) -> None:
        """生成後に新しい属性を追加するとAttributeErrorになる"""
        # Arrange
        title = Title("Python入門")

        # Act & Assert
        with pytest.raises(AttributeError):
            title.new_attr = "不正な属性"
