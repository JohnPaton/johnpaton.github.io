cd .\output\
Start-Process python -ArgumentList '-m', 'pelican.server'
Start-Process "http://localhost:8000"
cd ..\