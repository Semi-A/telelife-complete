from packages.core.services.content_filter import inspect

def test_obfuscated_blocked_terms():
    for value in ("کون","کوون","کوووون","ک و ن","ک-و-ن","كـوـن"):
        assert not inspect(value).allowed

def test_boundary_avoids_substring_false_positive():
    assert inspect("کونالا").allowed

def test_clean_persian_content():
    assert inspect("جمهوری روشن فردا").allowed