"""Command-line interface for warehouse operations."""

import argparse

from warehouse_ops.data_loader import load_products, load_suppliers
from warehouse_ops.inventory import InventoryLedger
from warehouse_ops.reporting import generate_inventory_report, generate_reorder_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="warehouse-ops")
    subparsers = parser.add_subparsers(dest="command")

    report = subparsers.add_parser("report", help="Generate an inventory report")
    report.add_argument("--products", required=True)
    report.add_argument("--suppliers", required=False)

    alerts = subparsers.add_parser("reorder-alerts", help="Show products at or below reorder point")
    alerts.add_argument("--products", required=True)
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "report":
        products = load_products(args.products)
        if args.suppliers:
            load_suppliers(args.suppliers)
        print(generate_inventory_report(products))
        return 0

    if args.command == "reorder-alerts":
        ledger = InventoryLedger(load_products(args.products))
        print(generate_reorder_report(ledger.reorder_alerts()))
        return 0

    parser.print_help()
    return 1
