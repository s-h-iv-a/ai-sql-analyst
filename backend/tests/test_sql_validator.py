import pytest

from app.utils.sql_validator import validate_sql


def test_validate_sql_allows_select():
    sql = "SELECT name FROM products"
    assert validate_sql(sql) == sql


def test_validate_sql_blocks_delete():
    with pytest.raises(ValueError, match="Only SELECT"):
        validate_sql("DELETE FROM products")


def test_validate_sql_blocks_multiple_statements():
    with pytest.raises(ValueError, match="Multiple SQL"):
        validate_sql("SELECT 1; DROP TABLE products")
