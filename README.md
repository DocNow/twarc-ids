# twarc-ids

This module is a simple example of how to create a plugin for [twarc]. It uses
[click-plugins] to extend the main twarc command, and to manage the command
line options.

First you need to install twarc and this plugin:

    pip install twarc
    pip install twarc-ids

Now you can collect data using the core twarc utility:

    twarc search blacklivesmatter > tweets.jsonl

And you have a new subcommand `ids` that is supplied by twarc-ids.

    twarc ids tweets.jsonl > ids.txt

It's good practice to include some tests for your module. See
[test_twarc_ids.py] for an example. You can run these with [pytest]:

    pytest

When creating your setup.py make sure you don't forget the [entry_points magic]
so that twarc will find your plugin when it is installed!

[click-plugins]: https://pypi.org/project/click-plugins/
[pytest]: https://pypi.org/project/pytest/ 
[test_twarc_ids.py]: https://github.com/DocNow/twarc-ids/blob/main/test_twarc_ids.py
[entry_points magic]: https://github.com/DocNow/twarc-ids/blob/main/setup.py#L20-L22
[twarc]: https://github.com/docnow/twarc
