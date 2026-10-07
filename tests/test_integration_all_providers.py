from ai_contractor.providers import PROVIDERS, validate_pair

def test_each_provider_has_a_valid_default_interface():
    for name, provider in PROVIDERS.items():
        validate_pair(name, provider.interfaces[0])
