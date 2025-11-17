from pathlib import Path
import shutil
import sys

TARGET_DIR = Path(__file__).resolve().parents[1] / "browserforge" / "datapoints" / "data"

def copy(src: Path, dst_name: str):
    if not src.exists():
        raise FileNotFoundError(str(src))
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    dst = TARGET_DIR / dst_name
    shutil.copyfile(src, dst)
    return dst

def main():
    try:
        from apify_fingerprint_datapoints import (
            get_input_network,
            get_header_network,
            get_fingerprint_network,
            get_headers_order,
            get_browser_helper_file,
        )
    except Exception as e:
        print(f"Missing apify_fingerprint_datapoints: {e}")
        sys.exit(1)

    files = {
        "input-network.zip": get_input_network(),
        "header-network.zip": get_header_network(),
        "fingerprint-network.zip": get_fingerprint_network(),
        "headers-order.json": get_headers_order(),
        "browser-helper-file.json": get_browser_helper_file(),
    }

    written = []
    for name, src in files.items():
        dst = copy(src, name)
        written.append(str(dst))

    print("Written:")
    for p in written:
        print(f" - {p}")

if __name__ == "__main__":
    main()