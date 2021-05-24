### Python automatic background changer script

#### Requirements 

- Python 3
- feh (https://feh.finalrewind.org/)  
- Time based job scheduler. If using arch-based distros, you can use cronie or systemd timers (see https://wiki.archlinux.org/index.php/cron), otherwise debian-based distros should have it by default

In order for this to work, just add this line to your crontab

```
* * * * * $(which python3) PATH_TO_SCRIPT/pyautobg --directory PATH_TO_YOUR_WALLPAPERS_DIRECTORY
```

#### Installation

Clone this repo and run
`./build.sh PATH_TO_DIST_DIR`

#### Development

- Install Docker & Docker Compose
- Clone this repo and run
- Run: `docker compose up`