import pytest
from ignore_file import main

@pytest.mark.parameterize(
        ["inp","expected"],
        [
            (0,1),
            (1,2),
            (2,3)
        ]
)
def test_main(inp:int, expected:int)->None:
    assert main(inp)==expected