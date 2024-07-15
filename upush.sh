#!/bin/bash

# Chiede all'utente di inserire il messaggio di commit
read -p "Inserisci il messaggio di commit: " commit_message

# Aggiunge tutti i file modificati allo staging area
git add .

# Esegue il commit con il messaggio fornito dall'utente
git commit -m "$commit_message"

# Esegue il pull e il push (puoi personalizzare i branch e il remote)
git pull origin main
git push origin main