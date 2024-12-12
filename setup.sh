mkdir -p bin
wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
tar -xvf ffmpeg-release-amd64-static.tar.xz
mv ffmpeg-*-static/ffmpeg ./bin/
mv ffmpeg-*-static/ffprobe ./bin/
chmod +x ./bin/ffmpeg ./bin/ffprobe
