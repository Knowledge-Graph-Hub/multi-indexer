# multi-indexer
A utility for creating sets of templated indexes for local or remote directories.

## What does this do? 

The `multi-indexer` creates an Apache HTTPd index-like page dictated by a mustache template. Such a template is provided here in `directory-index-template.html`.

If provided with a remote location on an AWS S3 bucket, it will create an index of remote directories/files.
(It *does not* upload any index files.)

Local indexing is *recursive* - it will index subfolders relative to the provided path.

Remote indexing is *not recursive* - it will create a single index for the provided path only.

## Usage

### Example usage for local indexing, just for local testing
```
mkdir -p /tmp/foo/bar/bib/bab && mkdir -p /tmp/foo/bar/fish && mkdir -p /tmp/foo/bar/foul
touch /tmp/foo/top.md && touch /tmp/foo/bar/bib/bab/bottom.txt && touch /tmp/foo/bar/fish/trout.f && touch /tmp/foo/bar/fish/bass.f
python multi_indexer.py -v --inject ./directory-index-template.html --directory /tmp/foo --prefix file:///tmp/foo -x
```

### Example usage for local indexing, assuming indexes will be uploaded:
```
python3 multi_indexer.py -v --inject ./directory-index-template.html --directory $WORKSPACE/mnt --prefix https://soyouhave.afancy.website/$PROJECTDIR/ -x'
```

### Example usage for remote indexing:
```
python3 multi_indexer.py -v --inject ./directory-index-template.html --prefix https://soyouhave.afancy.website/$PROJECTDIR/ -b a-bucket-name -r $PROJECTDIR -x'
```

## Credits

Adapted from `directory_indexer.py` by Eric Douglass, Seth Carbon, and Justin Reese, originally at
[https://github.com/Knowledge-Graph-Hub/go-site/blob/master/scripts/multi_indexer.py]
