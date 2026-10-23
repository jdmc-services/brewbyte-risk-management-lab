"""Module 5: public worked example. Extend it for the independent assignment."""
from pathlib import Path
import sys, json
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "labs"))
from brewbyte import run

if __name__ == "__main__":
    print(json.dumps(run(5), indent=2))
