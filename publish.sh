echo "Building site..."
pelican -d -s ./publishconf.py
echo "Updating content..."
cd ../jp.gh.io-master
git pull
rm -r *
cp -r ../johnpaton.github.io/output/* .
git add *
git commit -m "Pelican publish"
echo "Pushing..."
git push
cd ../johnpaton.github.io
echo "Don't forget to push the source!"