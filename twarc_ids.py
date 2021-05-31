import json
import click

from twarc.expansions import ensure_flattened

@click.command()
@click.argument('infile', type=click.File('r'), default='-')
@click.argument('outfile', type=click.File('w'), default='-')
def ids(infile, outfile):
    """
    Extract tweet ids from Twitter API V2 JSON.
    """
    count = 0
    for line in infile:
        count += 1
        line = line.strip()

        # ignore empty lines
        if line:
            try:
                data = json.loads(line)
                for tweet in ensure_flattened(data):
                    click.echo(tweet['id'], file=outfile)
            except ValueError as e:
                click.echo(f"Unexpected JSON data on line {count}", err=True)
                break
            except json.decoder.JSONDecodeError as e:
                click.echo(f"Invalid JSON on line {count}", err=True)
                break
            



