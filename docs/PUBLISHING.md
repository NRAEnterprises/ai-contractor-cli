# Publishing

Build and test with `scripts/build.sh` and `scripts/test.sh`. Inspect the sdist and wheel before upload. Configure trusted credentials outside the repository. `scripts/publish-testpypi.sh` and `publish-pypi.sh` invoke Twine and intentionally require credentials/environment supplied by the publisher. Verify a clean-environment install afterward. Never commit API tokens.
