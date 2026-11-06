
import pandas as pd
import pytest

from src.validation import validate_order_items


def sample_data():
    return pd.DataFrame([{
        "order_item_id": "ITEM001",
        "order_id": "ORD001",
        "product_id": "PROD001",
        "quantity": 2,
        "unit_price": 100,
        "discount": 10
    }])


def test_happy_path():
    valid, rejected = validate_order_items(
        sample_data(), ["ORD001"], ["PROD001"]
    )
    assert len(valid) == 1
    assert len(rejected) == 0


def test_empty_input():
    empty = sample_data().iloc[0:0]
    valid, rejected = validate_order_items(
        empty, ["ORD001"], ["PROD001"]
    )
    assert len(valid) == 0
    assert len(rejected) == 0


def test_missing_required_column():
    data = sample_data().drop(columns=["product_id"])
    with pytest.raises(ValueError):
        validate_order_items(data, ["ORD001"], ["PROD001"])


def test_duplicate_records():
    data = pd.concat(
        [sample_data(), sample_data()],
        ignore_index=True
    )
    valid, rejected = validate_order_items(
        data, ["ORD001"], ["PROD001"]
    )
    assert len(valid) == 1
    assert len(rejected) == 1


def test_null_values():
    data = sample_data()
    data.loc[0, "product_id"] = None

    valid, rejected = validate_order_items(
        data, ["ORD001"], ["PROD001"]
    )
    assert len(rejected) == 1


def test_invalid_foreign_key():
    data = sample_data()
    data.loc[0, "product_id"] = "PROD999"

    valid, rejected = validate_order_items(
        data, ["ORD001"], ["PROD001"]
    )
    assert len(rejected) == 1


def test_negative_quantity():
    data = sample_data()
    data.loc[0, "quantity"] = -5

    valid, rejected = validate_order_items(
        data, ["ORD001"], ["PROD001"]
    )
    assert len(rejected) == 1


def test_late_arriving_record():
    data = sample_data()
    # Historical source events are not rejected just for being old.
    data["order_date"] = pd.Timestamp("2024-01-01")

    valid, rejected = validate_order_items(
        data, ["ORD001"], ["PROD001"]
    )
    assert len(valid) == 1
    assert len(rejected) == 0


def test_same_input_is_deterministic():
    data = sample_data()

    valid1, rejected1 = validate_order_items(
        data, ["ORD001"], ["PROD001"]
    )

    valid2, rejected2 = validate_order_items(
        data, ["ORD001"], ["PROD001"]
    )

    pd.testing.assert_frame_equal(valid1, valid2)
    pd.testing.assert_frame_equal(rejected1, rejected2)


def test_processing_failure_is_detected():
    data = sample_data()

    with pytest.raises(ValueError):
        validate_order_items(
            data.drop(columns=["order_id"]),
            ["ORD001"],
            ["PROD001"]
        )
