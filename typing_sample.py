import dataclasses
from decimal import Decimal
from typing import NotRequired, Protocol, TypedDict


class Item(Protocol):
    quantity: float
    price: Decimal


@dataclasses.dataclass
class Product:
    quantity: float
    price: Decimal
    name: str


@dataclasses.dataclass
class StockItem:
    quantity: float
    price: Decimal
    sku: str


class OptDict(TypedDict):
    min_quantity: float | None
    min_price: NotRequired[Decimal]


def calculate(items: list[Item], options: OptDict | None) -> Decimal | int:
    options = options or OptDict(min_quantity=0)
    values = [
        Decimal(format(item.quantity, ".2f")) * item.price
        for item in items
        if not options["min_quantity"]
        or options["min_quantity"] <= item.quantity
        and options.get("min_price", 0) <= item.price
    ]
    return sum(values)


if __name__ == "__main__":
    quantity: float = 3.5
    base_price: Decimal = Decimal("10.0")

    p1 = Product(quantity=quantity, price=base_price, name="product1")
    p2 = Product(quantity=2, price=Decimal("5.0"), name="product2")
    s1 = StockItem(quantity=2.1, price=Decimal("10.0"), sku="stock1")
    s2 = StockItem(quantity=1.9, price=Decimal("1.0"), sku="stock2")

    total = calculate([p1, p2, s1, s2], {"min_quantity": 2, "min_price": Decimal("2.0")})
    print(f"Total: {total}")
