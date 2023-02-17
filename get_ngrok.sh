wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.tgz
tar -zcvf ngrok-v3-stable-linux-arm64.tgz
chmod +x ngrok
#./ngrok authtoken "";
#./ngrok config add-authtoken "";
./ngrok http 8080