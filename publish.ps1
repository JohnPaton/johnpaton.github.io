pelican -d -s .\publishconf.py
rm -r ..\jp.gh.io-master\*
cp -r .\output\* ..\jp.gh.io-master\
cd ..\jp.gh.io-master\
git add *
git commit -m "Pelican publish"
git push