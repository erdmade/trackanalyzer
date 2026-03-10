import sys
import argparse
import logging
from trackanalyzer.core.parsing import load_kml

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger(__name__)

def main():

    parser = argparse.ArgumentParser(
        description="Track Analyzer - load a KML file and view track on a map."
    )
    parser.add_argument(
        "file", 
        nargs = "?",
        help="Path to KML file."
    )
    args = parser.parse_args()

    if args.file is None:
        args.file = input("Enter KML file location:").strip()

    try:
        track = load_kml(args.file)

    except FileNotFoundError:
        print(f"Error: File {args.file} not found.")
        sys.exit(1)

    except Exception as e:
        print(f"{e}")
        sys.exit(1)


if __name__ == "__main__":
    main()