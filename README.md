# pc-mobility-print
UNOFFICIAL PaperCut Mobility Print Linux command line client

# Usage

## Get a list of printers

```
python3 ./main.py list
```

## Get a printer IPP URL

```
python3 ./main.py add <printername>
```

## Get a printer description

```
python3 ./main.py desc <printername>
```

## Attempt to automatically add a printer to CUPS

```
python3 ./main.py add <printername>
```

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
