from helpers import run_cli


def test_top_hotels_draw(tmp_path):
    """Em empate de valor, ordena pelo hotel_id crescente."""
    report = run_cli(
        tmp_path,
        [
            {
                "reservation_id": "R-1",
                "hotel_id": "H03",
                "hotel_name": "Hotel C",
                "status": "CONFIRMED",
                "currency": "BRL",
                "amount": "1000.00",
            },
            {
                "reservation_id": "R-2",
                "hotel_id": "H02",
                "hotel_name": "Hotel B",
                "status": "CONFIRMED",
                "currency": "BRL",
                "amount": "1500.00",
            },
            {
                "reservation_id": "R-3",
                "hotel_id": "H01",
                "hotel_name": "Hotel A",
                "status": "CONFIRMED",
                "currency": "BRL",
                "amount": "1000.00",
            },
        ],
    )

    assert [
        hotel["hotel_id"] for hotel in report["top_hotels"]
    ] == ["H02", "H01", "H03"]