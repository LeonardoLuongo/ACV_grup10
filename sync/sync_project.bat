@echo off
:: Imposta il percorso della cartella locale (H: corrisponde al tuo Google Drive)
set "TARGET_DIR=H:\My Drive\Uni\Magistrale\colab\2\AV\Project"
:: Imposta il link del tuo repository
set "REPO_URL=https://github.com/LeonardoLuongo/ArtificialVisionGroup17"

echo Controllo della directory: %TARGET_DIR%

:: Se la cartella non esiste, la crea
if not exist "%TARGET_DIR%" mkdir "%TARGET_DIR%"

:: Si sposta nella cartella
cd /d "%TARGET_DIR%"

:: Controlla se esiste la cartella nascosta .git per capire se è già un repo
if exist ".git" (
    echo Repo rilevata. Eseguo GIT PULL...
    git pull
) else (
    echo Cartella vuota o non inizializzata. Eseguo GIT CLONE...
    :: Il punto finale . serve a clonare DENTRO la cartella corrente senza crearne una nuova
    git clone %REPO_URL% .
)

echo.
echo Operazione completata.
pause