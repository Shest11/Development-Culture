from sales import _parse_record, total

def test_row_parses_valid_line():
    result = _parse_record("coffee,drinks,12.5,3\n")

    assert result == {
        "product_name": "coffee",
        "category": "drinks",
        "unit_price": 12.5,
        "quantity": 3,
    }


def test_total_calculates_sum_with_discount():
    data = [
        {"product_name": "coffee", "category": "drinks", "unit_price": 10.0, "quantity": 2},
        {"product_name": "tea", "category": "drinks", "unit_price": 5.0, "quantity": 4},
    ]

    assert total(data) == 40.0
    assert total(data, 10) == 36.0  