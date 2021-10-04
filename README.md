# pc-mobility-print
UNOFFICIAL PaperCut Mobility Print Linux command line client

# Usage

## Getting a list of printers

```
python3 ./main.py list
```

## Adding a printer

```
python3 ./main.py add PrinterNameHere
```

## Optional parameters

```
-i           : Don't verify print server SSL
-d DOMAIN    : May or may not need to be specified for your network (ex: corp.local)
-u USERNAME  : Only needed if adding a printer. If not specified, prompt user
-d PASSWORD  : Only needed if adding a printer. If not specified, prompt user
```

# License

[GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.en.html)