import inspect
import re

import pytest

import task01
import task02
import task03
import task04
import task05
import task06
import task07
import task08
import task09


# ---- Task 1 ----

def test_task1_if_total_is_asked_only_invoice_calculates_it():
    invoice = task01.Invoice([(10_000, 2), (5_000, 1)])
    assert invoice.total() == 25_000


def test_task1_if_invoice_is_saved_invoice_file_appends_the_total(tmp_path):
    path = tmp_path / "invoices.csv"
    invoice = task01.Invoice([(10_000, 2)])
    task01.InvoiceFile(str(path)).save(invoice)
    task01.InvoiceFile(str(path)).save(invoice)
    assert path.read_text(encoding="utf-8") == "20000\n20000\n"


def test_task1_if_html_is_needed_invoice_html_returns_h1():
    invoice = task01.Invoice([(10_000, 2)])
    assert task01.InvoiceHtml().to_html(invoice) == "<h1>Total: 20000</h1>"


def test_task1_if_items_is_empty_invoice_raises_value_error():
    with pytest.raises(ValueError):
        task01.Invoice([])


# ---- Task 2 ----

def test_task2_if_password_is_wrong_login_returns_false():
    auth = task02.Auth({"ali": "1234"})
    assert auth.login("ali", "0000") is False
    assert auth.login("ali", "1234") is True


def test_task2_if_reset_is_requested_mailer_sends_it(capsys):
    task02.Mailer().send_reset_email("ali@mail.uz")
    assert "ali@mail.uz" in capsys.readouterr().out


def test_task2_if_monthly_bill_runs_billing_prints_the_amount(capsys):
    task02.Billing().bill_monthly("ali", 49_000)
    assert "49000" in capsys.readouterr().out


# ---- Task 3 ----

def test_task3_if_percent_10_price_is_10_percent_lower():
    assert task03.final_price(200_000, task03.Percent(10)) == 180_000


def test_task3_if_fixed_50000_price_is_minus_50000():
    assert task03.final_price(200_000, task03.Fixed(50_000)) == 150_000


def test_task3_if_bogo_price_is_half():
    assert task03.final_price(200_000, task03.Bogo()) == 100_000


def test_task3_if_price_is_lower_than_the_fixed_amount_result_is_0():
    assert task03.final_price(30_000, task03.Fixed(50_000)) == 0


def test_task3_final_price_has_no_if():
    source = inspect.getsource(task03.final_price)
    assert not re.search(r"\bif\b|\belif\b", source)


# ---- Task 4 ----

def test_task4_if_kind_is_student_the_dict_returns_student_discount():
    assert isinstance(task04.make_discount("student"), task04.StudentDiscount)
    assert isinstance(task04.DISCOUNTS["student"](), task04.StudentDiscount)


def test_task4_student_discount_is_15_percent():
    discount = task04.make_discount("student")
    assert task03.final_price(200_000, discount) == 170_000


def test_task4_if_kind_is_unknown_value_error_unknown_discount():
    with pytest.raises(ValueError) as info:
        task04.make_discount("vip")
    assert str(info.value) == "unknown discount"


# ---- Task 5 ----

def test_task5_if_make_fly_gets_sparrow_it_prints_flying(capsys):
    task05.make_fly(task05.Sparrow())
    assert capsys.readouterr().out.strip() == "flying"


def test_task5_if_penguin_there_is_no_fly_and_walk_works():
    penguin = task05.Penguin()
    assert not hasattr(penguin, "fly")
    assert penguin.walk() == "walking"


# ---- Task 6 ----

def test_task6_if_check_gets_rectangle_it_passes():
    task06.check(task06.Rectangle())


def test_task6_if_check_gets_square_inherited_from_rectangle_assertion_error_16():
    with pytest.raises(AssertionError) as info:
        task06.check(task06.BadSquare())
    assert str(info.value) == "16"


def test_task6_if_both_are_siblings_under_shape_square_4_area_is_16_and_no_setters():
    square = task06.Square(4)
    assert square.area() == 16
    assert not hasattr(square, "set_width")
    assert isinstance(square, task06.Shape)
    assert isinstance(task06.Rect(5, 4), task06.Shape)


# ---- Task 7 ----

def test_task7_if_simple_printer_is_only_a_printer_it_has_no_scan_or_fax():
    printer = task07.SimplePrinter()
    assert not hasattr(printer, "scan")
    assert not hasattr(printer, "fax")


def test_task7_if_office_machine_is_printer_and_scanner_both_work():
    machine = task07.OfficeMachine()
    assert "hello" in machine.print("hello")
    assert machine.scan() == "scanning a page"


def test_task7_if_simple_printer_scan_is_called_attribute_error():
    with pytest.raises(AttributeError):
        task07.SimplePrinter().scan()


# ---- Task 8 ----

def test_task8_if_label_printer_is_passed_it_prints_label(capsys):
    task08.print_receipt(task08.LabelPrinter(), "Order #17")
    assert capsys.readouterr().out.strip() == "label: Order #17"


# ---- Task 9 ----

def test_task9_if_file_orders_is_passed_the_order_is_written_to_the_file(tmp_path):
    path = tmp_path / "orders.txt"
    service = task09.OrderService(task09.FileOrders(str(path)))
    service.place("order-17")
    assert path.read_text(encoding="utf-8") == "order-17\n"


def test_task9_if_console_orders_is_passed_the_order_is_printed(capsys):
    task09.OrderService(task09.ConsoleOrders()).place("order-17")
    assert "order-17" in capsys.readouterr().out


def test_task9_if_order_is_empty_place_raises_value_error():
    service = task09.OrderService(task09.ConsoleOrders())
    with pytest.raises(ValueError):
        service.place("")


def test_task9_order_service_does_not_name_any_detail():
    source = inspect.getsource(task09.OrderService)
    assert "FileOrders" not in source
    assert "ConsoleOrders" not in source


def test_task9_repository_is_abstract():
    with pytest.raises(TypeError):
        task09.OrderRepository()
