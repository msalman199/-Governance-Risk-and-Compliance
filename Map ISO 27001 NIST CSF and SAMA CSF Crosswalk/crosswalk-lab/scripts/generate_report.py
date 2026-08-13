import pandas as pd

def generate_report(crosswalk_csv: str, output_path: str) -> None:
    """
    Generate a summary report (Markdown or HTML) from the crosswalk CSV.

    Args:
        crosswalk_csv: path to crosswalk.csv
        output_path: path to write report (e.g., output/crosswalk_report.md)
    """
    # TODO: Load crosswalk CSV
    # TODO: Compute summary counts: total mapped, equivalent, gaps
    # TODO: Group by category/theme for a breakdown table
    # TODO: Write Markdown report with summary + full table
    pass


if __name__ == "__main__":
    generate_report(
        "../output/crosswalk.csv",
        "../output/crosswalk_report.md"
    )
