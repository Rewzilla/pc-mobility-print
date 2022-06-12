# pc-mobility-print
UNOFFICIAL PaperCut Mobility Print Linux client

# Usage (GUI)

```
python3 ./gui.py
```

# Usage (Command line)

## Get a list of printers

```
python3 ./cli.py list
```

## Get a printer IPP URL

```
python3 ./cli.py get <printername>
```

## Get a printer description

```
python3 ./cli.py desc <printername>
```

## Attempt to automatically add a printer to CUPS

```
python3 ./cli.py add <printername>
```

NOTE: You may need to log into CUPS afterward and specify a driver in order for this to work.

## Optional parameters

```
  -h, --help            show this help message and exit
  -i, --insecure        Don't verify SSL
  -s SERVER, --server SERVER
  -d DOMAIN, --domain DOMAIN
  -u USERNAME, --username USERNAME
  -p PASSWORD, --password PASSWORD
```

# License

[GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.en.html)
