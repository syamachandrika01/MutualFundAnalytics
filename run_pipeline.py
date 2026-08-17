from pathlib import Path
import subprocess
import sys

# Project root folder
BASE_DIR = Path(__file__).resolve().parent


def run_script(script_path):

    full_path = BASE_DIR / script_path

    print("\n" + "=" * 60)
    print(f"Running: {full_path}")
    print("=" * 60)

    if not full_path.exists():
        raise FileNotFoundError(
            f"Script not found: {full_path}"
        )

    result = subprocess.run(
        [sys.executable, str(full_path)],
        cwd=str(BASE_DIR),
        text=True
    )

    print(f"\nExit code: {result.returncode}")

    if result.returncode != 0:
        raise RuntimeError(
            f"{script_path} failed with exit code {result.returncode}"
        )

    print(f"✓ {script_path} completed successfully")


def main():

    print("\n")
    print("=" * 60)
    print("BLUESTOCK MUTUAL FUND ANALYTICS PIPELINE")
    print("=" * 60)

    scripts = [
    "scripts/data_ingestion.py",
    "scripts/data_cleaning.py",
    "scripts/load_database.py"
]

    for script in scripts:
        run_script(script)

    print("\n")
    print("=" * 60)
    print("✓ ALL PIPELINE STEPS COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()