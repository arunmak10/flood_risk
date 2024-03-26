from unittest.mock import patch, MagicMock
from run import start

@patch('subprocess.run')
def test_start_with_default_postcode(mock_subprocess, capsys, monkeypatch):
    # This is a part of the integration test to run the entire project end to end
    # Set up input for the test
    inputs = ["", "75"]  # Default postcode followed by inundated area percentage

    # Monkeypatch the input function to provide predefined inputs
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    # Call the start function
    start()

    # Capture the output and verify the expected output
    captured = capsys.readouterr()
    expected_output = "Expected damage for postcode PR1 8HU : 81272.25\n"
    assert captured.out == expected_output
    