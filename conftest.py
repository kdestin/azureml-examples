import pytest
from pathlib import Path

pytest_plugins = ["dev.pytest_plugins._jupyter_plugin"]



@pytest.fixture
def notebook_parameters():
    return dict(a=1, b=2, c=3)


if __name__ == "__main__":
    pytest.main([str(Path(__file__).parent / "sdk" / "python"), "-x", "--color=no"])
