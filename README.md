# Dataplan database

Database of provider host names mapped to approximate data usage limits

## Structure

There is one `txt` file per country in the directory `db_limited` and `db_unlimited` (named using the ISO 3166-1 alpha-2 country code). Each `txt` file lists one host name pattern per line. In `db_limited` the DNS names which probably indicate a usage limit (per month) are listed. There, each DNS name pattern is followed by the approximate mean usage limit per month in mega-bytes. E.g.

    *.web.vodafone.de 500
	
The files in `db_unlimited` only list one host name pattern per line. Internet users with this pattern probably have no usage limit per month applied to them.

## How to modify

Submit a pull request with the modified or added entries, please. You will find your host name e.g. at http://ipinfo.io/.

## License

This work is licensed as CC0 1.0 ( https://creativecommons.org/publicdomain/zero/1.0/ ).
