from twarc_ids import ids
from click.testing import CliRunner

runner = CliRunner()

def test_v2():
    result = runner.invoke(ids, ['test-data/tweets2.jsonl'])
    assert result.exit_code == 0
    assert result.output == '1366871005755547653\n'

def test_v2_multi():
    result = runner.invoke(ids, ['test-data/tweets3.jsonl'])
    assert result.exit_code == 0
    assert result.output.startswith('1374396236984291339\n')
    assert result.output.endswith('1374395697642885126\n')

def test_v2_flattened():
    result = runner.invoke(ids, ['test-data/tweets4.jsonl'])
    assert result.exit_code == 0
    assert result.output.startswith('1380845952819466249\n')
    assert result.output.endswith('1380845036326301699\n')


