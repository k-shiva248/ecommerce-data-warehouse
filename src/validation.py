
import pandas as pd


def validate_order_items(df, valid_order_ids, valid_product_ids):

    required_columns = [
        "order_item_id", "order_id", "product_id",
        "quantity", "unit_price", "discount"
    ]

    missing = set(required_columns) - set(df.columns)

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    data = df.copy()
    data["rejection_reason"] = ""

    def add_reason(mask, reason):
        data.loc[mask, "rejection_reason"] = (
            data.loc[mask, "rejection_reason"].apply(
                lambda x: f"{x}; {reason}" if x else reason
            )
        )

    for column in required_columns:
        add_reason(data[column].isna(), f"missing_{column}")

    duplicate_mask = (
        data["order_item_id"].duplicated(keep="first")
        & data["order_item_id"].notna()
    )
    add_reason(duplicate_mask, "duplicate_order_item_id")

    add_reason(
        ~data["order_id"].isin(valid_order_ids),
        "invalid_order_id"
    )

    add_reason(
        ~data["product_id"].isin(valid_product_ids),
        "invalid_product_id"
    )

    for column in ["quantity", "unit_price", "discount"]:
        data[column] = pd.to_numeric(
            data[column], errors="coerce"
        )

    for column in ["quantity", "unit_price", "discount"]:
        add_reason(
            data[column].isna(),
            f"invalid_{column}"
        )

    add_reason(data["quantity"].le(0), "invalid_quantity")
    add_reason(data["unit_price"].le(0), "invalid_unit_price")
    add_reason(data["discount"].lt(0), "negative_discount")

    gross = data["quantity"] * data["unit_price"]

    add_reason(
        data["discount"].gt(gross),
        "discount_exceeds_gross_amount"
    )

    valid = data[data["rejection_reason"] == ""].drop(
        columns="rejection_reason"
    )

    rejected = data[data["rejection_reason"] != ""]

    return valid.copy(), rejected.copy()
