import csv
import json
import os
import random
import string
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from xml.dom import minidom

import pandas as pd
from faker import Faker

fake = Faker()

# Constants for data generation
BROKERS = [
    "Goldman Sachs",
    "JP Morgan",
    "Morgan Stanley",
    "Deutsche Bank",
    "Barclays",
    "Citigroup",
    "Bank of America",
    "Credit Suisse",
    "UBS",
    "HSBC",
    "BNP Paribas",
    "Nomura",
    "RBC Capital Markets",
    "Wells Fargo",
    "Societe Generale",
]

INSTRUMENTS = [
    "AAPL",
    "MSFT",
    "GOOGL",
    "AMZN",
    "TSLA",
    "META",
    "NVDA",
    "JPM",
    "BAC",
    "XOM",
    "EURUSD",
    "GBPUSD",
    "USDJPY",
    "AUDUSD",
    "USDCAD",
    "USDCHF",
    "NZDUSD",
    "EURGBP",
    "BTCUSD",
    "ETHUSD",
    "XRPUSD",
    "LTCUSD",
    "BCHUSD",
    "ADAUSD",
    "DOTUSD",
    "SOLUSD",
    "SPY",
    "QQQ",
    "IWM",
    "VTI",
    "VOO",
    "VUG",
    "VB",
    "VEA",
    "VWO",
    "AGG",
    "TLT",
]

ASSET_CLASSES = [
    "Equity",
    "Fixed Income",
    "FX",
    "Commodity",
    "Cryptocurrency",
    "Derivative",
    "ETF",
    "Bond",
]

CURRENCIES = [
    "USD",
    "EUR",
    "GBP",
    "JPY",
    "CHF",
    "CAD",
    "AUD",
    "NZD",
    "INR",
    "CNY",
    "SGD",
    "HKD",
]

TRADE_TYPES = [
    "Spot",
    "Forward",
    "Future",
    "Option",
    "Swap",
    "Margin",
    "Intraday",
    "Delivery",
]

TRADE_SIDES = ["Buy", "Sell", "Buy Cover", "Sell Short"]

COUNTERPARTIES = [
    "Hedge Fund Alpha",
    "Pension Fund Beta",
    "Asset Manager Gamma",
    "Insurance Co Delta",
    "Corporate Treasury Epsilon",
    "Family Office Zeta",
    "Sovereign Wealth Eta",
    "Endowment Theta",
]

TRADING_VENUES = [
    "NYSE",
    "NASDAQ",
    "LSE",
    "TSE",
    "HKEX",
    "SSE",
    "Euronext",
    "Deutsche Boerse",
    "BATS",
    "Chi-X",
    "Dark Pool A",
    "Dark Pool B",
    "MTF",
    "OTC",
]

SECTORS = [
    "Technology",
    "Healthcare",
    "Financials",
    "Energy",
    "Consumer Discretionary",
    "Industrials",
    "Materials",
    "Utilities",
    "Real Estate",
    "Communication Services",
    "Consumer Staples",
    "Telecommunications",
]

INDUSTRIES = [
    "Software",
    "Biotechnology",
    "Investment Banking",
    "Oil & Gas",
    "Retail",
    "Aerospace",
    "Chemicals",
    "Electric Utilities",
    "REITs",
    "Media",
    "Food & Beverage",
    "Wireless Communications",
]

RATING_AGENCIES = ["S&P", "Moody's", "Fitch", "DBRS", "Morningstar"]

COUNTRIES = [
    "USA",
    "UK",
    "Germany",
    "France",
    "Japan",
    "China",
    "Singapore",
    "Hong Kong",
    "Switzerland",
    "Canada",
    "Australia",
    "India",
    "Brazil",
    "Mexico",
    "South Korea",
]

REGIONS = [
    "North America",
    "Europe",
    "Asia-Pacific",
    "Emerging Markets",
    "Latin America",
]

SETTLEMENT_TYPES = ["DVP", "Free of Payment", "Netting", "Gross", "Hold in Custody"]

CONFIRMATION_METHODS = [
    "SWIFT",
    "Email",
    "Fax",
    "DTCC",
    "Omgeo",
    "Manual",
    "Electronic",
]


def generate_trade_record(trade_index):
    """Generate a single trade record with 70+ attributes."""
    # Base dates
    trade_date = fake.date_between(start_date="-2y", end_date="today")
    settlement_date = trade_date + timedelta(days=random.choice([0, 1, 2, 3, 5, 7, 10, 30]))
    maturity_date = trade_date + timedelta(days=random.choice([30, 60, 90, 180, 365, 730, 1095]))
    entry_date = trade_date - timedelta(days=random.randint(0, 5))

    # Base values
    quantity = random.randint(1, 1000000)
    price = round(random.uniform(0.01, 100000), 4)
    notional = round(quantity * price, 2)

    # Derived calculations
    fx_rate = round(random.uniform(0.5, 150), 6)
    market_value = round(notional * fx_rate, 2)

    # Risk metrics
    var_95 = round(notional * random.uniform(0.01, 0.05), 2)
    var_99 = round(var_95 * 1.5, 2)
    delta = round(random.uniform(-1, 1), 4)
    gamma = round(random.uniform(0, 0.1), 6)
    vega = round(random.uniform(0, 100), 2)
    theta = round(random.uniform(-10, 0), 4)

    # Pricing metrics
    accrued_interest = round(random.uniform(0, 1000), 2)
    clean_price = price
    dirty_price = round(
        clean_price + (accrued_interest / (notional / quantity) if notional > 0 else 0),
        4,
    )
    yield_pct = round(random.uniform(-5, 15), 4)
    spread_bps = round(random.uniform(-100, 500), 2)

    # Reference data
    isin = f"US{random.randint(1000000000, 9999999999)}"
    cusip = "".join(random.choices(string.ascii_uppercase + string.digits, k=9))
    sedol = "".join(random.choices(string.ascii_uppercase + string.digits, k=7))
    bloomberg_ticker = (
        f"{random.choice(INSTRUMENTS)} {random.choice(['US', 'UK', 'GR', 'JP'])} Equity"
    )

    # Party information
    broker = random.choice(BROKERS)
    trader_id = f"TRD{random.randint(1000, 9999)}"
    sales_person = fake.name()
    counterparty = random.choice(COUNTERPARTIES)
    counterparty_lei = f"{random.randint(10000000000000000000, 99999999999999999999)}"

    # Trade details
    trade_type = random.choice(TRADE_TYPES)
    trade_side = random.choice(TRADE_SIDES)
    asset_class = random.choice(ASSET_CLASSES)
    instrument = random.choice(INSTRUMENTS)
    currency = random.choice(CURRENCIES)

    record = {
        # 1. Trade Identification (10 attributes)
        "trade_id": f"TR-{trade_index:010d}",
        "order_id": f"ORD-{random.randint(1000000, 9999999)}",
        "execution_id": f"EXC-{random.randint(100000000, 999999999)}",
        "allocation_id": f"ALL-{trade_index:08d}",
        "block_id": f"BLK-{random.randint(10000, 99999)}",
        "parent_order_id": (
            f"PAR-{random.randint(100000, 999999)}" if random.random() > 0.7 else None
        ),
        "client_order_id": f"CLI-{random.randint(10000000, 99999999)}",
        "originating_system": random.choice(["OMS", "EMS", "FIX", "API", "Manual"]),
        "version": random.randint(1, 5),
        "previous_version": random.randint(1, 4) if random.random() > 0.8 else None,
        # 2. Trade Details (15 attributes)
        "trade_date": str(trade_date),
        "trade_time": fake.time(),
        "entry_date": str(entry_date),
        "entry_time": fake.time(),
        "settlement_date": str(settlement_date),
        "maturity_date": str(maturity_date),
        "value_date": str(settlement_date),
        "effective_date": str(trade_date),
        "termination_date": str(maturity_date),
        "trade_type": trade_type,
        "trade_side": trade_side,
        "asset_class": asset_class,
        "instrument_symbol": instrument,
        "instrument_name": f"{instrument} {asset_class}",
        "instrument_type": random.choice(
            ["Common Stock", "Preferred", "ADR", "ETF", "Bond", "Option", "Future"]
        ),
        # 3. Instrument Identification (10 attributes)
        "isin": isin,
        "cusip": cusip,
        "sedol": sedol,
        "bloomberg_ticker": bloomberg_ticker,
        "reuters_ric": f"{instrument}.{random.choice(['L', 'N', 'O', 'Z'])}",
        "bbgid": f"BBG{random.randint(10000000000, 99999999999)}",
        "exchange_code": random.choice(TRADING_VENUES),
        "mic_code": random.choice(["XNYS", "XNAS", "XLON", "XTKS", "XHKG", "XSHG", "XPAR", "XETR"]),
        "sedol_code": sedol,
        "figi": f"BBG{random.randint(1000000000000, 9999999999999)}",
        # 4. Pricing & Quantity (12 attributes)
        "quantity": quantity,
        "price": price,
        "notional_amount": notional,
        "notional_currency": currency,
        "market_price": round(price * random.uniform(0.95, 1.05), 4),
        "clean_price": clean_price,
        "dirty_price": dirty_price,
        "accrued_interest": accrued_interest,
        "yield_percent": yield_pct,
        "spread_bps": spread_bps,
        "day_count_convention": random.choice(
            ["30/360", "Actual/360", "Actual/365", "Actual/Actual"]
        ),
        "price_multiplier": random.choice([1, 100, 1000]),
        # 5. Party Information (10 attributes)
        "broker": broker,
        "broker_id": f"BRK{random.randint(100, 999)}",
        "trader_id": trader_id,
        "trader_name": fake.name(),
        "sales_person": sales_person,
        "sales_desk": random.choice(["Cash", "Derivatives", "FX", "Rates", "Credit", "Equity"]),
        "counterparty": counterparty,
        "counterparty_lei": counterparty_lei,
        "counterparty_account": f"ACC{random.randint(10000000, 99999999)}",
        "clearing_house": random.choice(
            ["DTC", "Euroclear", "Clearstream", "LCH", "CME Clearport"]
        ),
        # 6. Risk Metrics (10 attributes)
        "var_95": var_95,
        "var_99": var_99,
        "expected_shortfall": round(var_99 * 1.2, 2),
        "delta": delta,
        "gamma": gamma,
        "vega": vega,
        "theta": theta,
        "rho": round(random.uniform(-100, 100), 2),
        "pv01": round(notional * 0.0001, 2),
        "cs01": round(notional * 0.0001 * random.uniform(0.5, 2), 2),
        # 7. Reference Data (10 attributes)
        "sector": random.choice(SECTORS),
        "industry": random.choice(INDUSTRIES),
        "country_of_risk": random.choice(COUNTRIES),
        "country_of_incorporation": random.choice(COUNTRIES),
        "region": random.choice(REGIONS),
        "credit_rating": random.choice(
            [
                "AAA",
                "AA+",
                "AA",
                "AA-",
                "A+",
                "A",
                "A-",
                "BBB+",
                "BBB",
                "BB+",
                "BB",
                "NR",
            ]
        ),
        "rating_agency": random.choice(RATING_AGENCIES),
        "issuer_name": fake.company(),
        "issuer_lei": f"{random.randint(10000000000000000000, 99999999999999999999)}",
        "market_cap_tier": random.choice(["Large Cap", "Mid Cap", "Small Cap", "Micro Cap"]),
        # 8. Calculated Fields (8 attributes)
        "market_value": market_value,
        "unrealized_pnl": round(random.uniform(-notional * 0.2, notional * 0.2), 2),
        "realized_pnl": (
            round(random.uniform(0, notional * 0.1), 2) if random.random() > 0.7 else 0
        ),
        "total_pnl": None,  # Will be calculated
        "dv01": round(notional * 0.0001, 2),
        "cr01": round(notional * 0.0001 * random.uniform(0.8, 1.2), 2),
        "ie01": round(notional * 0.0001 * random.uniform(0.9, 1.1), 2),
        "as01": round(notional * 0.0001 * random.uniform(0.7, 1.3), 2),
        # 9. Settlement & Clearing (8 attributes)
        "settlement_type": random.choice(SETTLEMENT_TYPES),
        "settlement_currency": random.choice(CURRENCIES),
        "settlement_amount": round(notional * fx_rate, 2),
        "settlement_fx_rate": fx_rate,
        "clearing_status": random.choice(["Pending", "Cleared", "Failed", "Resolved"]),
        "confirmation_method": random.choice(CONFIRMATION_METHODS),
        "allocation_status": random.choice(["Pending", "Allocated", "Rejected"]),
        "affirmation_status": random.choice(["Pending", "Affirmed", "Disputed"]),
        # 10. Regulatory & Compliance (8 attributes)
        "reporting_jurisdiction": random.choice(COUNTRIES),
        "mifid_ii_reportable": random.choice([True, False]),
        "emir_reportable": random.choice([True, False]),
        "cftc_reportable": random.choice([True, False]),
        "esma_category": random.choice(["Professional", "Retail", "Eligible Counterparty"]),
        "transaction_reporting_status": random.choice(["Reported", "Pending", "Exempt"]),
        "sfd_indicator": random.choice([True, False]),
        "rts_27_reportable": random.choice([True, False]),
        # 11. Status & Timestamps (8 attributes)
        "trade_status": random.choice(["New", "Amended", "Cancelled", "Pending", "Completed"]),
        "lifecycle_status": random.choice(["Open", "Closed", "Matured", "Terminated"]),
        "booking_status": random.choice(["Booked", "Pending", "Error", "Reversed"]),
        "confirmation_status": random.choice(["Unconfirmed", "Confirmed", "Disputed"]),
        "settlement_status": random.choice(["Unsettled", "Settled", "Failed"]),
        "created_timestamp": f"{entry_date}T{fake.time()}",
        "modified_timestamp": f"{trade_date}T{fake.time()}",
        "user_created": fake.email(),
        # 12. Additional Attributes (10 attributes)
        "trading_venue": random.choice(TRADING_VENUES),
        "venue_mic": random.choice(["XNYS", "XNAS", "XLON", "XTKS", "XHKG"]),
        "execution_venue": random.choice(TRADING_VENUES),
        "algo_strategy": random.choice(
            ["VWAP", "TWAP", "Implementation Shortfall", "Arrival Price", "POV", None]
        ),
        "participation_rate": (round(random.uniform(5, 30), 2) if random.random() > 0.5 else None),
        "arrival_price": round(price * random.uniform(0.99, 1.01), 4),
        "benchmark_price": round(price * random.uniform(0.98, 1.02), 4),
        "slippage_bps": round(random.uniform(-50, 50), 2),
        "market_impact_bps": round(random.uniform(-20, 20), 2),
        "opportunity_cost": round(random.uniform(-1000, 1000), 2),
        # 13. FX Specific (8 attributes)
        "base_currency": random.choice(CURRENCIES),
        "quote_currency": random.choice(CURRENCIES),
        "spot_rate": fx_rate,
        "forward_points": (round(random.uniform(-500, 500), 4) if asset_class == "FX" else None),
        "forward_rate": (
            round(fx_rate * (1 + random.uniform(-0.1, 0.1)), 6) if asset_class == "FX" else None
        ),
        "value_date_spot": str(settlement_date),
        "fixing_date": str(trade_date) if asset_class == "FX" else None,
        "fixing_source": random.choice(["ECB", "FED", "BOE", "WMR", "Bloomberg"]),
        # 14. Documentation (6 attributes)
        "master_agreement_type": random.choice(["ISDA", "GMRA", "MSLA", "NA"]),
        "master_agreement_date": str(fake.date_between(start_date="-10y", end_date="-1y")),
        "csa_in_place": random.choice([True, False]),
        "collateral_currency": random.choice(CURRENCIES),
        "collateral_amount": round(random.uniform(0, notional * 0.1), 2),
        "netting_agreement": random.choice([True, False]),
        # 15. Audit & Metadata (8 attributes)
        "source_system": random.choice(["Trading Platform", "EMS", "OMS", "Excel Upload", "FIX"]),
        "data_quality_score": round(random.uniform(0, 100), 2),
        "validation_status": random.choice(["Valid", "Warning", "Error"]),
        "etl_timestamp": datetime.now().isoformat(),
        "batch_id": f"BATCH-{datetime.now().strftime('%Y%m%d')}-{random.randint(1000, 9999)}",
        "is_internal_transfer": random.choice([True, False]),
        "is_backdated": random.choice([True, False]),
        "backdate_reason": random.choice(
            ["Error Correction", "Late Booking", "System Issue", None]
        ),
    }

    # Calculate total PnL
    record["total_pnl"] = round((record["unrealized_pnl"] or 0) + (record["realized_pnl"] or 0), 2)

    return record


def generate_dataset(num_records=1000):
    """Generate a dataset of trade records."""
    records = []
    for i in range(1, num_records + 1):
        records.append(generate_trade_record(i))
    return records


def save_to_json(records, filename="trades.json"):
    """Save records to JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, default=str)
    print(f"✓ Saved JSON: {filename} ({len(records)} records)")


def save_to_csv(records, filename="trades.csv"):
    """Save records to CSV file."""
    if not records:
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)
    print(f"✓ Saved CSV: {filename} ({len(records)} records)")


def save_to_xlsx(records, filename="trades.xlsx"):
    """Save records to Excel file."""
    try:

        df = pd.DataFrame(records)
        df.to_excel(filename, index=False, engine="openpyxl")
        print(f"✓ Saved Excel: {filename} ({len(records)} records)")
    except ImportError:
        print("✗ pandas/openpyxl not installed. Skipping Excel export.")


def save_to_xml(records, filename="trades.xml"):
    """Save records to XML file."""
    root = ET.Element("trades")

    for record in records:
        trade_elem = ET.SubElement(root, "trade")
        for key, value in record.items():
            child = ET.SubElement(trade_elem, key)
            if value is not None:
                child.text = str(value)

    # Pretty print XML
    rough_string = ET.tostring(root, encoding="unicode")
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(pretty_xml)
    print(f"✓ Saved XML: {filename} ({len(records)} records)")


def main():
    """Main function to generate datasets."""
    print("=" * 60)
    print("Financial Trade Data Generator")
    print("=" * 60)

    # Get number of records from user or use default
    try:
        num_records = int(input("Enter number of records to generate (default: 1000): ") or 1000)
    except ValueError:
        num_records = 1000

    print(f"\nGenerating {num_records:,} trade records with 70+ attributes...")
    print("-" * 60)

    # Generate data
    records = generate_dataset(num_records)

    # Display sample
    print(f"\nSample record (Trade ID: {records[0]['trade_id']}):")
    print(f"  - Trade Date: {records[0]['trade_date']}")
    print(f"  - Instrument: {records[0]['instrument_symbol']}")
    print(f"  - Broker: {records[0]['broker']}")
    print(f"  - Total attributes: {len(records[0])}")
    print("-" * 60)

    # Create output directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"trade_data_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    print(f"\nOutput directory: {output_dir}/")

    # Export to all formats
    print("\nExporting data...")

    save_to_json(records, os.path.join(output_dir, "trades.json"))
    save_to_csv(records, os.path.join(output_dir, "trades.csv"))
    save_to_xlsx(records, os.path.join(output_dir, "trades.xlsx"))
    save_to_xml(records, os.path.join(output_dir, "trades.xml"))

    # Summary
    print("-" * 60)
    print("\nGeneration Complete!")
    print(f"Total records: {num_records:,}")
    print(f"Attributes per record: {len(records[0])}")
    print(f"Output folder: {output_dir}/")
    print("\nFiles generated:")
    for f in ["trades.json", "trades.csv", "trades.xlsx", "trades.xml"]:
        filepath = os.path.join(output_dir, f)
        if os.path.exists(filepath):
            size = os.path.getsize(filepath) / (1024 * 1024)  # MB
            print(f"  - {f}: {size:.2f} MB")
    print("=" * 60)


if __name__ == "__main__":
    main()
