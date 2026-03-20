from logic_utils import check_guess, get_range_for_difficulty, update_score


# --- Bug 1: Hard difficulty range is easier than Normal ---
# get_range_for_difficulty("Hard") returns (1, 50), but Normal returns (1, 100).
# Hard should have a *larger* range (harder to guess), not a smaller one.

def test_hard_range_is_harder_than_normal():
    """Hard mode should have a larger range than Normal, not a smaller one."""
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high, (
        f"Hard range upper bound ({hard_high}) should be greater than "
        f"Normal's ({normal_high}), but it is not — Hard is currently easier than Normal."
    )

def test_easy_range_is_easier_than_normal():
    """Easy mode should have a smaller range than Normal."""
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    assert easy_high < normal_high, (
        f"Easy range upper bound ({easy_high}) should be less than Normal's ({normal_high})."
    )


# --- Bug 2: check_guess can never return "Win" when secret is a string ---
# On even attempts, app.py passes secret as str(secret), so guess_int == secret
# evaluates as int == str which is always False in Python 3.

def test_check_guess_win_returns_tuple():
    """check_guess should return a tuple (outcome, message)."""
    result = check_guess(50, 50)
    assert isinstance(result, tuple) and len(result) == 2, (
        "check_guess should return a (outcome, message) tuple."
    )

def test_check_guess_win_with_int_secret():
    """Exact match with int secret should be a win."""
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_check_guess_win_with_string_secret():
    """Exact match should still be a win even when secret is passed as a string.
    Bug: 50 == '50' is False in Python 3, so this never returns 'Win'."""
    outcome, _ = check_guess(50, "50")
    assert outcome == "Win", (
        "check_guess(50, '50') should return 'Win', but it does not "
        "because int == str is always False in Python 3."
    )

def test_check_guess_too_high_with_string_secret():
    """Guess higher than secret (string) should still report Too High."""
    outcome, _ = check_guess(60, "50")
    assert outcome == "Too High"

def test_check_guess_too_low_with_string_secret():
    """Guess lower than secret (string) should still report Too Low."""
    outcome, _ = check_guess(40, "50")
    assert outcome == "Too Low"


