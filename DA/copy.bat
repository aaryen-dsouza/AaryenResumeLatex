REM filepath: /d:/Studies/Masters/CO-OP/AaryenResume/SD/copy_pdf.bat
@echo off
set SOURCE_DIR=d:\Canada\UoW\COOP\AaryenResumeLatex\DA
set DEST_DIR=d:\Canada\JobHunt\FullTime\Current
set SRC_PDF_NAME=main.pdf
set DES_PDF_NAME=AaryenDSouza_DAResume.pdf

echo Copying %SRC_PDF_NAME% from %SOURCE_DIR% to %DEST_DIR%
copy "%SOURCE_DIR%\%SRC_PDF_NAME%" "%DEST_DIR%\%DES_PDF_NAME%"
echo Copy operation completed.

D:\Canada\UoW\COOP\Current