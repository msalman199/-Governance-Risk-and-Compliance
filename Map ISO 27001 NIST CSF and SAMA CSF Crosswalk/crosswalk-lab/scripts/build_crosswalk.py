import pandas as pd

def load_catalog(filepath: str, source_name: str) -> pd.DataFrame:
    """
    Load a normalized control catalog CSV and tag it with source framework.

    Args:
        filepath: path to normalized CSV
        source_name: label like 'ISO27001', 'NIST_CSF', 'SAMA_CSF'

    Returns:
        DataFrame with columns: control_id, control_title, category, source
    """
    # TODO: Read CSV with pandas
    # TODO: Rename domain/function/principle column to 'category'
    # TODO: Add a 'source' column with source_name
    # TODO: Return standardized DataFrame
    pass


def build_mapping(iso_df: pd.DataFrame, nist_df: pd.DataFrame,
                   sama_df: pd.DataFrame, mapping_rules: list) -> pd.DataFrame:
    """
    Build crosswalk rows from manual mapping rules.

    Args:
        iso_df, nist_df, sama_df: standardized DataFrames
        mapping_rules: list of dicts, e.g.
            {"iso": "A.5.1", "nist": "GV.PO-01", "sama": "3.1.1", "status": "Equivalent"}

    Returns:
        DataFrame with resolved titles per framework and mapping status
    """
    # TODO: For each rule, look up control_title in each DataFrame by control_id
    # TODO: Handle missing mappings (status = "Gap") when a rule leaves a field blank
    # TODO: Assemble into a single crosswalk DataFrame
    pass


def find_gaps(crosswalk_df: pd.DataFrame) -> pd.DataFrame:
    """
    Identify controls present in one framework but unmapped in others.

    Returns:
        DataFrame filtered to rows where status == 'Gap'
    """
    # TODO: Filter crosswalk_df for gap rows
    pass


if __name__ == "__main__":
    # TODO: Call load_catalog() for each normalized CSV
    # TODO: Define mapping_rules list covering policy, vulnerability mgmt,
    #       monitoring, and incident management controls
    # TODO: Call build_mapping() and find_gaps()
    # TODO: Save results to ~/crosswalk-lab/output/crosswalk.csv
    print("Crosswalk build script - complete the TODOs")
