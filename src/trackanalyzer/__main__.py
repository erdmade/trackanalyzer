import sys
import argparse
from trackanalyzer.core.parsing import load_kml

def main():
    print("main() started")
    print (sys.executable)

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

        print ("File loaded successfully!")

    except FileNotFoundError:
        print(f"Error: File {args.file} not found.")
        sys.exit(1)

    except Exception as e:
        print(f"{e}")
        sys.exit(1)


if __name__ == "__main__":
    main()