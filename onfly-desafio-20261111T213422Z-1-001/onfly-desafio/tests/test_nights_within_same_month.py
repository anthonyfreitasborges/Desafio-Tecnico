from helpers import run_cli


def test_nights_within_same_month(tmp_path):
    """Calcula as noites entre datas diferentes no mesmo mês."""
    report = run_cli(
        tmp_path,
        [
            {
                "reservation_id": "R-1",
                "checkin_date": "2025-01-10",
                "checkout_date": "2025-01-15",
                "rooms": "1",
            }
        ],
    )
    assert report["summary"]["total_room_nights"] == 5