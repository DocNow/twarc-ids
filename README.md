# twarc-ids

This module is a simple example of how to create a plugin for twarc. It uses
[click-plugins].

First you need to install twarc and this plugin:

    pip install twarc
    pip install twarc-ids

Now you can collect data using the core twarc utility:

    twarc search blacklivesmatter > tweets.jsonl

And you have a new subcommand `ids` that is supplied by twarc-ids.

    twarc ids tweets.jsonl > ids.txt

It's good practice to include some tests for your module. See test_twarc_ids for an example. You can run these with [pytest]:

    pytest test_twarc_ids

[click-plugins]: https://pypi.org/project/click-plugins/
[pytest]: https://pypi.org/projects/pytest/ 
