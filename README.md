## mypy config file 

[mypy](https://mypy.readthedocs.io/) does support a config file,
e.g. `setup.cfg`.

## Per-module configuration

`mypy` allows per-module/per-package configuration, see sections
`[mypy-PATTERN]` in `setup.cfg`.

In this example code base we've got errors in `mod.sub1`, which is,
say, a third-party code we import as a git submodule. Since we cannot
control code quality of the third-party software, we'd lie to ignore
type errors in this package. That's done in `[mypy-mod.sub1.*]`
section of the config file.

Once section configurations defined we run `mypy` like this
(`setup.cfg` is applied automatically):

```
$ mypy mod/
```

or by specifiying config file name explicitly:


```
$ mypy --config-file=setup.cfg mod/
```
