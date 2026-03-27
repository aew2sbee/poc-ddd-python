import pytest
from domain.models.book.author.author import Author


class TestAuthor:
    def test_author_can_be_created_with_one_character(self):
        # 1文字でAuthorが作成できる
        author_name = "A"
        author = Author(author_name)
        assert author.value == author_name

    def test_author_can_be_created_with_one_hundred_characters(self):
        # 100文字でAuthorが作成できる
        author_name = "A" * 100
        author = Author(author_name)
        assert author.value == author_name

    def test_author_raises_error_when_less_than_min_length(self):
        # 最小長未満の値でAuthorを生成するとエラーを投げる
        author_name = ""
        with pytest.raises(ValueError) as excinfo:
            Author(author_name)
        assert "著者名の文字数が1以上である必要があります。" in str(excinfo.value)

    def test_author_raises_error_when_exceeds_max_length(self):
        # 最大長を超える値でAuthorを生成するとエラーを投げる
        author_name = "A" * 101
        with pytest.raises(ValueError) as excinfo:
            Author(author_name)
        assert "著者名の文字数が100以下である必要があります。" in str(excinfo.value)
