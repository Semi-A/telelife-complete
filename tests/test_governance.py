from packages.core.services.governance import rules_for

def test_dictatorship_has_real_override_rule():
    r=rules_for("dictatorship")
    assert r.public_elections and r.election_starter=="leader" and r.leader_may_override

def test_non_electoral_systems_are_distinct():
    assert not rules_for("monarchy").public_elections
    assert not rules_for("military_junta").public_elections
    assert rules_for("republic").public_elections