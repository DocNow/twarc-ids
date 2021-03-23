import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name='twarc-ids',
    version='0.0.2',
    url='https://github.com/docnow/twarc-ids',
    author='Ed Summers',
    author_email='ehs@pobox.com',
    py_modules=['twarc_ids'],
    description='A twarc plugin to read Twitter data and output the tweet ids',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.3',
    install_requires=['twarc'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points='''
        [twarc.plugins]
        ids=twarc_ids:ids
    '''
)
