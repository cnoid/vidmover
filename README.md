# vidmover
Simple script to move your video files. Useful if you have left over cache, trailers or need to organize your library.

Detects files below a certain threshold, then moves them. Easy.

Requirements:
- Python 3
  - Ubuntu? For the love of God install python-is-python3
- moviepy
  - `pip install moviepy`
 
Usage:

`python vidmover.py path/to/current/files path/to/file/output SECONDS`


Example:

`python vidmover.py /media/Movies /media/Trailers 420`

Which would move all media files from /media/Movies to /media/Trailers, as long as they're under 420 seconds long (7 minutes).
