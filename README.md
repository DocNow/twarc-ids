# twarc-ids

This module is a simple reference implementation of a [twarc] plugin. It uses
[click-plugins] to extend the main twarc command with an 'ids' subcommand that
reads tweet data and writes out their identifiers.

It also is an example of using `twarc.ensure_flattened` to make ensure that
data has been "flattened" to make it easier to process Twitter API data as
a stream of tweets where referenced entities (users, media, etc) have had their
ids turned into objects. While not strictly needed for this plugin it does make
it easier to read the data since API responses can contain one tweet in the
payload or a list of tweets.

## Install

First you need to install twarc and this plugin:

    pip install twarc
    pip install twarc-ids

Now you can collect data using the core twarc utility:

    twarc search blacklivesmatter > tweets.jsonl

And you have a new subcommand `ids` that is supplied by twarc-ids.

    twarc ids tweets.jsonl > ids.txt

It's good practice to include some tests for your module. See
[test_twarc_ids.py] for an example. You can run it directly with [pytest] or
using:

    python setup.py test

When creating your setup.py make sure you don't forget the [entry_points magic]
so that twarc will find your plugin when it is installed!

[click-plugins]: https://pypi.org/project/click-plugins/
[pytest]: https://pypi.org/project/pytest/ 
[test_twarc_ids.py]: https://github.com/DocNow/twarc-ids/blob/main/test_twarc_ids.py
[entry_points magic]: https://github.com/DocNow/twarc-ids/blob/main/setup.py#L20-L22
[twarc]: https://github.com/docnow/twarc
