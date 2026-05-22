rem delete rust_mozprofile* folders inside %TEMP% folder
@echo off
setlocal
set "folder=%TEMP%"
for /d %%D in ("%folder%\rust_mozprofile*") do (
    echo Deleting "%%~fD"
    rd /s /q "%%~fD"
)

rem delete all tmp starting folders
for /d %%D in ("%folder%\tmp*") do (
    echo Deleting "%%~fD"
    rd /s /q "%%~fD"
)

