import pytest
from domain.models.book.title.title import Title


class TestTitle:
    def test_can_create_with_1_character(self) -> None:
        """Titleが1文字で作成できる"""
        title_str = "A"
        title = Title(title_str)
        assert title.value == title_str

    def test_can_create_with_1000_characters(self) -> None:
        """Titleが1000文字で作成できる"""
        title_str = "A" * 1000
        title = Title(title_str)
        assert title.value == title_str

    def test_error_when_more_than_max_length(self) -> None:
        """最大長以上の値でTitleを生成するとエラーを投げる"""
        # _MAX_LENGTH = 1000 なので 1001文字でテスト
        title_str = "A" * 1001
        with pytest.raises(ValueError) as excinfo:
            Title(title_str)
        assert "タイトルの文字数が1000以下である必要があります。" in str(excinfo.value)

    def test_error_when_less_than_min_length(self) -> None:
        """最小長未満の値でTitleを生成するとエラーを投げる"""
        # _MIN_LENGTH = 1 なので 0文字でテスト
        title_str = ""
        with pytest.raises(ValueError) as excinfo:
            Title(title_str)
        assert "タイトルの文字数が1以上である必要があります。" in str(excinfo.value)
