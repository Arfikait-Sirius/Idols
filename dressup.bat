@ECHO OFF

set DIR_IDOLS=%1\idols

IF NOT exist %DIR_IDOLS% (
     mkdir %DIR_IDOLS%
     type null > %DIR_IDOLS%\__init.py__
)

copy .\dir_Modules\Idols.py %1\. > NUL
copy .\dir_Girls\Louise\Louise.py %DIR_IDOLS%\. > NUL
copy .\dir_Girls\Emily\Emily.py %DIR_IDOLS%\. > NUL

echo Completed!
