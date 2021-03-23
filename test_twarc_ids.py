from twarc_ids import ids
from click.testing import CliRunner

def test_v1():
    runner = CliRunner()
    result = runner.invoke(ids, ['test-data/tweets1.jsonl'])
    assert result.exit_code == 0
    assert result.output == '1366587408960147459\n'

def test_v2():
    runner = CliRunner()
    result = runner.invoke(ids, ['test-data/tweets2.jsonl'])
    assert result.exit_code == 0
    assert result.output == '1366871005755547653\n'

def test_v2_multi():
    runner = CliRunner()
    result = runner.invoke(ids, ['test-data/tweets3.jsonl'])
    assert result.exit_code == 0
    assert result.output.startswith('1374396236984291339\n')
    assert result.output.endswith('1374395697642885126\n')
