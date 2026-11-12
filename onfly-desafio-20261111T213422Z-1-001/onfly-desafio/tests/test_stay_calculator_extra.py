from datetime import date

from onfly_report.services.stay_calculator import calculate_room_nights


def test_room_nights_dentro_do_mes():
    checkin = date(2026, 10, 10)
    checkout = date(2026, 10, 13)

    resultado = calculate_room_nights(checkin, checkout, rooms=1)

    assert resultado == 3