echo "Cloning development branch into ./johnpaton.github.io"
git clone -b dev https://github.com/johnpaton/johnpaton.github.io johnpaton.github.io
echo "Cloning master branch into ./jp.gh.io-master"
git clone https://github.com/johnpaton/johnpaton.github.io jp.gh.io-master
echo "Cloning Pelican plugins into ./pelican-plugins"
git clone --recursive https://github.com/getpelican/pelican-plugins
echo "Installing required Python packages"
cd johnpaton.github.io
pip install -r requirements.txt
echo "Cloning custom theme into ./johnpaton.github.io/themes/flex-mod"
cd themes
git clone https://github.com/johnpaton/flex-mod
cd ../..
