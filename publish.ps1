echo "Building site..."
pelican -d -s .\publishconf.py
echo "Updating content..."
rm -r ..\jp.gh.io-master\*
cp -r .\output\* ..\jp.gh.io-master\
cd ..\jp.gh.io-master\
git add *
git commit -m "Pelican publish"
echo "Pushing..."
git push
cd ..\johnpaton.github.io\
echo "Don't forget to push the source!"