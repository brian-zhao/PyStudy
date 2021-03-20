# Cheat Sheet for Random stuff
#### Table of Contents
[The Silver Searcher](#silver_searcher)


<a name="silver_searcher"/>
## The Silver Searcher.

```
brew install the_silver_searcher
```

Filter by file extension or file name (using -G flag):
```
ag -G .markdown dnsimple
```

Regular expresion search:
```
ag tiny[-_]p
```

Search compressed files using -z flag:
```
ag -z -G .zip packed
```

It parses from stdin (as any good UNIX tool should):
```
ag --help | ag search
```