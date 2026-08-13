def high_water_mark(ratings: list) -> str:
    """
    Determine the overall impact level using FIPS 199 high-water mark rule.

    Args:
        ratings: List of strings, e.g. ["Low", "Moderate", "High"]

    Returns:
        The highest impact level found (as a string)
    """
    # Order of severity, lowest to highest
    order = ["Low", "Moderate", "High"]

    # TODO: Find the rating in 'ratings' with the highest severity
    # Hint: use order.index() to compare severity levels
    # TODO: Return that rating as a string
    pass


# TODO: Call the function separately for Confidentiality, Integrity, and Availability
# Example:
# c_ratings = ["Low", "Moderate"]
# print("Overall Confidentiality:", high_water_mark(c_ratings))
