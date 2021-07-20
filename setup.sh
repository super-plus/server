if (( $EUID != 0 )); then
    echo "You need to run the setup with root permissions. Exiting"
    exit
fi

if (( $(grep SERVER_SETUP_COMPLETE "/etc/environment" | awk -F= '{print $2}') == 0 )); then
    echo "Setup is already completed! Exiting"
    exit
else
  #echo 'SERVER_SETUP_COMPLETE=1' >> /etc/environment
fi

if [ ! -f ./config.py ]; then
    echo "Which port do you want to use?"
    read -r port
    until ( ! nc -zv localhost "$port" >/dev/null 2>/dev/null )
    do
      if ( nc -zv localhost "$port" >/dev/null 2>/dev/null ); then
        echo "Port ${port} is already in use! Please select a different one."
        echo "Which port do you want to use?"
        read -r port
        if ( ! nc -zv localhost "$port" >/dev/null 2>/dev/null ); then
          break
        fi
      fi
    done

    echo "Which algorithm do you want to use for key generation?"
    echo "[1] RSA - Recommended"
    echo "[2] ECDH"
    read -r algorithm
    until [[ "$algorithm" == 1 || "$algorithm" == 2 ]]
    do
      if [[ "$algorithm" != 1 && "$algorithm" != 2 ]]; then
        echo "Please choose one of these:"
        echo "[1] RSA - Recommended"
        echo "[2] ECDH"
        read -r algorithm
        if [[ "$algorithm" == 1 || "$algorithm" == 2 ]]; then
          break
        fi
      fi
    done

    echo "Which key size do you want to use?"
    echo "[1] 4096 - Recommended"
    echo "[2] 2048"
    read -r keysize
    until [[ "$keysize" == 1 || "$keysize" == 2 ]]
    do
      if [[ "$keysize" != 1 && "$keysize" != 2 ]]; then
        echo "Please choose one of these:"
        echo "[1] 4096 - Recommended"
        echo "[2] 2048"
        read -r keysize
        if [[ "$keysize" == 1 || "$keysize" == 2 ]]; then
          break
        fi
      fi
    done

    echo "How many days should the key expire?"
    read -r days
    until [[ "$days" -gt 0 ]]
    do
      if [[ ! "$days" -gt 0 ]]; then
        echo "Please enter a positive number greater than 0"
        read -r days
        if [[ "$days" -gt 0 ]]; then
          break
        fi
      fi
    done
    wget https://gist.githubusercontent.com/rainman0607/3e9739e0d9f71b942e4e154f0e68f799/raw -O $PWD/config.py
    chmod 755 $PWD/config.py
    python3 $PWD/lib/setup/ConfigGenerator.py "$port" "$algorithm" "$keysize" "$days"
fi