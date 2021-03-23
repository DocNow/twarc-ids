import json
import click

@click.command()
@click.argument('infile', type=click.File('r'), default='-')
@click.argument('outfile', type=click.File('w'), default='-')
def ids(infile, outfile):
    """
    Extract tweet ids from tweet JSON.
    """
    count = 0
    for line in infile:
        count += 1
        line = line.strip()
        if line:
            try:
                t = json.loads(line)
                if 'id_str' in t:
                    click.echo(t['id_str'], file=outfile)
                elif 'data' in t and 'id' in t['data']:
                    click.echo(t['data']['id'], file=outfile)
                elif 'data' in t and type(t['data']) == list:
                    for tweet in t['data']:
                        click.echo(tweet['id'])
                else:
                    click.echo(f'Unexpected JSON on line {count}')
                    break
            except json.decoder.JSONDecodeError as e:
                click.echo(f"Invalid JSON on line {count}", err=True)
                break
            



